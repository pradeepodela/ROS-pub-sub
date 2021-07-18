#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def watch_carry(data):
    watched = 'i am elon  i have watched the video of carry with title'+str(data.data)

    print(watched)


def watch_pradeep(data):
    watched = 'i am elon  i have watched the video of carry with title'+str(data.data)
    print(watched)


def subcriber():

    rospy.init_node('elon')

    rospy.Subscriber('carryminati',String,watch_carry)


    rospy.Subscriber('pradeep_robotics',String,watch_pradeep)

if __name__ == '__main__':
    try:
        subcriber()
    except rospy.ROSInterruptException:
        print('some thing went wrong ')
        pass



