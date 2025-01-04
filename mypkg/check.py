# SPDX-FileCopyrightText: 2025 Akito Hamano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class Coord_check(Node):
    def __init__(self):
        super().__init__("Coord_check")
        self.sub = self.create_subscription(Float32MultiArray,"coordinate", self.sub_cb, 10)

    def sub_cb(self, msg):
        for i in range(0, len(msg.data), 2):
            self.get_logger().info("%f, %f" % (msg.data[i], msg.data[i + 1]))

def main():
    rclpy.init()
    node = Coord_check()
    rclpy.spin(node)
