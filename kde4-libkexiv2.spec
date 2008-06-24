Summary:	libkexiv2 - picture metadata manipulation library
Summary(pl.UTF-8):	libkexiv2 - biblioteka do obróbki metadanych obrazków
Name:		libkexiv2
Version:	0.1.7
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	adfd55e11f919533ba450d4d49ef078f
Patch0:		kde-ac260-lt.patch
URL:		http://www.kipi-plugins.org/drupal/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	exiv2-devel >= 0.14
BuildRequires:	kdelibs-devel >= 9:3.4.0
BuildRequires:	pkgconfig >= 0.9.0
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
Requires:	kdelibs-devel >= 9:3.4.0

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE.rev
%attr(755,root,root) %{_libdir}/libkexiv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiv2.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkexiv2.so
%{_libdir}/libkexiv2.la
%{_includedir}/%{name}
%{_pkgconfigdir}/libkexiv2.pc
