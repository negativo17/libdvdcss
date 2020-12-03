%global commit0 eb1f6ed7a012b390e23549778bcc7b54c55869d4
%global date 20200429
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Summary:        A portable abstraction library for DVD decryption
Name:           libdvdcss
Version:        1.4.3
Release:        2%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
License:        GPLv2+
URL:            http://www.videolan.org/%{name}/

%if 0%{?tag:1}
Source0:        http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
%else
Source0:        https://code.videolan.org/videolan/%{name}/-/archive/%{commit0}/%{name}-%{commit0}.tar.bz2#/%{name}-%{shortcommit0}.tar.bz2
%endif

BuildRequires:  doxygen
BuildRequires:  gcc
%if 0%{!?tag:1}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

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
%if 0%{?tag:1}
%autosetup
%else
%autosetup -n %{name}-%{commit0}
%endif

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
rm -fr %{buildroot}%{_docdir}/%{name} \
    %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

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
* Thu Dec 03 2020 Simone Caronni <negativo17@gmail.com> - 1.4.3-2.20200429giteb1f6ed
- Explicitly declare shared object versions.

* Sun Jan 12 2020 Simone Caronni <negativo17@gmail.com> - 1.4.3-1.20191013git8398d94
- Update to latest 1.4.3 snapshot.
- Use RPM macros.

* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 1.4.2-2
- Add GCC build requirement.

* Tue Apr 24 2018 Simone Caronni <negativo17@gmail.com> - 1.4.2-1
- Update to 1.4.2.

* Wed Jan 24 2018 Simone Caronni <negativo17@gmail.com> - 1.4.1-1
- Update to 1.4.1.

* Thu Jan 28 2016 Simone Caronni <negativo17@gmail.com> - 1.4.0-1
- Udpate to 1.4.0.

* Sat Oct 31 2015 Simone Caronni <negativo17@gmail.com> - 1.3.99-1
- Update to 1.3.99.

* Fri Oct 24 2014 Simone Caronni <negativo17@gmail.com> - 1.3.0-1
- Update to 1.3.0.
- Remove RHEL 5 obsolete tags from SPEC file.

* Fri Nov 15 2013 Simone Caronni <negativo17@gmail.com> - 1.2.13-2
- Run ldconfig in scriptlets.

* Tue May 07 2013 Simone Caronni <negativo17@gmail.com> - 1.2.13-1
- Update to 1.2.13.
- Add doxygen docs in devel subpackage.

* Mon Mar 12 2012 Remi Collet <RPMS@famillecollet.com> - 1.2.12-1
- Update to 1.2.12

* Sat Feb 18 2012 Remi Collet <RPMS@famillecollet.com> - 1.2.11-2
- If unsure, assume the drive is of RPC-I type

* Tue Nov 22 2011 Remi Collet <RPMS@famillecollet.com> - 1.2.11-1
- Update to 1.2.11
