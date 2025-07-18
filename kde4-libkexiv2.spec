%define         _state          stable
%define         orgname         libkexiv2
Summary:	libkexiv2 - picture metadata manipulation library
Summary(pl.UTF-8):	libkexiv2 - biblioteka do obróbki metadanych obrazków
Name:		kde4-libkexiv2
Version:	4.14.3
Release:	7
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	ba361677df71f5946a3f0b0bcace01a8
Patch0:		exiv2-0.27.patch
URL:		http://www.kde.org/
BuildRequires:	exiv2-devel >= 0.20
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	exiv2-libs >= 0.20
Obsoletes:	kde4-kdegraphics
Obsoletes:	libkexiv2 <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libkexiv2 is a KDE wrapper around Exiv2 library to manipulate pictures
metadata. This library is used by kipi-plugins, digiKam and others
kipi host programs.

%description -l pl.UTF-8
libkexiv2 to obudowanie KDE biblioteki Exiv2 do obróbki metadanych
obrazków. Ta biblioteka jest wykorzystywana przez pakiety
kipi-plugins, digiKam i inne programy oparte na kiki.

%package devel
Summary:	Header files for libkexiv2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libkexiv2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	exiv2-devel >= 0.20
Obsoletes:	kde4-kdegraphics-devel < 4.6.99
Obsoletes:	libkexiv2-devel <= 4.8.0

%description devel
Header files for libkexiv2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libkexiv2.

%prep
%setup -q -n %{orgname}-%{version}
%patch -P0 -p1

%build
install -d build
cd build
%cmake \
	../ \
	-DEXIV2_VERSION:STRING="0.27"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libkexiv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiv2.so.11
%{_datadir}/apps/libkexiv2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkexiv2.so
%{_includedir}/libkexiv2
%{_pkgconfigdir}/libkexiv2.pc
%{_libdir}/cmake/libkexiv2*
