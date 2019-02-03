Name:           ros-melodic-rqt-tf-tree
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS rqt_tf_tree package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_tf_tree
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-python-qt-binding >= 0.2.19
Requires:       ros-melodic-qt-dotgraph
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rqt-graph
Requires:       ros-melodic-rqt-gui
Requires:       ros-melodic-rqt-gui-py
Requires:       ros-melodic-tf2
Requires:       ros-melodic-tf2-msgs
Requires:       ros-melodic-tf2-ros
BuildRequires:  python-mock
BuildRequires:  ros-melodic-catkin

%description
rqt_tf_tree provides a GUI plugin for visualizing the ROS TF frame tree.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Sun Feb 03 2019 Isaac I.Y. Saito <gm130s@gmail.com> - 0.6.0-0
- Autogenerated by Bloom

* Wed Apr 18 2018 Aaron Blasdel <ablasdel@gmail.com> - 0.5.8-0
- Autogenerated by Bloom

