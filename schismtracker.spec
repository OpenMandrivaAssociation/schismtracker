Name:           schismtracker
Version:        20110929
Release:        %mkrel 1
URL:            http://schismtracker.org/
License:        GPLv2
Group:          Sound
Summary:        Music editor, Impulse Tracker clone
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  SDL-devel >= 1.2.10
BuildRequires:  libx11-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc-c++
BuildRequires:  python >= 2.4
BuildRequires:  mercurial

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
%__rm -rf %{buildroot}
%makeinstall

# install icons
for size in 16 22 24 32 36 48 64 72 96 128 192; do
    %__install -D -m 0644 icons/schism-icon-$size.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
%__install -D -m 0644 icons/schism-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%__install -d %{buildroot}%{_desktopdir}

cat > %{buildroot}%{_desktopdir}/%{name}.desktop << EOF
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

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/schismtracker
%{_datadir}/icons/hicolor/*/*/%{name}*
%{_desktopdir}/%{name}.desktop
%{_mandir}/*/%{name}.*

