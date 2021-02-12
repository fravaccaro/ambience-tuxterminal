Name:          ambience-tuxterminal
Version:       0.1
Release:       1
Summary:       Tux and vintage-themed ambience
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
If you spent sleepless nights discovering and fiddling with Linux this ambience is for you!

%files

%defattr(-,root,root,-)
/usr/share/ambience/*

%post
chmod 755 /usr/share/ambience/{name}
chmod 755 /usr/share/ambience/{name}/images
chmod 755 /usr/share/ambience/{name}/sounds
chmod 644 /usr/share/ambience/{name}/*.*
chmod 644 /usr/share/ambience/{name}/images/*.*
chmod 644 /usr/share/ambience/{name}/sounds/*.*
systemctl-user restart ambienced.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/ambience/{name}
systemctl-user restart ambienced.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "It's just upgrade"
systemctl-user restart ambienced.service
fi
fi

%changelog
* Fri Oct 26 2018 0.1
- First build.
