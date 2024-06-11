#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


if __name__=='__main__':
    rospy.init_node('cyonara', anonymous=True)

    while not rospy.is_shutdown():
        str = "Bye Bye Workshop"

        rospy.loginfo(str)