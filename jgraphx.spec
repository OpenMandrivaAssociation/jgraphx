Name:           jgraphx
Version:        2.2.0.2
Epoch:		1
Release:        2
Summary:        Java Graph Drawing Component

Group:          Development/Java
License:        BSD
URL:            http://www.jgraph.com/jgraph.html
Source0:        http://www.jgraph.com/downloads/jgraphx/archive/%{name}-%(echo %{version} |sed 's/\./_/g').zip

BuildRequires:  ant
BuildRequires:  java-devel >= 1.6
BuildRequires:  jpackage-utils
Requires:       java >= 1.4
Requires:       jpackage-utils

BuildArch:      noarch

%description
JGraphX is the a powerful, easy-to-use and feature-rich graph drawing
component for Java. It is a rewrite of JGraph, also known as JGraph 6.


%package javadoc
Summary:        API Documentation for %{name}

Group:          Documentation
Requires:       jpackage-utils
Requires:       %{name} = %{EVRD}

%description javadoc
JavaDoc documentation for %{name}


%prep
%setup -q -n %{name}
find -name '*.jar' -delete
rm -rf docs/api


%build
ant


%install

# Code
install -d %{buildroot}%{_javadir}
install -p -m644 lib/%{name}.jar \
        %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}.jar

# API documentation
install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}


%files
%{_javadir}/*
%doc license.txt


%files javadoc
%{_javadocdir}/*


