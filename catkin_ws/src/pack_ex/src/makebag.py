#! /usr/bin/env python

import rospy
import rosbag
from pynput import mouse
from pynput import keyboard
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

bag=rosbag.Bag('input.bag','w')
s= String()
i=Pose2D()


print ('Start record - ESC TO STOP') 

def on_move(x, y):
	print('Pointer moved to {0}'.format((x, y)))
	i.x=x
	i.y=y
	bag.write('mouse2D',i)
      
def on_press(key):
    try:
        print('{0} pressed'.format( key.char))
        s.data=key.char
        bag.write('keyboard',s)
 	
    except AttributeError:
        print('{0} pressed'.format( key))
        s.data=key.name
        bag.write('keyboard',s)
        if key==keyboard.Key.esc:
        	return False
           
mouse_listener = mouse.Listener(
    on_move=on_move)

mouse_listener.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
bag.close()
    
