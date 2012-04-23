Name:		fet
Summary:	Free Timetabling Software
Version:	5.17.0
Release:	1
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
# installing samples
%__cp -R examples %{buildroot}%{_datadir}/%{name}/
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

%if %{mdvver} >= 201200
%find_lang %{name} --with-qt
%else
touch %{name}.lang
%endif

%files -f %{name}.lang
%doc doc/algorithm/*.txt
%doc AUTHORS ChangeLog COPYING
%doc README REFERENCES THANKS TODO TRANSLATORS
%{_bindir}/fet
%{_datadir}/applications/fet.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/examples
%{_mandir}/man1/fet.1.xz
/usr/share/fet/translations/fet_untranslated.qm
%if %{mdvver} < 201200
%lang(ar)/usr/share/fet/translations/fet_ar.qm
%lang(ca)/usr/share/fet/translations/fet_ca.qm
%lang(da)/usr/share/fet/translations/fet_da.qm
%lang(de)/usr/share/fet/translations/fet_de.qm
%lang(el)/usr/share/fet/translations/fet_el.qm
%lang(es)/usr/share/fet/translations/fet_es.qm
%lang(fa)/usr/share/fet/translations/fet_fa.qm
%lang(fr)/usr/share/fet/translations/fet_fr.qm
%lang(gl)/usr/share/fet/translations/fet_gl.qm
%lang(he)/usr/share/fet/translations/fet_he.qm
%lang(hu)/usr/share/fet/translations/fet_hu.qm
%lang(id)/usr/share/fet/translations/fet_id.qm
%lang(it)/usr/share/fet/translations/fet_it.qm
%lang(lt)/usr/share/fet/translations/fet_lt.qm
%lang(mk)/usr/share/fet/translations/fet_mk.qm
%lang(ms)/usr/share/fet/translations/fet_ms.qm
%lang(nl)/usr/share/fet/translations/fet_nl.qm
%lang(pl)/usr/share/fet/translations/fet_pl.qm
%lang(pt_BR)/usr/share/fet/translations/fet_pt_BR.qm
%lang(ro)/usr/share/fet/translations/fet_ro.qm
%lang(ru)/usr/share/fet/translations/fet_ru.qm
%lang(si)/usr/share/fet/translations/fet_si.qm
%lang(sk)/usr/share/fet/translations/fet_sk.qm
%lang(sr)/usr/share/fet/translations/fet_sr.qm
%lang(tr)/usr/share/fet/translations/fet_tr.qm
%lang(uk)/usr/share/fet/translations/fet_uk.qm
%lang(vi)/usr/share/fet/translations/fet_vi.qm
%endif
