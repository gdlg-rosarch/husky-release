# Script generated with Bloom
pkgdesc="ROS - Clearpath Husky installation and integration package"
url='http://ros.org/wiki/husky_bringup'

pkgname='ros-kinetic-husky-bringup'
pkgver='0.3.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-roslaunch'
)

depends=('python2-scipy'
'ros-kinetic-husky-base'
'ros-kinetic-husky-control'
'ros-kinetic-husky-description'
'ros-kinetic-imu-filter-madgwick'
'ros-kinetic-imu-transformer'
'ros-kinetic-lms1xx'
'ros-kinetic-microstrain-3dmgx2-imu'
'ros-kinetic-nmea-comms'
'ros-kinetic-nmea-navsat-driver'
'ros-kinetic-robot-localization'
'ros-kinetic-robot-upstart'
'ros-kinetic-tf'
'ros-kinetic-tf2-ros'
'ros-kinetic-um6'
'ros-kinetic-um7'
)

conflicts=()
replaces=()

_dir=husky_bringup
source=()
md5sums=()

prepare() {
    cp -R $startdir/husky_bringup $srcdir/husky_bringup
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

