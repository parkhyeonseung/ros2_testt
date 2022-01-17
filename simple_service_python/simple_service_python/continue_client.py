import sys

from basic_interface.srv import IsimpleLedControl
import rclpy
from rclpy.node import Node


class LedControlClient(Node):

    def __init__(self):
        super().__init__('led_control_client')
        self.client = self.create_client(IsimpleLedControl, 'led_control') # Client builder 패턴
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service server...')
        self.req = IsimpleLedControl.Request()

    def send_request(self):
        self.req.command = int(input())
        self.future = self.client.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    led_control_client = LedControlClient()
 
    while(1):
        led_control_client.send_request()
        while rclpy.ok():
            rclpy.spin_once(led_control_client)
            if led_control_client.future.done():
                try:
                    response = led_control_client.future.result()
                except Exception as e:
                    led_control_client.get_logger().info(
                        'Service call failed: %r' % (e,))
                else:
                    if response.is_success:
                        led_control_client.get_logger().info("success")
                    else:
                        led_control_client.get_logger().info("false")
                break

    led_control_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()