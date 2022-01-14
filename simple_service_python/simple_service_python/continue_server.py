from roscr_bridge_interfaces.srv import IsimpleLedControl

import rclpy
from rclpy.node import Node


class LedControlServer(Node):

    def __init__(self):
        super().__init__('led_control_server')
        self.srv = self.create_service(IsimpleLedControl, 'led_control', self.service_callback)

    def service_callback(self, request, response):
        if request.command == 1:
            response.is_success = True
        else:
            response.is_success = False 
        self.get_logger().info('Command: %d' % request.command)
        # 여기 이부분에 OpenCR과 시리얼 통신을 하는 코드가 들어가게 됩니다.

        return response


def main(args=None):
    rclpy.init(args=args)

    led_control_server = LedControlServer()

    rclpy.spin(led_control_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()