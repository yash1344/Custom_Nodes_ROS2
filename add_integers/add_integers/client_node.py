import rclpy
import sys
from rclpy.node import Node
from custom_interface.srv import AddIntegers

class AddIntegersClientAsync(Node):

    def __init__(self):
        super().__init__('addition_client_async')
        self.client = self.create_client(AddIntegers, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        

    def send_request(self, a, b):
        request = AddIntegers.Request()
        request.a = int(sys.argv[1])
        request.b = int(sys.argv[2])
        self.future = self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)

    # Create Node
    client = AddIntegersClientAsync()
    client.send_request()

    # Use/Spin node
    while rclpy.ok():
        rclpy.spin_once(client)
        if client.future.done():
            try:
                response = client.future.result()
            except Exception as e:
                client.get_logger().error(f'Service call failed: {e}')
            else:
                client.get_logger().info(f'Result: {response.sum}')
            break

    # Shutdown
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()