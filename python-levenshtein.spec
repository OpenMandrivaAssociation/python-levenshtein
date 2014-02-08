%define oname python-Levenshtein
%define version 0.10.1
%define subrel 1
%define release 4

Summary: Levenshtein Python extension and C library
Name: python-levenshtein
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/translate/%{oname}-%{version}.tar.bz2
# nedded to build the html documentation
Source1: genextdoc.py
Patch0: python-Levenshtein-0.10.1-mathlib.diff
License: GPLv2+
Group: Development/Python
Url: http://translate.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
Provides: %{oname} = %{version}-%{release}

%description
The Levenshtein Python C extension module contains functions for fast
computation of
- Levenshtein (edit) distance, and edit operations
- string similarity
- approximate median strings, and generally string averaging
- string sequence and set similarity
It supports both normal and Unicode strings.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
install %{SOURCE1} .

%build

%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

PYTHONPATH=$PYTHONPATH:%{buildroot}%{python_sitearch} ./gendoc.sh Levenshtein

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc MANIFEST NEWS COPYING README
%doc StringMatcher.py Levenshtein.html
%{python_sitearch}/*.so
%{python_sitearch}/*.egg-info



%changelog
* Tue Sep 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-2.1
- built for updates
- P0: fix build (-lm)

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.10.1-2mdv2011.0
+ Revision: 590603
- rebuild for python-2.7
- drop obsolete %%py_requires macro and add python-devel as BR

* Thu May 21 2009 Jérôme Brenier <incubusss@mandriva.org> 0.10.1-1mdv2010.0
+ Revision: 378552
- fix doc
- import python-levenshtein


