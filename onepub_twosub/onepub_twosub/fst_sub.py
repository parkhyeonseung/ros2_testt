import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class first_sub(Node):
    def __init__(self):
        super().__init__('sum_calculator')
        self.subs = self.create_subscription(Int64,'natural_number_signal',self.callback,1)
        self.sum = 0
        self.subs

    def callback(self,msg):
        self.sum+=msg.data
        self.get_logger().info('Received: %d | Sum: %d' % (msg.data ,self.sum))

def main(args=None):
    rclpy.init(args=args)
    firstsub = first_sub()
    rclpy.spin(firstsub)
    
    firstsub.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()


        