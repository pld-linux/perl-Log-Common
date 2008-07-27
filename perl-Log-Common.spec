%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Common
Summary:	Log::Common perl module
Summary(pl.UTF-8):	Moduł perla Log::Common
Name:		perl-Log-Common
Version:	1.00
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d43342731ea415cfb2e49ac4a06c73cf
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Common logs messages in the httpd access and error log styles.

%description -l pl.UTF-8
Log::Common zapisuje logi w sposób podobny do logów access i error
serwera httpd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Log/Common.pm
%{_mandir}/man3/*
