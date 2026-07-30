%define upstream_name    Module-Install-CheckLib
%define upstream_version 0.14
Name:		perl-%{upstream_name}
Version:	0.14
Release:	1

Summary:	A Module::Install extension to check that a library is available
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bingos/module-install-checklib
Source0:	https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-Install-CheckLib-0.14.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Devel::CheckLib)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Module::Install::CheckLib is a the Module::Install manpage extension that
integrates the Devel::CheckLib manpage so that CPAN authors may stipulate
which particular C library and its headers they want available and to exit
the 'Makefile.PL' gracefully if they aren't.

The author specifies which C libraries, etc, they want available. the
Devel::CheckLib manpage is copied to the 'inc/' directory along with the
the Module::Install manpage files.

On the module user side, the bundled 'inc/' the Devel::CheckLib manpage
determines whether the current environment is supported or not and will
exit accordingly.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

