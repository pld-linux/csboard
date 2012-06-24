Summary:	CSBoard is a small GUI for gnuchess
Summary(pl):	CSBoard jest ma�ym frontendem do gnuchess
Name:		csboard
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/csboard/%{name}-%{version}.tar.gz
# Source0-md5:	2c02bca491192be19273266781b6f18b
Source1:	%{name}.desktop
Patch0:		%{name}-mono.patch
URL:		http://csboard.berlios.de/
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	scrollkeeper
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSBoard is a small GUI for gnuchess. It is written in C# and uses mono
and gtk-sharp. It is simple, but allows you just play chess with SVG
graphics and native look and desktop theme usage.

CSBoard use gnuchess as playing engine, but you can also play with
crafty of phalanx.

%description -l pl
CSBoard jest ma�ym frontendem do gnuchess. Zosta� napisany w j�zyku C#
i wykorzystuje mono i bibliotek� gtk-sharp. Jest prosty, ale pozwala
na gr� w szachy wykorzystuj�c grafik� wektorow� SVG,

%prep
%setup -q
%patch0 -p0

%build
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -f data/csboard.png  $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install csboard.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%preun
%gconf_schema_uninstall csboard.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csboard
%dir %{_datadir}/csboard
%dir %{_datadir}/csboard/images
%dir %{_datadir}/csboard/resource
%{_datadir}/csboard/csboard.exe
%{_datadir}/csboard/images/*
%{_datadir}/csboard/resource/*
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/csboard.schemas
