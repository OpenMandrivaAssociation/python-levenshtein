%global debug_package %nil
%define module levenshtein
%define oname Levenshtein

Name:		python-levenshtein
Version:	0.27.3
Release:	1
Summary:	Levenshtein Python extension and C library
License:	GPL-2.0-or-later
Group:		Development/Python
URL:		https://github.com/ztane/python-Levenshtein
Source0:	https://pypi.python.org/packages/source/l/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(rapidfuzz)
BuildRequires:	python%{pyver}dist(scikit-build-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(pytest)

Provides:	%{module} = %{version}-%{release}

%description
The Levenshtein Python C extension module contains functions for fast
computation of
- Levenshtein (edit) distance, and edit operations
- string similarity
- approximate median strings, and generally string averaging
- string sequence and set similarity
It supports both normal and Unicode strings.

%prep
%autosetup -n %{module}-%{version} -p1
# PEP639
#sed -i '/license = "GPL-2.0-or-later"/d' pyproject.toml

%build
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%py_install

%files
%doc README.md HISTORY.md
%license LICENSE
%{python_sitearch}/%{oname}
%{python_sitearch}/%{module}-%{version}.dist-info
