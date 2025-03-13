Summary:        A portable abstraction library for DVD decryption
Name:           libdvdcss
Version:        1.4.3
Release:        4%{?dist}
License:        GPLv2+
URL:            http://www.videolan.org/%{name}/

Source0:        http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool

%description
This is a portable abstraction library for DVD decryption which is used by
the VideoLAN project, a full MPEG2 client/server solution.  You will need
to install this package in order to have encrypted DVD playback with the
VideoLAN client and the Xine navigation plugin.

%package devel
Summary:     Header files and development libraries for %{name}
Requires:    %{name} = %{version}-%{release}
Requires:    pkgconfig

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name}, 
you will need to install %{name}-devel.

%prep
%autosetup

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
rm -fr %{buildroot}%{_docdir}/%{name} \
    %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.2.0

%files devel
%doc doc/html
%{_includedir}/dvdcss
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Mar 13 2025 Simone Caronni <negativo17@gmail.com> - 1.4.3-4
- Clean up SPEC file, trim changelog.

* Wed Sep 01 2021 Simone Caronni <negativo17@gmail.com> - 1.4.3-3
- Update to final 1.4.3 release.

* Thu Dec 03 2020 Simone Caronni <negativo17@gmail.com> - 1.4.3-2.20200429giteb1f6ed
- Explicitly declare shared object versions.

* Sun Jan 12 2020 Simone Caronni <negativo17@gmail.com> - 1.4.3-1.20191013git8398d94
- Update to latest 1.4.3 snapshot.
- Use RPM macros.
