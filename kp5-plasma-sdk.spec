# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.11.2
%define		qtver		5.3.2
%define		kpname		plasma-sdk

Summary:	KDE Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.11.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	52cec92f017090e8d75e1f6948224854
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-kactivities-stats-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpeople-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Desktop.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cuttlefish
%attr(755,root,root) %{_bindir}/lookandfeelexplorer
%attr(755,root,root) %{_bindir}/plasmaengineexplorer
%attr(755,root,root) %{_bindir}/plasmathemeexplorer
%attr(755,root,root) %{_bindir}/plasmoidviewer
%dir %{_libdir}/qt5/plugins/ktexteditor
%{_libdir}/qt5/plugins/ktexteditor/cuttlefishplugin.so
%{_desktopdir}/org.kde.cuttlefish.desktop
%{_desktopdir}/org.kde.plasma.lookandfeelexplorer.desktop
%{_desktopdir}/org.kde.plasma.themeexplorer.desktop
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/FormField.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/FormLabel.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/MetadataEditor.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/main.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/metadata.desktop
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/metadata.json
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/code
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/code/openInEditor.sh
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/data
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/data/themeDescription.json
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/data/todo
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/ColorButton.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/ColorEditor.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/FormLabel.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/MetadataEditor.qml
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/Hand.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/actionbutton.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/allframesvgs.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/analog_meter.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/busyindicator.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/button.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/checkmarks.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/clock.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/containment-controls.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/dialog.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/framesvg.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/icons.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/listitem.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/monitor.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/panel.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/progressbar.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/scrollbar.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/slider.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/tabbar.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/delegates/textfield.qml
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/fakecontrols
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/fakecontrols/Button.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/fakecontrols/CheckBox.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/fakecontrols/LineEdit.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/contents/ui/main.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/metadata.desktop
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/metadata.json
%{_datadir}/kservices5/plasma-package-org.kde.plasma.cuttlefish.desktop
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.plasmoidviewershell.desktop
%{_mandir}/man1/plasmaengineexplorer.1*
%{_mandir}/man1/plasmoidviewer.1*
%{_datadir}/metainfo/org.kde.cuttlefish.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.cuttlefish.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.lookandfeelexplorer.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.plasmoidviewershell.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.themeexplorer.appdata.xml
%dir %{_datadir}/plasma/packages/org.kde.plasma.cuttlefish
%dir %{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents
%dir %{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents/ui
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/IconGrid.qml
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/IconGridDelegate.qml
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/Preview.qml
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/SvgGrid.qml
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/Tools.qml
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/contents/ui/cuttlefish.qml
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/metadata.desktop
%{_datadir}/plasma/packages/org.kde.plasma.cuttlefish/metadata.json
%dir %{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell
%dir %{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents
%dir %{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/applet
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/applet/AppletError.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/applet/CompactApplet.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/applet/DefaultCompactRepresentation.qml
%dir %{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/AppletConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigCategoryDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationContainmentActions.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationContainmentAppearance.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationKcmPage.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ConfigurationShortcuts.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/ContainmentConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/MouseEventInputButton.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/configuration/PanelConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/defaults
%dir %{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/Background.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/Desktop.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/Konsole.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/contents/views/SdkButtons.qml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/metadata.desktop
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/metadata.json
