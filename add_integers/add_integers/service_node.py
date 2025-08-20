import rclpy
from rclpy.node import Node
from custom_interface.srv import AddIntegers

class AddIntegersService(Node):

    def __init__(self):
        super().__init__('add_int_service')
        self.srv = self.create_service(AddIntegers, 'add_two_ints', self.add_integers_callback)

    def add_integers_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Incoming Request: a={request.a}, b={request.b}')
        return response

if __name__ == '__main__':
    rclpy.init()

    # Create Node
    service = AddIntegersService()

    # Run/Use the node
    rclpy.spin(service)

    # Shutdown
    rclpy.shutdown()