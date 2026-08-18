Name:		python-typeguard
Version:	4.6.0
Release:	1
Summary:	Run-time type checker for Python
License:	MIT
Group:		Development/Python
URL:		https://github.com/agronholm/typeguard
Source0:	https://files.pythonhosted.org/packages/source/t/typeguard/typeguard-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(typing-extensions)

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%description
Runtime type checking for PEP 484 annotations. Used by tyro (and
therefore Unsloth) to validate command-line and configuration objects.

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/typeguard
%{py_sitedir}/typeguard-*.*-info
