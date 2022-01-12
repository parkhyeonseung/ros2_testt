import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
bridge = CvBridge()

class BasicSubscriber(Node):

    def __init__(self):
        super().__init__('image_raw')
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,1
            )
        self.subscription  

    def listener_callback(self, data):
        cv_image = bridge.imgmsg_to_cv2(data,'bgr8')
        cv2.imshow('call',cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    basic_subcriber = BasicSubscriber()
    rclpy.spin(basic_subcriber)

    basic_subcriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()