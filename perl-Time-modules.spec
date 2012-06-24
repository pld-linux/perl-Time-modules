%define	pdir	Time
%define	pnam	modules
%include	/usr/lib/rpm/macros.perl
Summary:	Time-modules perl module
Summary(pl):	Modu� perla Time-modules
Name:		perl-Time-modules
Version:	101.062101
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time-modules package contains the following modules: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

%description -l pl
Pakiet Time-modules zawiera nastepuj�ce modu�y: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

%prep
%setup -q -n Time-modules-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Time/*.pm
%{_mandir}/man3/*
