Summary:	Criteria abstract queries
Summary(pl.UTF-8):	Criteria - abstrakcyjne zapytania
Name:		ruby-Criteria
Version:	1.1a
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	http://mephle.org/Criteria/criteria-%{version}.tar.gz
# Source0-md5:	a39482fdf7bae7639791444dfb4d91ce
URL:		http://www.mephle.org/Criteria/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Criteria is a module for abstracting queries to various data sets. For
instance, you might have a flat text file, or an array of Ruby
objects, or a SQL database, and wish to perform the same query on any
given source, without different versions of code for each.

%description -l pl.UTF-8
Criteria to moduł do abstrakcyjnych zapytań na różnych typach danych.
Na przykład, można mieć płaski plik tekstowy lub tablicę obiektów w
Rubym, albo bazę SQL, i chcieć wykonać to samo zapytanie na dowolnym
źródle, bez tworzenia różnych wersji kodu dla każdego z nich.

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

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/criteria
%{ruby_rubylibdir}/criteria.rb
%{ruby_ridir}/*
