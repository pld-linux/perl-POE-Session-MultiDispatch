#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Session-MultiDispatch
Summary:	POE::Session::MultiDispatch - callback dispatch for session events
Summary(pl):	POE::Session::MultiDispatch - wysy³anie callbacka dla zdarzeñ sesji
Name:		perl-POE-Session-MultiDispatch
Version:	1.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	59b2e2614c3a048d4ad5d0bd87ecd044
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Session::MultiDispatch is a drop in replacement for POE::Session
that adds callback dispatch functionality to POE sessions. Each event
may have multiple handlers associated with it. Fine control over the
order of execution is available using helper methods that extend the
interface of a POE::Session.

%description -l pl
POE::Session::MultiDispatch to zamiennik POE::Session dodaj±cy
funkcjonalno¶æ wysy³ania callbacków do sesji POE. Ka¿de zdarzenie mo¿e
mieæ wiele powi±zanych ze sob± funkcji obs³ugi. Dostêpna jest dobra
kontrola nad kolejno¶ci± wykonywania przy u¿yciu metod pomocniczych
rozszerzaj±cych interfejs POE::Session.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
