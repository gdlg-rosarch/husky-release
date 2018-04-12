Name:           ros-kinetic-husky-base
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS husky_base package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/husky_base
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-diagnostic-aggregator
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-diff-drive-controller
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-husky-control
Requires:       ros-kinetic-husky-description
Requires:       ros-kinetic-husky-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-topic-tools
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-husky-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-sensor-msgs

%description
Clearpath Husky robot driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Apr 11 2018 Paul Bovbel <paul@bovbel.com> - 0.3.0-0
- Autogenerated by Bloom

