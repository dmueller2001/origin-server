%if 0%{?fedora}%{?rhel} <= 6
    %global scl ruby193
    %global scl_prefix ruby193-
    %global vendor_ruby /opt/rh/%{scl}/root/usr/share/ruby/vendor_ruby/
    %global mco_agent_root /opt/rh/%{scl}/root/usr/libexec/mcollective/mcollective/agent/
%else
    %global vendor_ruby /usr/share/ruby/vendor_ruby/
    %global mco_agent_root /usr/libexec/mcollective/mcollective/agent/
%endif

Summary:       M-Collective agent file for openshift-origin-msg-node-mcollective
Name:          openshift-origin-msg-node-mcollective
Version: 1.8.0
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      %{?scl:%scl_prefix}rubygems
Requires:      %{?scl:%scl_prefix}rubygem-open4
Requires:      %{?scl:%scl_prefix}rubygem-json
Requires:      rubygem-openshift-origin-node
Requires:      mcollective
Requires:      %{?scl:%scl_prefix}facter
Requires:      openshift-origin-msg-common
BuildArch:     noarch

%description
mcollective communication plugin

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{mco_agent_root}
mkdir -p %{buildroot}%{vendor_ruby}facter
mkdir -p %{buildroot}/etc/cron.minutely
mkdir -p %{buildroot}/usr/libexec/mcollective

cp -p src/openshift.rb %{buildroot}%{mco_agent_root}
cp -p facts/openshift_facts.rb %{buildroot}%{vendor_ruby}facter/
cp -p facts/openshift-facts %{buildroot}/etc/cron.minutely/
cp -p facts/update_yaml.rb %{buildroot}/usr/libexec/mcollective/

%files
%{mco_agent_root}openshift.rb
%{vendor_ruby}facter/openshift_facts.rb
%attr(0700,-,-) /usr/libexec/mcollective/update_yaml.rb
%attr(0700,-,-) %config(noreplace) /etc/cron.minutely/openshift-facts

%changelog
* Tue Apr 16 2013 Troy Dawson <tdawson@redhat.com> 1.7.4-1
- Bug 952408 - Node filters threaddump calls (jhonce@redhat.com)

* Wed Apr 10 2013 Adam Miller <admiller@redhat.com> 1.7.3-1
- Delete move/pre-move/post-move hooks, these hooks are no longer needed.
  (rpenta@redhat.com)
- Adding checks for ssh key matches (abhgupta@redhat.com)

* Mon Apr 08 2013 Adam Miller <admiller@redhat.com> 1.7.2-1
- WIP Cartridge Refactor - Support V1 contract for CLIENT_ERROR
  (jhonce@redhat.com)
- fixing rebase (tdawson@redhat.com)

* Thu Mar 28 2013 Adam Miller <admiller@redhat.com> 1.7.1-1
- bump_minor_versions for sprint 26 (admiller@redhat.com)
- WIP Cartridge Refactor - more robust oo-admin-cartridge (jhonce@redhat.com)

* Wed Mar 27 2013 Adam Miller <admiller@redhat.com> 1.6.4-1
- WIP Cartridge Refactor - Roll out old threaddump support (jhonce@redhat.com)
- WIP Cartridge Refactor - Add PHP support for threaddump (jhonce@redhat.com)

* Mon Mar 18 2013 Adam Miller <admiller@redhat.com> 1.6.3-1
- Add SNI upload support to API (lnader@redhat.com)

* Thu Mar 14 2013 Adam Miller <admiller@redhat.com> 1.6.2-1
- Replacing get_value() with config['param'] style calls for new version of
  parseconfig gem. (kraman@gmail.com)
- Merge pull request #1625 from tdawson/tdawson/remove-obsoletes
  (dmcphers+openshiftbot@redhat.com)
- Merge pull request #1629 from jwhonce/wip/cartridge_repository
  (dmcphers+openshiftbot@redhat.com)
- WIP Cartridge Refactor - Cartridge Repository (jhonce@redhat.com)
- Revert "Merge pull request #1622 from jwhonce/wip/cartridge_repository"
  (dmcphers@redhat.com)
- remove old obsoletes (tdawson@redhat.com)
- WIP Cartridge Refactor - Cartridge Repository (jhonce@redhat.com)
- Revert "Merge pull request #1604 from jwhonce/wip/cartridge_repository"
  (dmcphers@redhat.com)
- Adding the ability to fetch all gears with broker auth tokens
  (bleanhar@redhat.com)
- WIP Cartridge Refactor - Cartridge Repository (jhonce@redhat.com)

* Thu Mar 07 2013 Adam Miller <admiller@redhat.com> 1.6.1-1
- bump_minor_versions for sprint 25 (admiller@redhat.com)

* Wed Mar 06 2013 Adam Miller <admiller@redhat.com> 1.5.10-1
- Bug 918480 (dmcphers@redhat.com)
- Bug 917990 - Multiple fixes. (rmillner@redhat.com)

* Tue Mar 05 2013 Adam Miller <admiller@redhat.com> 1.5.9-1
- Bug 916918 - Couple of issues with frontend calls. (rmillner@redhat.com)

* Fri Mar 01 2013 Adam Miller <admiller@redhat.com> 1.5.8-1
- Bug 916918 - Add frontend calls to allowed actions. (rmillner@redhat.com)

* Thu Feb 28 2013 Adam Miller <admiller@redhat.com> 1.5.7-1
- reverted US2448 (lnader@redhat.com)

* Wed Feb 27 2013 Adam Miller <admiller@redhat.com> 1.5.6-1
- US2448 (lnader@redhat.com)

* Tue Feb 26 2013 Adam Miller <admiller@redhat.com> 1.5.5-1
- Bug 913351 - Cannot create application successfully when district is added
  (jhonce@redhat.com)

* Wed Feb 20 2013 Adam Miller <admiller@redhat.com> 1.5.4-1
- Bug 912899 - mcollective changing all numeric mongoid to BigInt
  (jhonce@redhat.com)

* Tue Feb 19 2013 Adam Miller <admiller@redhat.com> 1.5.3-1
- Commands and mcollective calls for each FrontendHttpServer API.
  (rmillner@redhat.com)
- Bug 912292: Return namespace update output on reply (ironcladlou@gmail.com)
- Switch from VirtualHosts to mod_rewrite based routing to support high
  density. (rmillner@redhat.com)
- Bug 842991 - Do not replace /etc/cron.minutely/openshift-facts when
  installing new rpm. (jhonce@redhat.com)
- Fix mcollective plugin rubygem dependency (john@ibiblio.org)
- Fixes for ruby193 (john@ibiblio.org)
- Audit oo_* return value in agent (pmorie@gmail.com)
- Return output from oo_status in agent (pmorie@gmail.com)
- Return connector execution output on the MCol reply (ironcladlou@gmail.com)
- Refactor agent and proxy, move all v1 code to v1 model
  (ironcladlou@gmail.com)
- WIP Cartridge Refactor (jhonce@redhat.com)
- WIP Cartridge Refactor (jhonce@redhat.com)

* Fri Feb 08 2013 Adam Miller <admiller@redhat.com> 1.5.2-1
- change %%define to %%global (tdawson@redhat.com)

* Thu Feb 07 2013 Adam Miller <admiller@redhat.com> 1.5.1-1
- bump_minor_versions for sprint 24 (admiller@redhat.com)

* Thu Jan 31 2013 Adam Miller <admiller@redhat.com> 1.4.3-1
- Merge pull request #1255 from sosiouxme/newfacts
  (dmcphers+openshiftbot@redhat.com)
- <facter,resource_limits> active_capacity/max_active_apps/etc switched to
  gear-based accounting (lmeyer@redhat.com)
- Merge pull request #1238 from sosiouxme/newfacts
  (dmcphers+openshiftbot@redhat.com)
- <facter,resource_limits> reckon by gears (as opposed to git repos), add gear
  status facts (lmeyer@redhat.com)
- <facter> some code cleanup - no functional change (lmeyer@redhat.com)

* Tue Jan 29 2013 Adam Miller <admiller@redhat.com> 1.4.2-1
- Reduce logging noise in MCollective agent (ironcladlou@gmail.com)
- Switch calling convention to match US3143 (rmillner@redhat.com)

* Wed Jan 23 2013 Adam Miller <admiller@redhat.com> 1.4.1-1
- bump_minor_versions for sprint 23 (admiller@redhat.com)

* Fri Jan 18 2013 Dan McPherson <dmcphers@redhat.com> 1.3.3-1
- SSL support for custom domains. (mpatel@redhat.com)
- Replace expose/show/conceal-port hooks with Endpoints (ironcladlou@gmail.com)

* Tue Dec 18 2012 Adam Miller <admiller@redhat.com> 1.3.2-1
- - oo-setup-broker fixes:  - Open dns ports for access to DNS server from
  outside the VM   - Turn on SELinux booleans only if they are off (Speeds up
  re-install)   - Added console SELinux booleans - oo-setup-node fixes:  -
  Setup mcollective to use broker IPs - Updates abstract cartridges to set
  proper order for php-5.4 and postgres-9.1 cartridges - Updated broker to add
  fedora 17 cartridges - Fixed facts cron job (kraman@gmail.com)

* Wed Dec 12 2012 Adam Miller <admiller@redhat.com> 1.3.1-1
- bump_minor_versions for sprint 22 (admiller@redhat.com)

* Tue Dec 11 2012 Adam Miller <admiller@redhat.com> 1.2.5-1
- Merge pull request #1052 from rmillner/BZ877321 (openshift+bot@redhat.com)
- Add username to filter list. (rmillner@redhat.com)
- Hide the password in mcollective logs. (rmillner@redhat.com)

* Mon Dec 10 2012 Adam Miller <admiller@redhat.com> 1.2.4-1
- Proper host name validation. (rmillner@redhat.com)

* Tue Dec 04 2012 Adam Miller <admiller@redhat.com> 1.2.3-1
- Security - Fix the full path to restorecon it was causing errors in the logs
  (tkramer@redhat.com)
- more mco 2.2 changes (dmcphers@redhat.com)
- repacking for mco 2.2 (dmcphers@redhat.com)
- Refactor tidy into the node library (ironcladlou@gmail.com)
- Merge pull request #1002 from tdawson/tdawson/fed-update/msg-node-
  mcollective-1.1.4 (openshift+bot@redhat.com)
- Move add/remove alias to the node API. (rmillner@redhat.com)
- Removed spec clutter for building on rhel5 (tdawson@redhat.com)
- mco value passing cleanup (dmcphers@redhat.com)

* Thu Nov 29 2012 Adam Miller <admiller@redhat.com> 1.2.2-1
- add any validator for mco 2.2 (dmcphers@redhat.com)
- Various mcollective changes getting ready for 2.2 (dmcphers@redhat.com)
- Move force-stop into the the node library (ironcladlou@gmail.com)
- add backtraces to error conditions in agent (dmcphers@redhat.com)
- Changing same uid move to rsync (dmcphers@redhat.com)
- use /bin/env for cron (dmcphers@redhat.com)
- add oo-ruby (dmcphers@redhat.com)
- Add method to get the active gears (dmcphers@redhat.com)

* Sat Nov 17 2012 Adam Miller <admiller@redhat.com> 1.2.1-1
- bump_minor_versions for sprint 21 (admiller@redhat.com)

* Fri Nov 16 2012 Adam Miller <admiller@redhat.com> 1.1.3-1
- BZ 876942:Disable threading until we can explore proper concurrency
  management (rmillner@redhat.com)
- Only use scl if it's available (ironcladlou@gmail.com)

* Wed Nov 14 2012 Adam Miller <admiller@redhat.com> 1.1.2-1
- add config to gemspec (dmcphers@redhat.com)
- getting specs up to 1.9 sclized (dmcphers@redhat.com)

* Thu Nov 08 2012 Adam Miller <admiller@redhat.com> 1.1.1-1
- Bumping specs to at least 1.1 (dmcphers@redhat.com)

* Tue Oct 30 2012 Adam Miller <admiller@redhat.com> 1.0.1-1
- bumping specs to at least 1.0.0 (dmcphers@redhat.com)
