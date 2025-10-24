import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool

class CollisionMonitor(Node):
    def __init__(self):
        super().__init__('collision_monitor')
        self.pub = self.create_publisher(Bool, '/safety/too_close', 10)
        self.sub = self.create_subscription(LaserScan, '/scan', self.cb, 10)
        self.declare_parameter('min_distance', 0.5)

    def cb(self, scan: LaserScan):
        md = self.get_parameter('min_distance').value
        if not scan.ranges:
            return
        if min([r for r in scan.ranges if r > 0.0] or [999]) < md:
            self.pub.publish(Bool(data=True))
        else:
            self.pub.publish(Bool(data=False))

def main(args=None):
    rclpy.init(args=args)
    node = CollisionMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
