%define betaver rc1

Summary: PHP documentation plugin for kdevelop
Name: kdevelop4-php-docs
Version: 0
Release: %mkrel -c %betaver 1
Source0: http://fr2.rpmfind.net/linux/KDE/unstable/kdevelop/3.10.0/src/kdev-php-docs-%{betaver}.tar.bz2
License: GPLv2+
Group: Development/Other
Url: http://www.kdevelop.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: kdevplatform4-devel
Requires: kdevelop4-php

%description
This plugin adds PHP documentation-view to KDevelop.

%files
%defattr(-,root,root)
%_kde_libdir/kde4/kdevphpdocs.so
%_kde_libdir/kde4/kdevphpdocs_config.so
%_kde_datadir/config.kcfg/phpdocssettings.kcfg
%_kde_services/kdevphpdocs.desktop
%_kde_services/kdevphpdocs_config.desktop

#--------------------------------------------------------------------

%prep
%setup -qn kdev-php-docs-%{betaver}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
