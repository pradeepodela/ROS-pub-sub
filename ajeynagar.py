#!/usr/bin/env python

import rospy
from std_msgs.msg import String

video_num = 0


def youtuber():
    pub = rospy.Publisher('indian_robotics_community' , String , queue_size=1)

    rospy.init_node('123')  ### name of the node 

    rate = rospy.Rate(1)   ### noumber of times it shouild publish for 1 sec

    while not rospy.is_shutdown():
       

        publishing = 'hellow i have published a video ' 

       

        pub.publish(publishing)
        print(publishing)

        rate.sleep()



if __name__ == '__main__':
    try:
        youtuber()
    except rospy.ROSInterruptException:
        pass
        