import rclpy
from rclpy.node import Node
from basic_interface.srv import Mocksensorcontrol

class Customserviceserver(Node):
    def __init__(self):
        super().__init__('custom_service_server')
        self.srv = self.create_service(Mocksensorcontrol,'mock_sensor',self.callback)

    def callback(self,request,response):
        if request.command ==1:
            self.get_logger().info('control %s : %d' % (request.sensor_id,request.command))
            response.is_success = True
        else:
            self.get_logger().info('Error')
            response.is_success = False

        return response

def main(args=None):
    rclpy.init(args=args)
    custom_service_server = Customserviceserver()
    rclpy.spin(custom_service_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    