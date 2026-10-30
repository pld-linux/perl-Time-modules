#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Time
%define		pnam	ParseDate
Summary:	Various Time:: Perl modules
Summary(pl.UTF-8):	Różne moduły Perla Time::
Name:		perl-Time-modules
%define	pver	2026.033
Version:	%{pver}0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/B/BP/BPS/%{pdir}-%{pnam}-%{pver}.tar.gz
# Source0-md5:	31e4fb54f3e047255285fc3f9d73d559
URL:		https://metacpan.org/dist/Time-ParseDate
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# t/datetime.t, t/order*.t set TZ to America/Los_Angeles, Europe/Moscow
BuildRequires:	tzdata-zoneinfo
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time-modules package contains the following modules: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

%description -l pl.UTF-8
Pakiet Time-modules zawiera nastepujące moduły: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

%prep
%setup -q -n %{pdir}-%{pnam}-%{pver}

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
%doc Changes README
%{perl_vendorlib}/Time/*.pm
%{_mandir}/man3/*
