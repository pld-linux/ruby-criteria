%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Criteria abstract queries
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
Criteria is a module for abstracting queries to various data sets.  For
instance, you might have a flat text file, or an array of Ruby objects, or a
SQL database, and wish to perform the same query on any given source, without
different versions of code for each.

%prep
%setup -q -n criteria-%{version}

%build
ruby install.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

rdoc -o rdoc/ --main README.en lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby install.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/criteria
%{ruby_rubylibdir}/criteria.rb
