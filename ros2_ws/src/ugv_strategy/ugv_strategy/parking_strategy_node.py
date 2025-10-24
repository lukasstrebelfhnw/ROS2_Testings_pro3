import rclpy
from rclpy.node import Node
from ugv_msgs.msg import ParkingSlots

class ParkingStrategy(Node):
    def __init__(self):
        super().__init__('parking_strategy')
        self.sub = self.create_subscription(ParkingSlots, '/parking/slots', self.cb, 10)

    def cb(self, msg: ParkingSlots):
        # Choose a free slot with best pose; placeholder
        pass

def main(args=None):
    rclpy.init(args=args)
    node = ParkingStrategy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
