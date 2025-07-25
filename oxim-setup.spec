%define version      1.4.4
%define release      %mkrel 1

Summary:	OXIM setup tool
Name:		oxim-setup
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		System/Internationalization
URL:		https://opendesktop.org.tw/demopage/oxim/
Source0:	ftp://140.111.128.66/odp/OXIM/Source/%{name}-%{version}.tar.gz
Patch0:		oxim-setup-1.2.1-fix-str-fmt.patch
Patch1:		oxim-setup-1.4.1-drop-unused-libs.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  oxim-devel >= 1.2.1
BuildRequires:	gtk+2-devel
BuildRequires:  curl-devel
BuildRequires:	gettext-devel
Requires:	oxim >= 1.2.1
Conflicts:	oxim < 1.2.1

%description
OXIM Setup Tool.

%prep
%setup -q
%patch0 -p0
%patch1 -p0 -b .libs

%build
autoreconf -fi
%configure2_5x --disable-static \
	--enable-setup-gtk \
	--disable-setup-qt3 \
	--disable-setup-php \
	--disable-setup-gambas \
	--disable-qt-immodule
%make

%install
rm -fr %buildroot
%makeinstall_std

rm -fr %buildroot%_datadir/gettext

%find_lang %name

%post
%if %mdkversion < 200900
%update_menus
%endif

%postun
%if %mdkversion < 200900
%clean_menus
%endif

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/oxim-setup
%{_libdir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
