#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Convert-Bencode_XS
Version  : 0.06
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/I/IW/IWADE/Convert-Bencode_XS-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IW/IWADE/Convert-Bencode_XS-0.06.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Convert-Bencode_XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Convert-Bencode_XS version 0.06
===============================
This module provide fast conversion functions to/from the Bencode format.
This format is described at http://bitconjurer.org/BitTorrent/protocol.html

%package dev
Summary: dev components for the perl-Convert-Bencode_XS package.
Group: Development
Provides: perl-Convert-Bencode_XS-devel = %{version}-%{release}
Requires: perl-Convert-Bencode_XS = %{version}-%{release}

%description dev
dev components for the perl-Convert-Bencode_XS package.


%package perl
Summary: perl components for the perl-Convert-Bencode_XS package.
Group: Default
Requires: perl-Convert-Bencode_XS = %{version}-%{release}

%description perl
perl components for the perl-Convert-Bencode_XS package.


%prep
%setup -q -n Convert-Bencode_XS-0.06
cd %{_builddir}/Convert-Bencode_XS-0.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Convert::Bencode_XS.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Convert/Bencode_XS.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Convert/Bencode_XS/Bencode_XS.so
