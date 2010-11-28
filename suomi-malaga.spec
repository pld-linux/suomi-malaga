Summary:	Description of Finnish morphology written in Malaga
Summary(pl.UTF-8):	Opis morfologii języka fińskiego napisany w języku Malaga
Name:		suomi-malaga
Version:	1.8
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/voikko/%{name}-%{version}.tar.gz
# Source0-md5:	f122495e136b8e21e33b0f71822c0fbc
URL:		http://voikko.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	malaga >= 7.8
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Description of Finnish morphology written in Malaga.

%description -l pl.UTF-8
Opis morfologii języka fińskiego napisany w języku Malaga.

%package -n voikko-fi
Summary:	Finish dictionary for voikko spellchecker/hyphenator
Summary(pl.UTF-8):	Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów voikko
Group:		Applications/Text
Requires:	libvoikko >= 2.2

%description -n voikko-fi
Finish dictionary for voikko spellchecker/hyphenator.

%description -n voikko-fi -l pl.UTF-8
Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów
voikko.

#package -n sukija-fi

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} voikko-install \
	DESTDIR=$RPM_BUILD_ROOT%{_libdir}/voikko

%clean
rm -rf $RPM_BUILD_ROOT

%files -n voikko-fi
%defattr(644,root,root,755)
%doc CONTRIBUTORS ChangeLog README
%lang(fi) %doc README.fi
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.pro
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.lex_*
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.mor_*
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.sym_*

#files -n sukija-fi
