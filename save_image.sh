#! /bin/bash

if [ "$1" ]; then
	rosservice call /save_image $1
	chmod 777 $1_rgb.jpg $1_depth.npy
else
	rosservice call /save_image suka
	chmod 777 suka_rgb.jpg suka_depth.npy
fi
