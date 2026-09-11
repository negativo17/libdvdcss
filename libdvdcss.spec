Summary:        A portable abstraction library for DVD decryption
Name:           libdvdcss
Version:        1.6.0
Release:        1%{?dist}
License:        GPLv2+
URL:            http://www.videolan.org/%{name}/

Source0:        https://code.videolan.org/videolan/libdvdcss/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  meson >= 0.60.0

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

# Old doxygen versions do not have the -q switch
sed -i -e "s/'-q', //g" doc/meson.build

%build
%meson \
    -Denable_docs=true \
    -Denable_examples=true
%meson_build

%install
%meson_install
rm -f %{buildroot}%{_libdir}/*.a

%files
%license %{_pkgdocdir}/COPYING
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/NEWS
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.4.0

%files devel
%doc %{_pkgdocdir}/html
%{_includedir}/dvdcss
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Sep 11 2026 Simone Caronni <negativo17@gmail.com> - 1.6.0-1
- Update to 1.6.0.

* Thu Mar 13 2025 Simone Caronni <negativo17@gmail.com> - 1.4.3-4
- Clean up SPEC file, trim changelog.

* Wed Sep 01 2021 Simone Caronni <negativo17@gmail.com> - 1.4.3-3
- Update to final 1.4.3 release.

* Thu Dec 03 2020 Simone Caronni <negativo17@gmail.com> - 1.4.3-2.20200429giteb1f6ed
- Explicitly declare shared object versions.

* Sun Jan 12 2020 Simone Caronni <negativo17@gmail.com> - 1.4.3-1.20191013git8398d94
- Update to latest 1.4.3 snapshot.
- Use RPM macros.
