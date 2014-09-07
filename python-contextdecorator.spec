%if 0%{?fedora}
%global _with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-contextdecorator
Version:        0.10.0
Release:        2%{?dist}
Summary:        Create APIs that work as decorators and as context managers

Group:          Development/Languages
License:        BSD
URL:            https://code.google.com/p/contextdecorator
# https://pypi.python.org/packages/source/c/contextdecorator/contextdecorator-0.10.0.tar.gz#md5=779973c0e9502c9fdc7add9628cbb58d
Source0:        https://pypi.python.org/packages/source/c/contextdecorator/contextdecorator-%{version}.tar.gz
Patch0:         contextdec-lic.patch

BuildRequires:  python2-devel python-setuptools
BuildArch:      noarch

%description
Create APIs that work as decorators and as context managers.
If you're a library or framework creator then it is nice to be
able to create APIs that can be used either as decorators or 
context managers.

%if 0%{?_with_python3}
%package -n python3-contextdecorator
Summary: Create APIs that work as decorators and as context managers
BuildRequires:  python3-devel python3-setuptools

%description -n python3-contextdecorator
Create APIs that work as decorators and as context managers.
If you're a library or framework creator then it is nice to be
able to create APIs that can be used either as decorators or 
context managers.
%endif


%prep
%setup -q -n contextdecorator-%{version}
%patch0 -p1
%if 0%{?_with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3


%build
%if 0%{?_with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif
%{__python2} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%if 0%{?_with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd
%endif

%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt LICENSE
%{python_sitelib}/*

%if 0%{?_with_python3}
%files -n python3-contextdecorator
%doc README.txt LICENSE
%{python3_sitelib}/*
%endif


%changelog
* Sun Sep 7 2014 Micharl Rice <michael@michaelrice.org> - 0.10.0-2
- Added license patch

* Mon Sep 1 2014 Michael Rice <michael@michaelrice.org> - 0.10.0-1
- Initial RPM build
