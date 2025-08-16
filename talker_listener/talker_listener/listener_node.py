import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    # Create Node
    listener_node = ListenerNode()

    # Use Node
    rclpy.spin(listener_node)

    # Destroy Node
    listener_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()