#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	TabularDisplay
Summary:	Text::TabularDisplay - display text in formatted table output
Summary(pl.UTF-8):	Text::TabularDisplay - wypisywanie tekstu w postaci tabelki
Name:		perl-Text-TabularDisplay
Version:	1.28
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abb13449751ae40c01747a443f0420b4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::TabularDisplay simplifies displaying textual data in a table.
The output is identical to the columnar display of query results in
the mysql text monitor.

%description -l pl.UTF-8
Text::TabularDisplay upraszcza wyświetlanie danych tekstowych w
tabeli. Wyjście jest identyczne do kolumnowego wyświetlania wyników
zapytania w tekstowym monitorze mysql.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
