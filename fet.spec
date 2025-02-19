%global debug_package %{nil}

Name:		fet
Summary:	Free Timetabling Software
Version:	7.0.3
Release:	1
Group:		Education
License:	GPLv2+
URL:		https://lalescu.ro/liviu/fet/
Source0:	http://lalescu.ro/liviu/fet/download/%{name}-%{version}.tar.bz2
BuildRequires:  qmake-qt6
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6PrintSupport)


%description
FET is free timetabling software (licensed under GNU GPL v2 or later). This
program aims to automatically generate the timetable of a school,
high-school or university. It may be used for other timetabling purposes.

FET can mean "Free Educational Timetabling" (the "E" in the middle may
also stand for other words, based on your personal preference).

%prep
%setup 

%build
qmake-qt6 fet.pro
%make_build

%install
%make_install \
    INSTALL_ROOT=%{buildroot}

%__install -d %{buildroot}%{_datadir}/licenses/%{name}
mv %{buildroot}%{_datadir}/doc/%{name}/licenses/*  %{buildroot}%{_datadir}/licenses/%{name}
rmdir %{buildroot}%{_datadir}/doc/%{name}/licenses
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING

%find_lang %{name} --with-qt

%files -f %{name}.lang
%{_datadir}/doc/%{name}/*
%{_datadir}/licenses/%{name}/*
%license COPYING 
%{_bindir}/fet*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/examples/*
%{_datadir}/applications/fet.desktop
%{_datadir}/icons/hicolor/*/apps/fet.*
%{_mandir}/man1/fet*.1.zst


