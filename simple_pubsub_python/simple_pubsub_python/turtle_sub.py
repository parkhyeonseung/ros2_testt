import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu
from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data

class BasicSubscriber(Node):

    def __init__(self):
        super().__init__('basic_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.ranges[20:25])
        # self.get_logger().info('Received: ')


def main(args=None):
    rclpy.init(args=args)
    basic_subcriber = BasicSubscriber()
    rclpy.spin(basic_subcriber)

    basic_subcriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()