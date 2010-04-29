Summary: PHP documentation plugin for kdevelop
Name: kdevelop4-php-docs
Version: 1.0.0
Release: %mkrel 2
Source0: http://fr2.rpmfind.net/linux/KDE/stable/kdevelop/4.0.0/src/kdevelop-php-docs-%{version}.tar.bz2
License: GPLv2+
Group: Development/Other
Url: http://www.kdevelop.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: kdevplatform4-devel >= 4:0.10.2
Requires: kdevelop4-php >= 1.0.0

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
%setup -qn kdevelop-php-docs-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
