# Run tests in check section
%bcond_without check

%global goipath         gopkg.in/readline.v1
%global forgeurl        https://github.com/chzyer/readline
%global oldgoipath      github.com/chzyer/readline
%global oldgoname       %gorpmname %{oldgoipath}
%global commit          2972be24d48e78746da79ba8e24e8b488c9880de

%global common_description %{expand:
Pure golang implementation for GNU-Readline kind library.}

%gometa

Name:    %{goname}
Version: 1.4
Release: 6%{?dist}
Summary: Pure golang implementation for GNU-Readline kind library
License: MIT and WTFPL
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(golang.org/x/sys/unix)

%if %{with check}
BuildRequires: golang(github.com/chzyer/test)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-gopkg-readline-devel = %{version}-%{release}
Obsoletes: golang-gopkg-readline-devel < 1.4-3
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%package -n compat-%{oldgoname}-devel
Summary:    %{summary}
BuildArch:  noarch
 
%description -n compat-%{oldgoname}-devel
%{common_description}
 
This package contains compatibility glue for code that still imports the
%{oldgoipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall

install -m 0755 -vd %{buildroot}%{gopath}/src/%(dirname %{oldgoipath})
ln -s %{gopath}/src/%{goipath} %{buildroot}%{gopath}/src/%{oldgoipath}


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md example


%files -n compat-%{oldgoname}-devel
%dir %{gopath}/src/%(dirname %{oldgoipath})
%{gopath}/src/%{oldgoipath}


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6.git2972be2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-5.20180628git2972be2
- Bump to commit 2972be24d48e78746da79ba8e24e8b488c9880de

* Mon Apr 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-4.20180409gitf6d7a1f
- Upstream GIT revision f6d7a1f

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-3
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-1
- First package for Fedora

