%include	/usr/lib/rpm/macros.perl
Summary:	Log-Common perl module
Summary(pl):	Modu� perla Log-Common
Name:		perl-Log-Common
Version:	1.00
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Log/Log-Common-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log-Common logs messages in the httpd access and error log styles.

%description -l pl
Log-Common zapisuje logi w spos�b podobny do log�w access i error
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
