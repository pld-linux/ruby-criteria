%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Criteria abstract queries
Summary(pl):	Criteria - abstrakcyjne zapytania
Name:		ruby-Criteria
Version:	1.1a
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://mephle.org/Criteria/criteria-%{version}.tar.gz
# Source0-md5:	a39482fdf7bae7639791444dfb4d91ce
URL:		http://www.mephle.org/Criteria/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Criteria is a module for abstracting queries to various data sets. For
instance, you might have a flat text file, or an array of Ruby
objects, or a SQL database, and wish to perform the same query on any
given source, without different versions of code for each.

%description -l pl
Criteria to modu³ do abstrakcyjnych zapytañ na ró¿nych typach danych.
Na przyk³ad, mo¿na mieæ p³aski plik tekstowy lub tablicê obiektów w
Rubym, albo bazê SQL, i chcieæ wykonaæ to samo zapytanie na dowolnym
¼ródle, bez tworzenia ró¿nych wersji kodu dla ka¿dego z nich.

%prep
%setup -q -n criteria-%{version}

%build
ruby install.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

rdoc -o rdoc --main README.en lib
rdoc --ri -o ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/criteria
%{ruby_rubylibdir}/criteria.rb
%{ruby_ridir}/*
