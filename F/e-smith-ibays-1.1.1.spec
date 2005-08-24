Summary: e-smith server and gateway - ibays module
%define name e-smith-ibays
Name: %{name}
%define version 1.1.1
%define release 13
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-ibays-1.1.1-02.mitel_patch
Patch1: e-smith-ibays-1.1.1-03.mitel_patch
Patch2: e-smith-ibays-1.1.1-04.mitel_patch
Patch3: e-smith-ibays-1.1.1-06.mitel_patch
Patch4: e-smith-ibays-1.1.1-07.mitel_patch
Patch5: e-smith-ibays-1.1.1-08.mitel_patch
Patch6: e-smith-ibays-1.1.1-09.mitel_patch
Patch7: e-smith-ibays-1.1.1-10.mitel_patch
Patch8: e-smith-ibays-1.1.1-11.mitel_patch
Patch9: e-smith-ibays-1.1.1-12.mitel_patch
Patch10: e-smith-ibays-1.1.1-13.mitel_patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base >= 4.13.15-76
Requires: perl(CGI::FormMagick)
Conflicts: e-smith-apache < 0.1.1
BuildRequires: perl, perl(Test::Inline)
BuildRequires: e-smith-devtools >= 1.11.0-03
AutoReqProv: no


%description
e-smith server and gateway software - ibays module.

%changelog
* Wed Aug 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-13]
- Default plugin to none in esFM::ibay::create_ibay(). [SF: 1267897]

* Mon Aug 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-12]
- Fix missing "use esmith::util" in ibay plugin lib. [SF: 1265684]
- Don't display ibay Plugin choice if "none" is the only choice. [SF: 1263740]

* Fri Aug 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.1-11]
- Need to check $ibay->prop('type') not $ibay->type [SF: 1260237]

* Tue Aug  9 2005 Shad Lords <slords@mail.com>
- [1.1.1-10]
- Remove 90e-smithAccess10common (belongs in e-smith-apache)
- Move some ibay options to database

* Thu Aug  4 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.1-09]
- Syntactic fix to perl code from 1.1.1-08 change

* Thu Jul 28 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-08]
- Update all uses of deprecated esmith::config and db_ APIs.
- Rewrite ibay-delete action in shell.

* Wed Jan 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-07]
- Fix untaint RE. [charlieb MN00050161]
- Fix "will not stay shared" warnings in IbayPlugin/none.pm

* Thu Nov 11 2004 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-06]
- Untaint name before using in system(). [charlieb MN00050161]

* Fri Sep  3 2004 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-05]
- Updated requires with new perl dependencies. [msoulier MN00040240]
- Clean BuildRequires. [charlieb MN00043055]

* Fri Feb  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.1-04]
- Fixed two issues with previous change. [msoulier 7475]

* Fri Feb  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.1-03]
- Updating default repair method to set CGIs as executable if enabled.
  [msoulier 7475]

* Wed Nov 19 2003 Tony Clayton <apc@e-smith.com>
- [1.1.1-02]
- Fix processTemplate call in IbayPlugin::none [tonyc 9924]
- Merge ibay-conf-plugin into ibay-modify action [tonyc 9924]

* Wed Nov 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.1-01]
- Collecting patches.

* Wed Nov 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-02]
- Adding 6.0 styling to ibay panel. [msoulier 10415]
- Converted createlinks to new api.
- Add IbayPlugin stuff [tonyc 9924]
- Add dependency on perl-CGI-FormMagick >= 0.91-04 [tonyc 9924]

* Fri Sep  5 2003 Tony Clayton <apc@e-smith.com>
- [1.1.0-01]
- Changing version to development stream number - 1.1.0
- Rolling to development stream [tonyc 9924]

* Wed Aug 13 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.3-05]
- Fixed the content ibay showing up in the ibay list of the primary domain's
  virtual host block. [msoulier 9649]

* Wed Aug 13 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.3-04]
- Correcting the previous revision, and limiting ibay access as sub-urls to
  the primary domain only. [msoulier 9649]

* Wed Aug  6 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.3-03]
- Unify ibay handling, since 15PrimaryContent is now obsolete, and changing
  the primary domain's content was breaking access to ibays. [msoulier 9649]

* Wed Jul  2 2003 Charlie Brady <charlieb@e-smith.com>
- [1.0.3-02]
- Fix path of created starter website index file (don't rely on symlink
  which "should" point to correct place). [charlieb 9241]

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.3-01]
- Added order to migrate fragments [gordonr 9015]

* Wed Jun 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.2-04]
- Fixed Conflicts header - should be <, not <= [gordonr 8903]

* Wed Jun 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.2-03]
- Missing 'use esmith::util' [gordonr 8973]

* Tue Jun 10 2003 Charlie Brady <charlieb@e-smith.com>
- [1.0.2-02]
- Fix broken symlinks in post-{install,upgrade}. [charlieb 8973]

* Fri Jun  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.2-01]
- Shuffled some httpd.conf fragments from e-smith-apache [gordonr 8903]

* Tue May 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.0.1-01]
- Fix typo in createlinks script. Rolling version of package
  to correct build problem. [charlieb 8841]

* Tue May 27 2003 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-02]
- Add some code from init-accounts action which depends on
  /home/e-smith/files/ibays directory, which isn't included
  in base. New action is init-ibays. [charlieb 8841]

* Thu May  8 2003 Mark Knox <markk@e-smith.com>
- [1.0.0-01]
- Initial release. Split out from e-smith-base. [markk 8610]

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%pre
%post

%build
# Force creation of potentially empty directories
mkdir -p root/etc/e-smith/skel/ibay/{cgi-bin,files,html,.AppleDesktop}
mkdir -p root/etc/e-smith/skel/e-smith/files/ibays
mkdir -p root/etc/e-smith/web/{common,functions}
mkdir -p root/etc/e-smith/web/panels/manager/{cgi-bin,common,html}
mkdir -p root/home/e-smith/files/ibays

# symlink IbayPlugin perl lib directory to /etc/e-smith/IbayPlugin
ln -s /$(cd root; find usr -name IbayPlugin) root/etc/e-smith/IbayPlugin

LEXICONS=$(find root/etc/e-smith/web/functions \
	-type f | grep -v CVS | grep -v pleasewait)

for lexicon in $LEXICONS
do
    /sbin/e-smith/validate-lexicon $lexicon
done

/sbin/e-smith/generate-lexicons

perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
