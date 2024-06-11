#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def pose_callback(data):
    print("Turtle's current position:")
    print("X:", data.x)
    print("Y:", data.y)
    print("Theta (angle):", data.theta)

def turtle_position_listener():
    rospy.init_node('turtle_position_listener', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        turtle_position_listener()
    except rospy.ROSInterruptException:
        pass
