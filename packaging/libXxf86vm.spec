Name:           libXxf86vm
Version:        1.1.2
Release:        1
License:        MIT
Summary:        X.org libXxf86vm library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXxf86vm runtime library

%package devel
Summary:        X.org libXxf86vm library
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
%make_install

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
