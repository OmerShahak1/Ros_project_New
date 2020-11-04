# Ros_project_New-ROS Noetic
Andromeda Assessment 

Dependencies:
pynput library

Executables are now installed in \catkin_ws\src\pack_ex\src:
Execute in this order:

1)makebag- record user keyboard inputs and mouse position inputs and stores them in a rosbag file (input.bag). Esc to stop.

2)subscribe- subscribes to the published topics('/mouse_topic' ,'/keyboard_topic') and outputs them in a console synchronously.

3)publish- reads the recorded rosbag file (input.bag) and publishes the inputs to '/mouse_topic' and '/keyboard_topic'.
