%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	modules
Summary:	Time::modules perl module
Summary(pl):	Modu³ perla Time::modules
Name:		perl-Time-modules
Version:	2002.1001
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::modules package contains the following modules: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

%description -l pl
Pakiet Time::modules zawiera nastepuj±ce modu³y: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%{perl_sitelib}/Time/*.pm
%{_mandir}/man3/*
