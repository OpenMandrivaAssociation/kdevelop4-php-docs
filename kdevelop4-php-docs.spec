%define kdevelop_ver 4.%(echo %{version} | cut -d. -f2,3)

Summary:	PHP documentation plugin for kdevelop
Name:		kdevelop4-php-docs
Version:	1.4.1
Release:	2
License:	GPLv2+
Group:		Development/Other
Url:		http://www.kdevelop.org
Source0:	http://fr2.rpmfind.net/linux/KDE/unstable/kdevelop/%{kdevelop_ver}/src/kdevelop-php-docs-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdevplatform4-devel >= 4:%{version}
Requires:	kdevelop4-php >= %{version}

%description
This plugin adds PHP documentation-view to KDevelop.

%files -f kdevphpdocs.lang
%{_kde_libdir}/kde4/kdevphpdocs.so
%{_kde_libdir}/kde4/kdevphpdocs_config.so
%{_kde_datadir}/config.kcfg/phpdocssettings.kcfg
%{_kde_services}/kdevphpdocs.desktop
%{_kde_services}/kdevphpdocs_config.desktop

#--------------------------------------------------------------------

%prep
%setup -qn kdevelop-php-docs-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang kdevphpdocs


