#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class Commander:
    def __init__(self) -> None:
        rospy.init_node('commander1', anonymous=True)

        self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=1)

        rospy.Subscriber('/nafi_command', String, self.command_callback)
    
    def command_callback(self, data):
        rospy.loginfo("Command received: {}".format(data.data))

        # Amar pathano

        velocity = Twist()

        if data.data.lower() == "forward":
            velocity.linear.x = 2
        elif data.data.lower() == "backward":
            velocity.linear.x = -2
        elif data.data.lower() == "left":
            velocity.angular.z = 0.5
        elif data.data.lower() == "right":
            velocity.angular.z = -0.5
        self.pub.publish(velocity)


if __name__=='__main__':
    node = Commander()
    rospy.spin()