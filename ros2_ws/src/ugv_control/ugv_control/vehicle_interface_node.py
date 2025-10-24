import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class VehicleInterface(Node):
    def __init__(self):
        super().__init__('vehicle_interface')
        self.sub = self.create_subscription(Twist, '/cmd_vel_limited', self.cb, 10)
        self.estop_sub = self.create_subscription(Bool, '/emerg_stop', self.estop_cb, 10)
        # TODO: init hardware drivers (ESC, steering servo) or publish to micro-ROS bridge
        self.estop = False

    def estop_cb(self, msg: Bool):
        self.estop = msg.data

    def cb(self, cmd: Twist):
        if self.estop:
            # send zero to hardware
            return
        # map cmd to hardware here
        # e.g., PWM for throttle/steer
        pass

def main(args=None):
    rclpy.init(args=args)
    node = VehicleInterface()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
