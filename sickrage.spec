Name:		sickchill
Version:	e094759
Release:	1%{?dist}
Summary:	Automatic Video Library Manager for TV Shows

License:	GPLv3
URL:		https://github.com/SickChill/SickChill
Source0:	https://github.com/SickChill/SickChill
Source1:        sickrage.service
Source2:        sickrage-bt.service
Source3:        transmission-settings.json
BuildRequires:	transmission-daemon python3-virtualenv
Requires:       python3

%description
SickChill is an automatic Video Library Manager for TV Shows. It watches
for new episodes of your favorite shows, and when they are posted it does
its magic.

%prep
git clone -q %{URL} .

%build
#%configure
#%make_build

%install
#%make_install

%files
%doc

%changelog
* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - e094759-1
- Modernize spec for AlmaLinux 10
