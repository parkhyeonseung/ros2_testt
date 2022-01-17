from basic_interface.srv import IsimpleLedControl
import serial
import rclpy
from rclpy.node import Node
import time


class LedControlServer(Node):

    def __init__(self):
        super().__init__('led_control_server')
        self.srv = self.create_service(IsimpleLedControl, 'led_control', self.service_callback)
        self.ser = serial.Serial ("/dev/ttyACM0", 115200)
    def service_callback(self, request, response):
        if request.command == 1:
            response.is_success = True
            self.ser.write(str.encode('1')) #transmit data serially
            time.sleep(0.1)
            self.ser.write(str.encode('q')) #transmit data serially
            time.sleep(0.1)
            self.ser.write(str.encode('w')) #transmit data serially
            time.sleep(0.1)
            self.ser.write(str.encode('e')) #transmit data serially
            time.sleep(0.1)
            self.ser.write(str.encode('r')) #transmit data serially
            time.sleep(0.1)
            self.ser.write(str.encode('a')) #transmit data serially
            time.sleep(0.1)
            self.ser.write(str.encode('s')) #transmit data serially
            time.sleep(0.1)
            self.ser.write(str.encode('d')) #transmit data serially
            time.sleep(0.1)

            # self.ser.write(0x32) #transmit data serially
            # time.sleep(2)
            # self.ser.write(0x33) #transmit data serially
            # time.sleep(2)
            # self.ser.write(0x34) #transmit data serially
            # time.sleep(2)
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