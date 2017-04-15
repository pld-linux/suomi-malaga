# TODO: sukija (both malaga and vfst)
#
# Conditional build:
%bcond_without	vfst	# dictionaries for VFST backend

Summary:	Description of Finnish morphology written in Malaga
Summary(pl.UTF-8):	Opis morfologii języka fińskiego napisany w języku Malaga
Name:		suomi-malaga
Version:	1.19
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/voikko/corevoikko/releases
Source0:	https://github.com/voikko/corevoikko/archive/rel-suomimalaga-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	51f799e600d7c66623d71f7fc44be31d
URL:		http://voikko.puimula.org/
%{?with_vfst:BuildRequires:	foma}
BuildRequires:	libstdc++-devel
BuildRequires:	malaga >= 7.8
BuildRequires:	python >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Description of Finnish morphology written in Malaga.

%description -l pl.UTF-8
Opis morfologii języka fińskiego napisany w języku Malaga.

%package -n voikko-fi-malaga
Summary:	Finish dictionary for voikko spellchecker/hyphenator
Summary(pl.UTF-8):	Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów voikko
Group:		Applications/Text
Requires:	libvoikko >= 2.2
Provides:	voikko-fi = %{version}
Obsoletes:	voikko-fi < %{version}

%description -n voikko-fi-malaga
Finish dictionary for voikko spellchecker/hyphenator.

%description -n voikko-fi-malaga -l pl.UTF-8
Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów
voikko.

%package -n voikko-fi-vfst
Summary:	Finish dictionary for voikko spellchecker/hyphenator
Summary(pl.UTF-8):	Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów voikko
Group:		Applications/Text
Requires:	libvoikko >= 3.8
Provides:	voikko-fi = %{version}
Obsoletes:	voikko-fi < %{version}

%description -n voikko-fi-vfst
Finish dictionary for voikko spellchecker/hyphenator.

%description -n voikko-fi-vfst -l pl.UTF-8
Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów
voikko.

#package -n sukija-fi

%prep
%setup -q -n corevoikko-rel-suomimalaga-%{version}

%build
%{__make} -C suomimalaga all %{?with_vfst:vvfst}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C suomimalaga voikko-install \
	DESTDIR=$RPM_BUILD_ROOT%{_libdir}/voikko

%if %{with vfst}
%{__make} -C suomimalaga vvfst-install \
	DESTDIR=$RPM_BUILD_ROOT%{_datadir}/voikko
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n voikko-fi-malaga
%defattr(644,root,root,755)
%doc suomimalaga/{CONTRIBUTORS,ChangeLog,README}
%lang(fi) %doc suomimalaga/README.fi
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.pro
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.lex_*
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.mor_*
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.sym_*

%files -n voikko-fi-vfst
%defattr(644,root,root,755)
%doc suomimalaga/{CONTRIBUTORS,ChangeLog,README}
%lang(fi) %doc suomimalaga/README.fi
%{_datadir}/voikko/5/mor-standard/autocorr.vfst
%{_datadir}/voikko/5/mor-standard/index.txt
%{_datadir}/voikko/5/mor-standard/mor.vfst

#files -n sukija-fi
