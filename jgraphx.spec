%define real_ver %( echo %{version} | tr . _)

Summary:	Java-based Diagram Component and Editor
Name:		jgraphx
Version:	1.3.1.5
Release:	%mkrel 1
License:	BSD
Group:		Development/Java
URL:		http://www.jgraph.com/
Source0:	http://www.jgraph.com/downloads/jgraphx/archive/%{name}-%{real_ver}.zip
BuildRequires:	ant >= 0:1.6
BuildRequires:	java-rpmbuild
BuildRequires:	jpackage-utils >= 0:1.6
Requires:	jpackage-utils
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Jgraphx is the a lightweight and feature-rich graph component for Java,
and the successor to jgraph. It provides automatic 2D layout and routing
for diagrams. Object and relations can be displayed in any Swing UI
via provided scalable component.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
%{summary}.

%prep
%setup -q -c

mv %{name}/* .

# remove all binary libs
find -type f -name "*.jar" | xargs -t rm

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%ant -Dbuild.sysclasspath=only

# Remove copies of source so that we don't confuse
# the debuginfo finder
rm -rf build/src dist/%{name}-%{version}-src

%install
rm -rf %{buildroot}

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p lib/jgraphx.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd  %{buildroot}%{_javadir} 
    #create symlink
    ln -s %{name}-%{version}.jar %{name}.jar
    #indexing
    jar -i %{name}-%{version}.jar
popd

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# maven
%add_to_maven_depmap com.mxgraph %{name} %{version} JPP %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc license.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%config(noreplace) %{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(-,root,root)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
