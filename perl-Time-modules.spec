%include	/usr/lib/rpm/macros.perl
Summary:	Time-modules perl module
Summary(pl):	Modu³ perla Time-modules
Name:		perl-Time-modules
Version:	99.062301
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/Time-modules-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Time-modules package contains the following modules: 
Time::CTime, Time::JulianDay, Time::ParseDate, Time::Timezone,
Time::DaysInMonth.

%description -l pl
Pakiet Time-modules zawiera nastepuj±ce modu³y: 
Time::CTime, Time::JulianDay, Time::ParseDate, Time::Timezone,
Time::DaysInMonth.

%prep
%setup -q -n Time-modules-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Time-modules
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGELOG}.gz

%{perl_sitelib}/Time/*.pm
%{perl_sitearch}/auto/Time-modules

%{_mandir}/man3/*
