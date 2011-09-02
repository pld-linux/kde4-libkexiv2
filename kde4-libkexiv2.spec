%define         _state          stable
%define         orgname         libkexiv2
%define         qtver           4.7.3
Summary:	libkexiv2 - picture metadata manipulation library
Summary(pl.UTF-8):	libkexiv2 - biblioteka do obróbki metadanych obrazków
Name:		libkexiv2
Version:	4.7.1
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	78940384d4d194cc82f26f73187234d1
URL:		http://www.kde.org/
BuildRequires:	exiv2-devel >= 0.18
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	pkgconfig >= 0.9.0
Obsoletes:	kde4-kdegraphics
Obsoletes:	kde4-libkexiv2
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
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	exiv2-devel
Obsoletes:	kde4-kdegraphics-devel

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../
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
%attr(755,root,root) %ghost %{_libdir}/libkexiv2.so.10
%{_datadir}/apps/libkexiv2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkexiv2.so
%{_includedir}/%{name}
%{_pkgconfigdir}/libkexiv2.pc
