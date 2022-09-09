Name:		sickchill
Version:	e094759
Release:	1%{?dist}
Summary:	Automatic Video Library Manager for TV Shows

Group:		Web
License:	GPLv3
URL:		https://github.com/SickChill/SickChill
Source0:	https://github.com/SickChill/SickChill
Source1:        sickrage.service
Source2:        sickrage-bt.service
Source3:        transmission-settings.json
BuildRequires:	transmission-daemon python3-virtualenv
Requires:       python3

%description


%prep
%clean
git clone -q %{URL} .

%build
#%configure
#make %{?_smp_mflags}


%install
#%make_install


%files
%doc



%changelog

