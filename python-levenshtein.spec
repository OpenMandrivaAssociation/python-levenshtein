%define oname python-Levenshtein

Summary:	Levenshtein Python extension and C library
Name:		python-levenshtein
Version:	0.11.2
Release:	5
License:	GPLv2+
Group:		Development/Python
Url:		http://translate.sourceforge.net/
Source0:	http://downloads.sourceforge.net/translate/%{oname}-%{version}.tar.gz
# nedded to build the html documentation
Source1:	genextdoc.py
BuildRequires:	pkgconfig(python3)
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
%setup -q -n %{oname}-%{version}
install %{SOURCE1} .

%build
%{__python} setup.py build build_ext -l m

%install
%{__python} setup.py install --root=%{buildroot}

PYTHONPATH=$PYTHONPATH:%{buildroot}%{python_sitearch} %__python genextdoc.py Levenshtein

%files
%doc MANIFEST.in NEWS COPYING README.rst
%doc StringMatcher.py Levenshtein.html
%{python_sitearch}/*.so
%{python_sitearch}/*.egg-info

