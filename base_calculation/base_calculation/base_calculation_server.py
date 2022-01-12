import rclpy
from rclpy.node import Node
from basic_interface.srv import Basecal

class Basecalserver(Node):
    def __init__(self):
        super().__init__('base_calculation_server')
        self.srv = self.create_service(Basecal,'base_cal',self.callback)

    def callback(self,request,response):
        if request.gi in ['*','-','+','/']:
            cal = str(request.ac)+request.gi+str(request.bc)
            response.result = eval(cal)
        else :
            self.get_logger().info('please input +,-,*,/')
        self.get_logger().info('%d %s %d = %d' % (request.ac , request.gi, request.bc,response.result))
        return response

def main(args=None):
    rclpy.init(args=args)
    base_cal_server = Basecalserver()
    rclpy.spin(base_cal_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

    
        