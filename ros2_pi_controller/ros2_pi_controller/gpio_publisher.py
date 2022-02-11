import rclpy
import time
from rclpy.node import Node

from std_msgs.msg import String


class GpioPublisher(Node):

    def __init__(self):
        super().__init__('gpio_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.pin_no = 24

    def timer_callback(self):
        msg = String()
        msg.data = 'ON %d' % self.pin_no
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        time.sleep(1.0)
        msg.data = 'OFF %d' % self.pin_no
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    
    gpio_publisher = GpioPublisher()

    rclpy.spin(gpio_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gpio_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
