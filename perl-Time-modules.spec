%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Time-modules perl module
Summary(pl):	Modu³ perla Time-modules
Name:		perl-Time-modules
Version:	98.112901
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/Time-modules-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Time-modules package contains the following modules: 
Time::CTime.pm, Time::JulianDay.pm, Time::ParseDate.pm, Time::Timezone.pm,
Time::DaysInMonth.pm.

%description -l pl
Pakiet Time-modules zawiera nastepuj±ce modu³y: 
Time::CTime.pm, Time::JulianDay.pm, Time::ParseDate.pm, Time::Timezone.pm,
Time::DaysInMonth.pm.

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
