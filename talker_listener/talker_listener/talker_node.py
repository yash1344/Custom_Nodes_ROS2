import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello, world...{self.count}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.count += 1

def main(args = None):
    rclpy.init(args=args)

    # Create Node
    talkerNode = TalkerNode()

    # Use Node
    rclpy.spin(talkerNode)

    # Destroy Node
    talkerNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()