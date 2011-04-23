%define upstream_name    Module-Install-CheckLib
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A Module::Install extension to check that a library is available
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Devel::CheckLib)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


