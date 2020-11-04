#! /usr/bin/env python

import rospy
import rosbag
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

def callback(msg):
	print (msg)

rospy.init_node('topic_subscriber')
rate=rospy.Rate(10)
sub1=rospy.Subscriber('/mouse_topic',Pose2D,callback)
sub=rospy.Subscriber('/keyboard_topic',String,callback)
rate.sleep()
rospy.spin()

