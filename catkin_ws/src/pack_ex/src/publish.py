#! /usr/bin/env python

import rospy
import rosbag
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

rospy.init_node('topic_publisher')
pub=rospy.Publisher('/keyboard_topic', String, queue_size=10)
key_in=String()
pub1=rospy.Publisher('/mouse_topic', Pose2D, queue_size=10)
loc=Pose2D()
rate=rospy.Rate(10)
bag=rosbag.Bag('input.bag')
while not rospy.is_shutdown():
	for topic ,msg, t in bag.read_messages(topics=['mouse2D']):
		loc.x=msg.x
		loc.y=msg.y
		#print(loc)
		pub1.publish(loc)
	
	for topic ,msg, t in bag.read_messages(topics=['keyboard']):
		key_in=msg
		#print(key_in)
		pub.publish(key_in)	
	rate.sleep()
bag.close()



           


    
