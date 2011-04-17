%define upstream_name	 POE-Component-IRC
%define upstream_version 6.60

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A fully event-driven IRC client module
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Object::Pluggable)
BuildRequires:  perl(POE::Filter::IRCD)
BuildRequires:  perl(POE::Component::Client::DNS)
BuildRequires:  perl(POE::Component::Client::Ident)
BuildRequires:  perl(POE::Component::Pluggable)

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Component::IRC is a POE (Perl Object Environment) component
which provides a convenient way for POE applications to create a tiny
IRC client session and send and receive IRC events through it. If that
first sentence was a bit too much, go read the POE documentation over
and over until it makes some sense.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Changes
find lib -name \*.pm | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
