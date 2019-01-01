%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kfloppy
Summary:	kfloppy
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	871e311af9984f77bf82a9a1067f29cf
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcompletion-devel >= 5.44.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.44.0
BuildRequires:	kf5-kcrash-devel >= 5.53.0
BuildRequires:	kf5-kdoctools-devel >= 5.44.0
BuildRequires:	kf5-ki18n-devel >= 5.44.0
BuildRequires:	kf5-kxmlgui-devel >= 5.44.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KFloppy is a utility that provides a straightforward graphical means
to format 3.5" and 5.25" floppy disks.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kfloppy.categories
%attr(755,root,root) %{_bindir}/kfloppy
%{_desktopdir}/org.kde.kfloppy.desktop
%{_iconsdir}/hicolor/128x128/apps/kfloppy.png
%{_iconsdir}/hicolor/16x16/apps/kfloppy.png
%{_iconsdir}/hicolor/22x22/apps/kfloppy.png
%{_iconsdir}/hicolor/32x32/apps/kfloppy.png
%{_iconsdir}/hicolor/48x48/apps/kfloppy.png
%{_iconsdir}/hicolor/64x64/apps/kfloppy.png
%{_datadir}/metainfo/org.kde.kfloppy.appdata.xml
