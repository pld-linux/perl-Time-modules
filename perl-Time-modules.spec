#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	modules
Summary:	Various Time:: Perl modules
Summary(pl):	R�ne modu�y Perla Time::
Name:		perl-Time-modules
Version:	2003.1126
Release:	1
License:	free (see manuals)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3bda3a2935c2d7d099c8001f583c4cb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time-modules package contains the following modules: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

%description -l pl
Pakiet Time-modules zawiera nastepuj�ce modu�y: Time::CTime,
Time::JulianDay, Time::ParseDate, Time::Timezone, Time::DaysInMonth.

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
%doc README CHANGELOG
%{perl_vendorlib}/Time/*.pm
%{_mandir}/man3/*
