import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class onepub(Node):
    def __init__(self):
        super().__init__('natural_number_generator')
        self.publisher = self.create_publisher(Int64,'natural_number_signal',1)
        tick = 1
        self.timer = self.create_timer(tick,self.callback)
        self.count = 0

    def callback(self):
        msg = Int64()
        msg.data = self.count
        self.publisher.publish(msg)
        self.get_logger().info('pub: %d' % msg.data)
        self.count+=1

def main(args=None):
    rclpy.init(args=args)
    onepub_ = onepub()
    rclpy.spin(onepub_)

    onepub_.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
