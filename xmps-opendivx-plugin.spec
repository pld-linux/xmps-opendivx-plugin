Summary:	OpenDivX plugin for XMPS
Summary(pl):	Wtyczka OpenDivX dla odtwarzacza XMPS
Name:		xmps-opendivx-plugin
Version:	0.0.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.projectmayo.com/dnload/divx4linux/xmps/%{name}-%{version}.tar.gz
URL:		http://www.projectmayo.com/
Requires:	xmps
BuildRequires:	libdivxdecore-devel
BuildRequires:	xmps-devel >= 0.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	mawk
BuildRequires:	glib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
OpenDivX plugin for XMPS (X Multimedia Player System).

%description -l pl
Wtyczka OpenDivX dla odtwarzacza XMPS.

%prep
%setup  -q

%build
%{__libtoolize}
aclocal
%{__autoconf}
%configure \
	--enable-static=no
%{__make} CFLAGS="%{rpmcflags} $(glib-config --cflags)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmps/*/*/*.so
