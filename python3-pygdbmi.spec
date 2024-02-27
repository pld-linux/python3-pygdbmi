%define		module	pygdbmi
Summary:	pygdbmi
Summary(pl.UTF-8):	pygdbmi
Name:		python3-%{module}
Version:	0.11.0.0
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download:	https://pypi.org/simple/pygdbmi/
Source0:	https://files.pythonhosted.org/packages/source/p/pygdbmi/%{module}-%{version}.tar.gz
# Source0-md5:	34b1812e77469c6206002b3929798cab
URL:		https://pypi.org/project/pygdbmi/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pygdbmi - Get Structured Output from GDB's Machine Interface

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/py.typed
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
