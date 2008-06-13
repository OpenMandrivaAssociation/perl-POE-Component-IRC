%define module	POE-Component-IRC
%define name	perl-%{module}
%define version	5.80
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A fully event-driven IRC client module
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(POE::Filter::IRCD)
BuildRequires:  perl(POE::Component::Client::DNS)
BuildRequires:  perl(POE::Component::Client::Ident)
BuildRequires:  perl(POE::Component::Pluggable)
BuildRequires:  perl(Date::Format)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
POE::Component::IRC is a POE (Perl Object Environment) component
which provides a convenient way for POE applications to create a tiny
IRC client session and send and receive IRC events through it. If that
first sentence was a bit too much, go read the POE documentation over
and over until it makes some sense.

%prep
%setup -q -n %{module}-%{version}
chmod 644 README Changes
find lib -name \*.pm | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes examples
%{perl_vendorlib}/POE
%_mandir/*/*


