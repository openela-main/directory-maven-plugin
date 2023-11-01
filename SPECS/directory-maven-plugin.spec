Name:       directory-maven-plugin
Version:    0.3.1
Release:    2%{?dist}
Summary:    Establish locations for files in multi-module builds

License:    ASL 2.0
URL:        https://github.com/jdcasey/directory-maven-plugin

Source0:    https://github.com/jdcasey/directory-maven-plugin/archive/directory-maven-plugin-0.3.1.tar.gz

BuildArch:  noarch
ExclusiveArch: x86_64

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(junit:junit)

%description
The Directory Plugin for Maven is used to discover various project-related 
paths, such as the execution root directory, the directory for a specific 
project in the current build session, or the highest project base directory 
(closest to the filesystem root directory) available in the projects loaded 
from disk (not resolved from a remote repository). The plugin will then reflect
this value to the console, and also inject it into each project's properties 
using the value of the property plugin parameter.

%package javadoc
Summary:  Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%autosetup -n directory-maven-plugin-directory-maven-plugin-0.3.1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md

%changelog
* Thu Mar 04 2021 Alex Macdonald <almacdon@redhat.com> - 0.3.1-2
- Add ExclusiveArch: x86_64

* Mon Oct 15 2018 Salman Siddiqui <sasiddiq@redhat.com> - 0.3.1-1
- Initial packaging
