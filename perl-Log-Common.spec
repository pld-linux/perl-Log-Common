%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Common
Summary:	Log::Common perl module
Summary(pl):	Modu³ perla Log::Common
Name:		perl-Log-Common
Version:	1.00
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Common logs messages in the httpd access and error log styles.

%description -l pl
Log::Common zapisuje logi w sposób podobny do logów access i error
serwera httpd.

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
%doc ChangeLog README
%{perl_sitelib}/Log/Common.pm
%{_mandir}/man3/*
