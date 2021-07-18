#!/usr/bin/env python

import rospy
from std_msgs.msg import String

video_number = 0


def watch(data):

    watched = 'i have watched the video of carry with title'+str(data.data)

    print(watched)


def  subcribe():

    sub = rospy.Subscriber('indian_robotics_community' , String , watch)

    rospy.init_node('pradeep')


    pub = rospy.Publisher('pradeep_robotics' , String , queue_size=1)

    rate= rospy.Rate(1)
    while not rospy.is_shutdown():

        global video_number

        video_title = 'robotics number' + str(video_number)

        pub.publish(video_title)

        print(video_title)

        video_number = video_number+1

        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    try:
        subcribe()
    except rospy.ROSInterruptException:
        pass