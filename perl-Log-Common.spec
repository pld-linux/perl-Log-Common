%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Common
Summary:	Log::Common perl module
Summary(pl):	Modu� perla Log::Common
Name:		perl-Log-Common
Version:	1.00
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Common logs messages in the httpd access and error log styles.

%description -l pl
Log::Common zapisuje logi w spos�b podobny do log�w access i error
serwera httpd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Log/Common.pm
%{_mandir}/man3/*
