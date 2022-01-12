import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class second_sub(Node):
    def __init__(self):
        super().__init__('factorial_calculator')
        self.subs = self.create_subscription(Int64,'natural_number_signal',self.callback,1)
        self.result = 0
        self.subs

    def callback(self,msg):
        self.result = self.fac(msg.data)
        self.get_logger().info('Received: %d | factorial: %d' % (msg.data, self.result))
    
    def fac(self,num):
        if num <= 0:
            return 1
        elif num==1:
            return 1
        else:
            return num*self.fac(num-1)
        

def main(args=None):
    rclpy.init(args=args)
    firstsub = second_sub()
    rclpy.spin(firstsub)
    
    firstsub.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()


        