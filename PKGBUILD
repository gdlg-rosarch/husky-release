# Script generated with Bloom
pkgdesc="ROS - Clearpath Husky robot driver"
url='http://ros.org/wiki/husky_base'

pkgname='ros-kinetic-husky-base'
pkgver='0.3.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-controller-manager'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-hardware-interface'
'ros-kinetic-husky-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-roslaunch'
'ros-kinetic-roslint'
'ros-kinetic-sensor-msgs'
)

depends=('ros-kinetic-controller-manager'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-diff-drive-controller'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hardware-interface'
'ros-kinetic-husky-control'
'ros-kinetic-husky-description'
'ros-kinetic-husky-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-topic-tools'
)

conflicts=()
replaces=()

_dir=husky_base
source=()
md5sums=()

prepare() {
    cp -R $startdir/husky_base $srcdir/husky_base
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

