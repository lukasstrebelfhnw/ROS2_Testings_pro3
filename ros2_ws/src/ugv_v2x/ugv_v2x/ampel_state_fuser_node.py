import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8

class AmpelStateFuser(Node):
    def __init__(self):
        super().__init__('ampel_state_fuser')
        self.state_pub = self.create_publisher(UInt8, '/traffic_light/state', 10)
        self.sub1 = self.create_subscription(UInt8, '/leitsys/state', self.cb, 10)
        # Here you could also subscribe to vision-based traffic light detection
        self.last = 0

    def cb(self, msg: UInt8):
        # For now just forward, but hook in vision confidence etc.
        self.last = msg.data
        self.state_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = AmpelStateFuser()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
