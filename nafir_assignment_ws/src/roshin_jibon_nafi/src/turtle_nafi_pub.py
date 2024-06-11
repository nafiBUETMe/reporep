#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class SendingNode:
    def __init__(self) -> None:
        rospy.init_node('sending_node1',anonymous=True)

        self.pub = rospy.Publisher('/nafi_command',String, queue_size=1)
    
    def send(self, command):
        self.pub.publish(command)
        rospy.loginfo("Sending command: {}".format(command))
    
    def run(self):
        rospy.loginfo("Sending node is running")

        while not rospy.is_shutdown():
            command = input("Enter command (Forward, Backward, Right, Left): ")
            self.send(command)
            rospy.sleep(1)


if __name__=='__main__':
    node = SendingNode()
    node.run()