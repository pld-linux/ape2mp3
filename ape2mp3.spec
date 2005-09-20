Summary:	Converts ape-image to mp3-tracks
Summary(pl):	Konwertuje obraz ape do scie¿ek mp3
Name:		ape2mp3
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://mesh.dl.sourceforge.net/sourceforge/ape2mp3/%{name}
# Source0-md5:	30c5003a3a5abe461d8821d4aec1e8a4
URL:		http://sourceforge.net/projects/ape2mp3/
Requires:	bash
Requires:	bchunk
Requires:	lame
Requires:	mac
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts ape-image to mp3-tracks.

%description -l pl
Konwertuje obrazy w formacie ape do scie¿ek mp3

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_bindir}/ape2mp3
