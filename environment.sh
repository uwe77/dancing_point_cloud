#! /bin/bash

source /opt/ros/melodic/setup.bash
source ~/dancing_point_cloud/catkin_ws/devel/setup.bash

if [ "$1" ]; then
	echo "ROS MASTER $1"
	export ROS_MASTER_URI=http://$1:11311
else
	echo "ROS MASTER 127.0.0.1"
	export ROS_MASTER_URI=http://127.0.0.1:11311
fi

if [ "$2" ]; then
	echo "ROS IP $2"
	export ROS_IP=$2
else
	echo "ROS_IP 127.0.0.1"
	export ROS_IP=127.0.0.1
fi
