Name:		fet
Summary:	Free Timetabling Software
Version:	5.18.2
Release:	2
Group:		Education
License:	GPLv2+
URL:		http://lalescu.ro/liviu/fet/
Source0:	http://lalescu.ro/liviu/fet/download/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel

%description
FET is free timetabling software (licensed under GNU GPL v2 or later). This
program aims to automatically generate the timetable of a school,
high-school or university. It may be used for other timetabling purposes.

FET can mean "Free Educational Timetabling" (the "E" in the middle may
also stand for other words, based on your personal preference).

%prep
%setup -q

%build
%qmake_qt4
%make

%install
# manual installation, make file doesn't provide it
%__install -d -m 755 %{buildroot}%{_datadir}/%{name}
%__install -d -m 755 %{buildroot}%{_datadir}/%{name}/translations
# moved man file to /usr/share/man/man1/
xz -k 'doc/fet.1'
%__install -D -m 644 'doc/fet.1.xz' %{buildroot}%{_mandir}/man1/fet.1.xz
# installing translations
%__cp  translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
# installing binary.
%__install -D -m 755 fet %{buildroot}%{_bindir}/fet
%__install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/fet.desktop << EOF
[Desktop Entry]
Type=Application
Name=Timetable Generator
Name[de]=Stundenplan Generator
Name[ru]=Генератор расписаний
GenericName=Timetable software for schools
GenericName[de]=Stundenplan Generator
GenericName[ru]=Генератор расписаний
Comment=Generate timetables for educational institutions
Comment[de]=Erzeugt Stundenplne fr Lehranstalten
Comment[ru]=Составление расписаний для учебных заведений
Icon=fet
Exec=fet
Terminal=false
StartupNotify=true
Categories=Office;
EOF

%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc doc/algorithm/*.txt
%doc AUTHORS ChangeLog COPYING
%doc README REFERENCES THANKS TODO TRANSLATORS
%doc examples
%{_bindir}/fet
%{_datadir}/applications/fet.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/fet_untranslated.qm
%{_mandir}/man1/fet.1.xz
