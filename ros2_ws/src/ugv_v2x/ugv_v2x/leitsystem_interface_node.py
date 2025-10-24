import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8, Bool
from rclpy.parameter import Parameter

class LeitsystemInterface(Node):
    def __init__(self):
        super().__init__('leitsystem_interface')
        # Parameters simulate two TTL inputs; in real HW read GPIOs
        self.declare_parameter('ttl_green', False)
        self.declare_parameter('ttl_yellow', False)
        self.state_pub = self.create_publisher(UInt8, '/leitsys/state', 10)
        self.timer = self.create_timer(0.1, self.tick)

    def tick(self):
        is_green = self.get_parameter('ttl_green').get_parameter_value().bool_value
        is_yellow = self.get_parameter('ttl_yellow').get_parameter_value().bool_value
        # Mapping: 0=Red, 1=Yellow, 2=Green
        state = 2 if is_green else (1 if is_yellow else 0)
        msg = UInt8(); msg.data = state
        self.state_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LeitsystemInterface()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
