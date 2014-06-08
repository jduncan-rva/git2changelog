Summary: To convert git logs into formatted changelog entries
Name: git2changelog
Version: 0.1
Release: 4%{dist}
Source0: http://people.redhat.com/jduncan/%{name}/%{name}-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Requires: python-dateutil
BuildRequires: python2-devel
BuildRequires: python-setuptools
Url: https://github.com/jduncan-rva/git2changelog

%description
git2changelog analyzes a git repository to create a formatted changelog

%prep
%setup -q -n %{name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --root=$RPM_BUILD_ROOT

%files
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/*
%{_mandir}/man8/%{name}.8*
%{python2_sitelib}/*egg-info
%{python2_sitelib}/%{name}*
%{_bindir}/%{name}

%changelog
* Sun Jun 08 2014 Jamie Duncan <jduncan@redhat.com> - 0.1-4
- 08c27e2 =refactored to handle condition where tag was at HEAD properly. fixes #4

* Sun Jun 08 2014 Jamie Duncan <jduncan@redhat.com> - 0.1-3
- 869cb42 =set default for repository to the cwd. fixes #2

* Sun Jun 08 2014 Jamie Duncan <jduncan@redhat.com> - 0.1-2
- d5f16db =typo. fixes #1

* Sun Jun 08 2014 Jamie Duncan <jduncan@redhat.com> 0.1-1
- initial buildout and testing build
