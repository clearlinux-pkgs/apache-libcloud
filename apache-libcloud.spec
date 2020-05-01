#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2C0754B2CE0692F3 (tomaz@tomaz.me)
#
Name     : apache-libcloud
Version  : 3.0.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/15/f0/dcb99cba726642d38884973efdfe7071ccc06919fac034a8925bb4e0c16f/apache-libcloud-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/f0/dcb99cba726642d38884973efdfe7071ccc06919fac034a8925bb4e0c16f/apache-libcloud-3.0.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/15/f0/dcb99cba726642d38884973efdfe7071ccc06919fac034a8925bb4e0c16f/apache-libcloud-3.0.0.tar.gz.asc
Summary  : A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see https://libcloud.apache.org
Group    : Development/Tools
License  : Apache-2.0
Requires: apache-libcloud-license = %{version}-%{release}
Requires: apache-libcloud-python = %{version}-%{release}
Requires: apache-libcloud-python3 = %{version}-%{release}
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : requests
BuildRequires : tox
BuildRequires : virtualenv

%description
====================================================
        
        
        Apache Libcloud is a Python library which hides differences between different
        cloud provider APIs and allows you to manage different cloud resources
        through a unified and easy to use API.

%package license
Summary: license components for the apache-libcloud package.
Group: Default

%description license
license components for the apache-libcloud package.


%package python
Summary: python components for the apache-libcloud package.
Group: Default
Requires: apache-libcloud-python3 = %{version}-%{release}

%description python
python components for the apache-libcloud package.


%package python3
Summary: python3 components for the apache-libcloud package.
Group: Default
Requires: python3-core
Provides: pypi(apache_libcloud)
Requires: pypi(requests)

%description python3
python3 components for the apache-libcloud package.


%prep
%setup -q -n apache-libcloud-3.0.0
cd %{_builddir}/apache-libcloud-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588302844
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/apache-libcloud
cp %{_builddir}/apache-libcloud-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/apache-libcloud/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/apache-libcloud-3.0.0/NOTICE %{buildroot}/usr/share/package-licenses/apache-libcloud/904397a41ddf409c9cf5be84010b5edb585fb34f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apache-libcloud/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/apache-libcloud/904397a41ddf409c9cf5be84010b5edb585fb34f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
