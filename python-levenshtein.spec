%define oname python-Levenshtein

Summary:	Levenshtein Python extension and C library
Name:		python-levenshtein
Version:	0.12.0
Release:	1
License:	GPLv2+
Group:		Development/Python
Url:            http://github.com/ztane/python-Levenshtein
Source0:        https://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
# nedded to build the html documentation
Source1:	genextdoc.py
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
Provides:	%{oname} = %{version}-%{release}

%description
The Levenshtein Python C extension module contains functions for fast
computation of
- Levenshtein (edit) distance, and edit operations
- string similarity
- approximate median strings, and generally string averaging
- string sequence and set similarity
It supports both normal and Unicode strings.


%prep
%autosetup -n %{oname}-%{version} -p1

rm -rf python_Levenshtein.egg-info

%build
%py_build

%install
%py_install

# https://github.com/ztane/python-Levenshtein/issues/20
rm -f %{buildroot}/%{python_sitearch}/Levenshtein/_levenshtein.c
rm -f %{buildroot}/%{python_sitearch}/Levenshtein/_levenshtein.h
# https://github.com/ztane/python-Levenshtein/issues/21
rm -f %{buildroot}/%{python_sitearch}/Levenshtein/StringMatcher.py
rm -f %{buildroot}/%{python_sitearch}/Levenshtein/__pycache__/StringMatcher.*

%files
%doc README.rst HISTORY.txt
%doc docs/Levenshtein.html
%doc Levenshtein/StringMatcher.py
%{python_sitearch}/*
