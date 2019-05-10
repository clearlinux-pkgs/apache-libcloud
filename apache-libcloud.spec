#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apache-libcloud
Version  : 2.4.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/b9/3e/adfe316292bd2f5ff2556ea09887515c09974483c3028ae39563734e145b/apache-libcloud-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/3e/adfe316292bd2f5ff2556ea09887515c09974483c3028ae39563734e145b/apache-libcloud-2.4.0.tar.gz
Summary  : A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see http://libcloud.apache.org
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
%setup -q -n apache-libcloud-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557450157
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
cp LICENSE %{buildroot}/usr/share/package-licenses/apache-libcloud/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apache-libcloud/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
