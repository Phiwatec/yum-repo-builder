#!/bin/bash
echo "Getting File"
wget $1 -q -O  /tmp/working.deb > /dev/null
echo "Making temp dir"
mkdir /tmp/debbuild
echo "unpacking deb"
touch /tmp/PRE
dpkg-deb -R /tmp/working.deb /tmp/debbuild
touch /tmp/AFTER
echo "Making changes"
echo "Maintainer: Phiwatec" > /tmp/debbuild/DEBIAN/control
echo "Package: prometheus-ping-exporter" >> /tmp/debbuild/DEBIAN/control
echo "Version: ${2}" >> /tmp/debbuild/DEBIAN/control
echo "Architecture: amd64" >> /tmp/debbuild/DEBIAN/control
echo "Description: Prometheus Ping Exporter" >> /tmp/debbuild/DEBIAN/control 
echo "Packing deb"
dpkg-deb -b /tmp/debbuild /tmp/working.deb
echo "Copying.."
mv /tmp/working.deb $3
rm -r /tmp/debbuild
echo "Done :)"
