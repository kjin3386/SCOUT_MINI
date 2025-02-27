#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

def callback(img_msg):
    cv_image = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    cv2.imshow("RealSense Color Image", cv_image)
    cv2.waitKey(1)

rospy.init_node("realsense_viewer", anonymous=True)
rospy.Subscriber("/camera/color/image_raw", Image, callback)
rospy.spin()