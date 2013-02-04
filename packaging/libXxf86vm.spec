Name:           libXxf86vm
Version:        1.1.2
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System Environment/Libraries
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXxf86vm runtime library

%package devel
Summary:        X
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libXxf86vm development package

%prep
%setup -q

%build
%reconfigure --disable-static 
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING 
%{_libdir}/libXxf86vm.so.1
%{_libdir}/libXxf86vm.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_includedir}/X11/extensions/xf86vmode.h
