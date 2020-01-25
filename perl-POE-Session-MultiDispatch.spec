#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	POE
%define		pnam	Session-MultiDispatch
Summary:	POE::Session::MultiDispatch - callback dispatch for session events
Summary(pl.UTF-8):	POE::Session::MultiDispatch - wysyłanie callbacka dla zdarzeń sesji
Name:		perl-POE-Session-MultiDispatch
Version:	1.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	59b2e2614c3a048d4ad5d0bd87ecd044
URL:		http://search.cpan.org/dist/POE-Session-MultiDispatch/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE
BuildRequires:	perl-Test-Simple
%endif
Requires:	perl-POE
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Session::MultiDispatch is a drop in replacement for POE::Session
that adds callback dispatch functionality to POE sessions. Each event
may have multiple handlers associated with it. Fine control over the
order of execution is available using helper methods that extend the
interface of a POE::Session.

%description -l pl.UTF-8
POE::Session::MultiDispatch to zamiennik POE::Session dodający
funkcjonalność wysyłania callbacków do sesji POE. Każde zdarzenie może
mieć wiele powiązanych ze sobą funkcji obsługi. Dostępna jest dobra
kontrola nad kolejnością wykonywania przy użyciu metod pomocniczych
rozszerzających interfejs POE::Session.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
