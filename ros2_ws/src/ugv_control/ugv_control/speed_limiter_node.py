import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8

class SpeedLimiter(Node):
    def __init__(self):
        super().__init__('speed_limiter')
        self.max_v_green = self.declare_parameter('max_v_green', 1.5).value
        self.max_v_yellow = self.declare_parameter('max_v_yellow', 0.5).value
        self.max_v_red = 0.0
        self.state = 0
        self.pub = self.create_publisher(Twist, '/cmd_vel_limited', 10)
        self.sub_cmd = self.create_subscription(Twist, '/cmd_vel', self.cb_cmd, 10)
        self.sub_state = self.create_subscription(UInt8, '/traffic_light/state', self.cb_state, 10)

    def cb_state(self, msg: UInt8):
        self.state = int(msg.data)

    def clamp(self, v, cap):
        if v > cap: return cap
        if v < -cap: return -cap
        return v

    def cb_cmd(self, cmd: Twist):
        capped = Twist()
        if self.state == 2:
            cap = self.max_v_green
        elif self.state == 1:
            cap = self.max_v_yellow
        else:
            cap = self.max_v_red
        capped.linear.x = self.clamp(cmd.linear.x, cap)
        capped.angular.z = cmd.angular.z  # could also limit yaw rate
        self.pub.publish(capped)

def main(args=None):
    rclpy.init(args=args)
    node = SpeedLimiter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
