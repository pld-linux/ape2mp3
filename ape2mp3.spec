Summary:	Converts ape-image to MP3-tracks
Summary(pl):	Konwersja obrazów ape do scie¿ek MP3
Name:		ape2mp3
Version:	0.1
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/ape2mp3/%{name}
# Source0-md5:	30c5003a3a5abe461d8821d4aec1e8a4
Patch0:		%{name}-file.patch
URL:		http://sourceforge.net/projects/ape2mp3/
Requires:	bash
Requires:	bchunk >= 1.0
Requires:	lame
Requires:	mac >= 3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ape2mp3 converts ape-image to MP3-tracks.

%description -l pl
ape2mp3 konwertuje obrazy w formacie ape do scie¿ek MP3.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

patch $RPM_BUILD_ROOT%{_bindir}/%{name} %{PATCH0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ape2mp3
