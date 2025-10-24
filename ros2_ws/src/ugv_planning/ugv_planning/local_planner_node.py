import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class LocalPlanner(Node):
    def __init__(self):
        super().__init__('local_planner')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.too_close = False
        self.create_subscription(Bool, '/safety/too_close', self.cb_close, 10)
        self.timer = self.create_timer(0.1, self.tick)

    def cb_close(self, msg: Bool):
        self.too_close = msg.data

    def tick(self):
        cmd = Twist()
        if self.too_close:
            cmd.linear.x = 0.0
        else:
            cmd.linear.x = 0.8  # simple forward for demo
            cmd.angular.z = 0.0
        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = LocalPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
