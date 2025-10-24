import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, UInt8

class EmergencyBrake(Node):
    def __init__(self):
        super().__init__('emergency_brake')
        self.pub = self.create_publisher(Bool, '/emerg_stop', 10)
        self.sub = self.create_subscription(UInt8, '/traffic_light/state', self.cb, 10)

    def cb(self, msg: UInt8):
        stop = (msg.data == 0)
        self.pub.publish(Bool(data=stop))

def main(args=None):
    rclpy.init(args=args)
    node = EmergencyBrake()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
