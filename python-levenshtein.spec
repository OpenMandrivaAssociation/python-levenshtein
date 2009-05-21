%define oname python-Levenshtein
%define version 0.10.1
%define release %mkrel 1

Summary: Levenshtein Python extension and C library
Name: python-levenshtein
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/translate/%{oname}-%{version}.tar.bz2
# nedded to build the html documentation
Source1: genextdoc.py
License: GPLv2+
Group: Development/Python
Url: http://translate.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides: %{oname} = %{version}-%{release}
%py_requires -d

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
%doc MANIFEST NEWS COPYING README Levenshtein.html
%{python_sitearch}/*.so
%{python_sitearch}/*.egg-info

