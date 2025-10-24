import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class MissionManager(Node):
    def __init__(self):
        super().__init__('mission_manager')
        self.pub = self.create_publisher(PoseStamped, '/mission/goal', 10)
        # In a real setup, read goals from params/map; here publish nothing

def main(args=None):
    rclpy.init(args=args)
    node = MissionManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
