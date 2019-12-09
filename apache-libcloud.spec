#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2C0754B2CE0692F3 (tomaz@tomaz.me)
#
Name     : apache-libcloud
Version  : 2.7.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/d2/6f/e30813e7ab0d09e4be8544135ee18d7ff70ca61507c9831b7dcb1461c0d8/apache-libcloud-2.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d2/6f/e30813e7ab0d09e4be8544135ee18d7ff70ca61507c9831b7dcb1461c0d8/apache-libcloud-2.7.0.tar.gz
Source1 : https://files.pythonhosted.org/packages/d2/6f/e30813e7ab0d09e4be8544135ee18d7ff70ca61507c9831b7dcb1461c0d8/apache-libcloud-2.7.0.tar.gz.asc
Summary  : A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see http://libcloud.apache.org
Group    : Development/Tools
License  : Apache-2.0
Requires: apache-libcloud-license = %{version}-%{release}
Requires: apache-libcloud-python = %{version}-%{release}
Requires: apache-libcloud-python3 = %{version}-%{release}
Requires: requests
Requires: typing
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : requests
BuildRequires : tox
BuildRequires : typing
BuildRequires : virtualenv

%description
Apache Libcloud - a unified interface for the cloud
====================================================

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

%description python3
python3 components for the apache-libcloud package.


%prep
%setup -q -n apache-libcloud-2.7.0
cd %{_builddir}/apache-libcloud-2.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575930877
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/apache-libcloud
cp %{_builddir}/apache-libcloud-2.7.0/LICENSE %{buildroot}/usr/share/package-licenses/apache-libcloud/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/apache-libcloud-2.7.0/NOTICE %{buildroot}/usr/share/package-licenses/apache-libcloud/904397a41ddf409c9cf5be84010b5edb585fb34f
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
