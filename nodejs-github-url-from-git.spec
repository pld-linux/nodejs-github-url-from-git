%define		pkg	github-url-from-git
Summary:	Parse a github git url and return the github repo url
Name:		nodejs-%{pkg}
Version:	1.3.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	c2113bcbd29428b7ee4497106e6439da
URL:		https://github.com/visionmedia/node-github-url-from-git
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse a github git url and return the github repo url.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md LICENSE
%{nodejs_libdir}/%{pkg}
