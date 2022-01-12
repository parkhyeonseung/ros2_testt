import rclpy
from rclpy.node import Node
from basic_interface.srv import Basecal
import sys, select, termios, tty

settings = termios.tcgetattr(sys.stdin)

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist: key = sys.stdin.read(1)
    else: key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class Basecalclient(Node):
    def __init__(self):
        super().__init__('base_cal_client')
        self.client = self.create_client(Basecal,'base_cal')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('wait for server')
        self.req = Basecal.Request()
        self.sum_key = ''

    def send_request(self):
        while True:
            key = getKey()
            if key not in ['+','-','*','/',' ']:
                self.sum_key +=key
            elif key in ['+','-','*','/'] :
                self.req.ac=float(self.sum_key)
                self.sum_key =''
                self.req.gi = key
            elif key == ' ':
                self.req.bc=float(self.sum_key)
                self.sum_key = ''
                self.future = self.client.call_async(self.req)
                

def main(args=None):
    rclpy.init(args=args)
    basic_cal_client = Basecalclient()

    while rclpy.ok():
        basic_cal_client.get_logger().info('cal')
        basic_cal_client.send_request()
        rclpy.spin_once(basic_cal_client)
        if basic_cal_client.future.done():
            try:
                response = basic_cal_client.future.result()
            except Exception as e:
                basic_cal_client.get_logger().info('service all fail : %r' % (e,))
            except KeyboardInterrupt:
                break
            else:
                if type(response.result) == float:
                    basic_cal_client.get_logger().info('%f %s %f = %f ' % (basic_cal_client.req.ac,basic_cal_client.req.gi,basic_cal_client.req.bc, response.result))
                else:
                    basic_cal_client.get_logger().info('fail')

    basic_cal_client.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
