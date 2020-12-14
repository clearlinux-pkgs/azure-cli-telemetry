#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-cli-telemetry
Version  : 1.0.4
Release  : 8
URL      : https://files.pythonhosted.org/packages/70/1e/a6d38c76bfcdb82373c0ea22f74e018dc3a3124923a4d445e97c911e18a4/azure-cli-telemetry-1.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/70/1e/a6d38c76bfcdb82373c0ea22f74e018dc3a3124923a4d445e97c911e18a4/azure-cli-telemetry-1.0.4.tar.gz
Summary  : Microsoft Azure CLI Telemetry Package
Group    : Development/Tools
License  : MIT
Requires: azure-cli-telemetry-python = %{version}-%{release}
Requires: azure-cli-telemetry-python3 = %{version}-%{release}
Requires: applicationinsights
BuildRequires : applicationinsights
BuildRequires : buildreq-distutils3
BuildRequires : portalocker

%description
=====================================
        
        This is the Microsoft Azure CLI Telemetry package. It is not intended to be installed directly by the end user.

%package python
Summary: python components for the azure-cli-telemetry package.
Group: Default
Requires: azure-cli-telemetry-python3 = %{version}-%{release}

%description python
python components for the azure-cli-telemetry package.


%package python3
Summary: python3 components for the azure-cli-telemetry package.
Group: Default
Requires: python3-core
Provides: pypi(azure_cli_telemetry)
Requires: pypi(applicationinsights)
Requires: pypi(portalocker)

%description python3
python3 components for the azure-cli-telemetry package.


%prep
%setup -q -n azure-cli-telemetry-1.0.4
cd %{_builddir}/azure-cli-telemetry-1.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607973010
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/cli/__pycache__/__init__.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/cli/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
