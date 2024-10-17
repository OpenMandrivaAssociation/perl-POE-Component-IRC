%define upstream_name  POE-Component-IRC
%define upstream_version 6.80

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A fully event-driven IRC client module
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Date::Format)
BuildRequires:	perl(IRC::Utils)
BuildRequires:	perl(Object::Pluggable)
BuildRequires:	perl(POE::Filter::IRCD)
BuildRequires:	perl(POE::Component::Client::DNS)
BuildRequires:	perl(POE::Component::Client::Ident)
BuildRequires:	perl(POE::Component::Pluggable)
BuildRequires:	perl(POE::Component::Syndicator)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes examples
%{perl_vendorlib}/POE
%{_mandir}/*/*

%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.610.0-1mdv2011.0
+ Revision: 662497
- new version

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.600.0-1
+ Revision: 654265
- update to new version 6.60

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.540.0-1
+ Revision: 644795
- update to new version 6.54

* Sat Nov 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.520.0-1mdv2011.0
+ Revision: 597087
- update to 6.52

* Mon Sep 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.390.0-1mdv2011.0
+ Revision: 576300
- update to 6.39

* Mon Aug 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.370.0-1mdv2011.0
+ Revision: 572237
- update to 6.37

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.360.0-1mdv2011.0
+ Revision: 561943
- update to 6.36

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.350.0-1mdv2011.0
+ Revision: 552485
- update to 6.35

* Mon Mar 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.280.0-1mdv2010.1
+ Revision: 519960
- update to 6.28

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.240.0-1mdv2010.1
+ Revision: 504494
- update to 6.24

* Wed Jan 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.220.0-1mdv2010.1
+ Revision: 493955
- update to 6.22

* Sat Jan 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.200.0-1mdv2010.1
+ Revision: 492160
- update to 6.20

* Sat Dec 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.180.0-1mdv2010.1
+ Revision: 477633
- update to 6.18

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.160.0-1mdv2010.1
+ Revision: 461349
- update to 6.16

* Fri Sep 25 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.140.0-1mdv2010.0
+ Revision: 448608
- update to 6.14

* Thu Sep 10 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.120.0-1mdv2010.0
+ Revision: 437203
- update to 6.12

* Wed Aug 19 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.100.0-1mdv2010.0
+ Revision: 418125
- update to 6.10

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.80.0-1mdv2010.0
+ Revision: 408037
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.08-1mdv2010.0
+ Revision: 383538
- update to new version 6.08

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.06-1mdv2010.0
+ Revision: 371733
- update to new version 6.06

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.04-1mdv2009.1
+ Revision: 353642
- update to new version 6.04

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.02-1mdv2009.1
+ Revision: 352917
- update to new version 6.02

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.98-1mdv2009.1
+ Revision: 347693
- update to new version 5.98

* Fri Jan 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.96-1mdv2009.1
+ Revision: 335511
- update to new version 5.96

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.90-1mdv2009.1
+ Revision: 333407
- update to new version 5.90

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.88-1mdv2009.0
+ Revision: 277970
- update to new version 5.88

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.86-1mdv2009.0
+ Revision: 242076
- update to new version 5.86

* Fri Jun 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.84-1mdv2009.0
+ Revision: 229493
- update to new version 5.84

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.82-1mdv2009.0
+ Revision: 220159
- update to new version 5.82

* Fri Jun 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.80-1mdv2009.0
+ Revision: 218725
- update to new version 5.80

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.78-1mdv2009.0
+ Revision: 214556
- new version
- update to new version 5.76

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.74-1mdv2009.0
+ Revision: 193924
- update to new version 5.74

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.70-1mdv2008.1
+ Revision: 178288
- update to new version 5.70

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.68-1mdv2008.1
+ Revision: 173912
- update to new version 5.68
- update to new version 5.68

* Wed Feb 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.66-1mdv2008.1
+ Revision: 173296
- update to new version 5.66

* Sun Feb 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.64-1mdv2008.1
+ Revision: 169978
- update to new version 5.64

* Fri Feb 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.62-1mdv2008.1
+ Revision: 164024
- update to new version 5.62

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 5.60-1mdv2008.1
+ Revision: 163389
- update to new version 5.60

* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.58-1mdv2008.1
+ Revision: 162590
- update to new version 5.58

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 5.56-1mdv2008.1
+ Revision: 161381
- update to new version 5.56

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.54-1mdv2008.1
+ Revision: 159904
- update to new version 5.54

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.52-1mdv2008.1
+ Revision: 152844
- update to new version 5.52

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.40-1mdv2008.1
+ Revision: 138347
- update to new version 5.40
- update to new version 5.40

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.38-1mdv2008.1
+ Revision: 116173
- update to new version 5.38

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.36-1mdv2008.1
+ Revision: 105308
- update to new version 5.36

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.34-1mdv2008.0
+ Revision: 55843
- update to new version 5.34

* Sun Jul 01 2007 Olivier Thauvin <nanardon@mandriva.org> 5.32-1mdv2008.0
+ Revision: 46224
- 5.32

* Fri May 04 2007 Olivier Thauvin <nanardon@mandriva.org> 5.29-1mdv2008.0
+ Revision: 22237
- 5.29

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 5.28-1mdv2008.0
+ Revision: 20337
- 5.28

* Fri Apr 20 2007 Olivier Thauvin <nanardon@mandriva.org> 5.24-1mdv2008.0
+ Revision: 16067
- 5.24


* Sat Jan 06 2007 Olivier Thauvin <nanardon@mandriva.org> 5.18-1mdv2007.0
+ Revision: 104818
- 5.18

* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 5.16-1mdv2007.1
+ Revision: 94358
- 5.16
- 5.00

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 4.97-1mdv2007.0
+ Revision: 54036
- 4.97
- Import perl-POE-Component-IRC

* Mon Jul 10 2006 Emmanuel Andry <eandry@mandriva.org> 4.95-1mdv2007.0
- New version 4.95

* Sat Jun 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.93-1mdv2007.0
- New version 4.93

* Thu Jun 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.91-1mdv2007.0
- New release 4.91

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.90-1mdv2007.0
- New release 4.90

* Mon May 01 2006 Olivier Thauvin <nanardon@mandriva.org> 4.86-1mdk
- 4.86

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.85-1mdk
- New release 4.85
- better source URL
- better buildrequires syntax

* Sun Apr 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.81-1mdk
- New release 4.81

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.80-1mdk
- New release 4.80

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.79-1mdk
- New release 4.79

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 4.77-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- drop explicit requires
- fix directory ownership

* Mon Dec 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.75-1mdk
- 4.75

* Thu Oct 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.74-1mdk
- 4.74

* Mon Oct 17 2005 Olivier Thauvin <nanardon@mandriva.org> 4.71-1mdk
- 4.71

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 4.70-2mdk
- Fix BuildRequires

* Tue Sep 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.70-1mdk
- 4.70
- Fix permissions

* Thu Sep 08 2005 Olivier Thauvin <nanardon@mandriva.org> 4.69-1mdk
- 4.69

* Sat Jun 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.62-1mdk
- 4.62

* Tue May 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.5-1mdk
- 4.5

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.4-1mdk
- 4.4

* Sat Apr 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.3-1mdk
- 4.3

* Mon Mar 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.8-1mdk
- 3.8

* Mon Mar 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.7-1mdk
- 3.7

* Fri Feb 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.5-1mdk
- 3.5

* Mon Feb 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.4-1mdk
- 3.4

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.3-1mdk
- 3.3
- spec cleanup

* Fri Dec 24 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.9-2mdk
- q(Birthday rebuild) && perl->new() and "COIN";
- remove MANIFEST file from %%doc

