#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg calculate_check.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep "30.000000, 0.000000"


