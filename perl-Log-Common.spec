%define	pdir	Log
%define	pnam	Common
%include	/usr/lib/rpm/macros.perl
Summary:	Log-Common perl module
Summary(pl):	Modu³ perla Log-Common
Name:		perl-Log-Common
Version:	1.00
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log-Common logs messages in the httpd access and error log styles.

%description -l pl
Log-Common zapisuje logi w sposób podobny do logów access i error
serwera httpd.

%prep
%setup -q -n Log-Common-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Log/Common.pm
%{_mandir}/man3/*
