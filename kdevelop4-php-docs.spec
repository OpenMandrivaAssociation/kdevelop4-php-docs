Summary: PHP documentation plugin for kdevelop
Name: kdevelop4-php-docs
Version: 1.3.1
Release: %mkrel 1
Source0: http://fr2.rpmfind.net/linux/KDE/stable/kdevelop/4.2.3/src/kdevelop-php-docs-%{version}.tar.bz2
License: GPLv2+
Group: Development/Other
Url: http://www.kdevelop.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: kdevplatform4-devel >= 4:1.3.0
Requires: kdevelop4-php >= %{version}

%description
This plugin adds PHP documentation-view to KDevelop.

%files -f kdevphpdocs.lang
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

%find_lang kdevphpdocs

%clean
rm -rf %{buildroot}
