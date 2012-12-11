Name:		schismtracker
Version:	20120425
Release:	1
Summary:	Music editor, Impulse Tracker clone
License:	GPLv2
Group:		Sound
URL:		http://schismtracker.org/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	gcc-c++
BuildRequires:	python >= 2.4
BuildRequires:	mercurial

%description
Schism Tracker is a free reimplementation of Impulse Tracker, a
program used to create high quality music without the requirements of
specialized, expensive equipment, and with a unique "finger feel"
that is difficult to replicate in-part. The player is based on a
highly modified version of the Modplug engine, with a number of
bug-fixes and changes to improve IT playback.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall

# install icons
for size in 16 22 24 32 36 48 64 72 96 128 192; do
    install -D -m 0644 icons/schism-icon-$size.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
install -D -m 0644 icons/schism-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -d %{buildroot}%{_datadir}/applications

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Schism Tracker
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;AudioVideoEditing;
EOF

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/schismtracker
%{_datadir}/icons/hicolor/*/*/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/*/%{name}.*

%changelog
* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 20110929-1mdv2011.0
+ Revision: 701946
- imported package schismtracker


* Thu Sep 29 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 20110929-1mdv2010.2
- Latest snapshot

* Sun Apr 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 20110424-69.1mib2010.2
- Initial package for 2010.2
- MIB (Mandriva International Backports)