#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.27.8
%define		qtver		5.15.2
%define		kpname		plasma-sdk

Summary:	KDE Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.27.8
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	df67cf714baa309699886a5a7a66659d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
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
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Applications useful for Plasma Development.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%{_desktopdir}/org.kde.plasma.lookandfeelexplorer.desktop
%{_desktopdir}/org.kde.plasma.themeexplorer.desktop
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/contents/ui/FormField.qml

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
%{_mandir}/man1/plasmaengineexplorer.1*
%{_mandir}/man1/plasmoidviewer.1*
%{_datadir}/metainfo/org.kde.plasma.cuttlefish.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.lookandfeelexplorer.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.plasmoidviewershell.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.themeexplorer.appdata.xml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell
%{_desktopdir}/org.kde.plasmaengineexplorer.desktop
%{_desktopdir}/org.kde.plasmoidviewer.desktop
%{_datadir}/metainfo/org.kde.plasmaengineexplorer.appdata.xml
%{_datadir}/metainfo/org.kde.plasmoidviewer.appdata.xml
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.plasmoidviewershell.desktop
%{_desktopdir}/org.kde.plasma.cuttlefish.desktop

%lang(ca) %{_mandir}/ca/man1/plasmaengineexplorer.1*
%lang(ca) %{_mandir}/ca/man1/plasmoidviewer.1*
%lang(de) %{_mandir}/de/man1/plasmaengineexplorer.1*
%lang(de) %{_mandir}/de/man1/plasmoidviewer.1*
%lang(el) %{_mandir}/el/man1/plasmaengineexplorer.1*
%lang(el) %{_mandir}/el/man1/plasmoidviewer.1*
%lang(es) %{_mandir}/es/man1/plasmaengineexplorer.1*
%lang(es) %{_mandir}/es/man1/plasmoidviewer.1*
%lang(et) %{_mandir}/et/man1/plasmaengineexplorer.1*
%lang(et) %{_mandir}/et/man1/plasmoidviewer.1*
%lang(fr) %{_mandir}/fr/man1/plasmaengineexplorer.1*
%lang(fr) %{_mandir}/fr/man1/plasmoidviewer.1*
%lang(id) %{_mandir}/id/man1/plasmaengineexplorer.1*
%lang(id) %{_mandir}/id/man1/plasmoidviewer.1*
%lang(it) %{_mandir}/it/man1/plasmaengineexplorer.1*
%lang(it) %{_mandir}/it/man1/plasmoidviewer.1*
%lang(nl) %{_mandir}/nl/man1/plasmaengineexplorer.1*
%lang(nl) %{_mandir}/nl/man1/plasmoidviewer.1*
%lang(pt) %{_mandir}/pt/man1/plasmaengineexplorer.1*
%lang(pt) %{_mandir}/pt/man1/plasmoidviewer.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/plasmaengineexplorer.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/plasmoidviewer.1*
%lang(ru) %{_mandir}/ru/man1/plasmaengineexplorer.1*
%lang(ru) %{_mandir}/ru/man1/plasmoidviewer.1*
#%lang(sv) %{_mandir}/sv/man1/plasmaengineexplorer.1*
#%lang(sv) %{_mandir}/sv/man1/plasmoidviewer.1*
%lang(tr) %{_mandir}/tr/man1/plasmaengineexplorer.1*
%lang(tr) %{_mandir}/tr/man1/plasmoidviewer.1*
%lang(uk) %{_mandir}/uk/man1/plasmaengineexplorer.1*
%lang(uk) %{_mandir}/uk/man1/plasmoidviewer.1*
%{zsh_compdir}/_plasmoidviewer
