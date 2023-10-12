#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from dancing_tools.srv import imagecapture, imagecaptureResponse

def save_image_callback(req):
    cv_bridge = CvBridge()
    try:
        rgb_image_msg = rospy.wait_for_message('/dancing_camera1/color/image_raw', Image, timeout=5.0)
        depth_image_msg = rospy.wait_for_message('/dancing_camera1/depth/image_rect_raw', Image, timeout=5.0)
        
        rgb_image_cv = cv_bridge.imgmsg_to_cv2(rgb_image_msg, desired_encoding="passthrough")
        depth_image_cv = cv_bridge.imgmsg_to_cv2(depth_image_msg, desired_encoding="passthrough")
        # rgb_image_cv = cv2.rotate(rgb_image_cv, cv2.ROTATE_180)
        rgb_image_cv = cv2.cvtColor(rgb_image_cv, cv2.COLOR_RGB2BGR)
        # depth_image_cv = cv2.rotate(depth_image_cv, cv2.ROTATE_180)
        
        rgb_image_data = np.array(rgb_image_cv)
        depth_image_data = np.array(depth_image_cv)
        

        rgb_filename = req.filename + "_rgb.jpg"
        cv2.imwrite(rgb_filename, rgb_image_cv)
        rospy.loginfo("RGB image saved as %s", rgb_filename)

        depth_filename = req.filename + "_depth.npy"
        np.save(depth_filename, depth_image_data)
        rospy.loginfo("Depth image saved as %s", depth_filename)

        response = imagecaptureResponse()
        response.rgb_image = rgb_image_msg
        response.depth_image = depth_image_msg
        return response
    except rospy.ROSException:
        rospy.logerr("Failed to capture images.")
        return None
if __name__ == '__main__':
    rospy.init_node('save_image_service')
    rospy.Service('save_image', imagecapture, save_image_callback)
    rospy.spin()
