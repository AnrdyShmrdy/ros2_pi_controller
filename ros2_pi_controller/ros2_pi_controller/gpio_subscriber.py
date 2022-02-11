# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

from rclpy.node import Node

from std_msgs.msg import String


class GpioSubscriber(Node):

    def __init__(self):
        super().__init__('gpio_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        if 'ON' in msg.data:
            if '24' in msg.data:
                GPIO.output(24, GPIO.HIGH)  #turn on the LED
            elif '23' in msg.data:
                GPIO.output(23, GPIO.HIGH)  #turn on the LED
            elif '22' in msg.data:
                GPIO.output(22, GPIO.HIGH)  #turn on the LED
        elif 'OFF' in msg.data:
            if '24' in msg.data:
                GPIO.output(24, GPIO.LOW)  #turn off the LED
            elif '23' in msg.data:
                GPIO.output(23, GPIO.LOW)  #turn off the LED
            elif '22' in msg.data:
                GPIO.output(22, GPIO.LOW)  #turn off the LED




def main(args=None):
    rclpy.init(args=args)

    gpio_subscriber = GpioSubscriber()

    rclpy.spin(gpio_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gpio_subscriber.destroy_node()
    rclpy.shutdown()
    GPIO.cleanup()                  #clean up all the ports used


if __name__ == '__main__':
    main()

