#!/bin/bash
echo "Getting File"
wget $1 -q -O  /tmp/android-studio.deb > /dev/null
echo "Making temp dir"
mkdir /tmp/debbuild
echo "unpacking deb"
dpkg-deb -R /tmp/android-studio.deb /tmp/debbuild
echo "Making changes"
echo "ln -sf /opt/android-studio/bin/studio.sh /usr/bin/android-studio" > /tmp/debbuild/DEBIAN/preinst
echo "Maintainer: Phiwatec" > /tmp/debbuild/DEBIAN/control
echo "Package: android-studio" >> /tmp/debbuild/DEBIAN/control
echo "Version: ${2}" >> /tmp/debbuild/DEBIAN/control
echo "Architecture: amd64" >> /tmp/debbuild/DEBIAN/control
echo "Description: Android-Studio neu gepackt aus ChromeOS Version" >> /tmp/debbuild/DEBIAN/control 
echo "Packing deb"
dpkg-deb -b /tmp/debbuild /tmp/android-studio.deb
echo "Copying.."
mv /tmp/android-studio.deb $3
rm -r /tmp/debbuild
echo "Done :)"
