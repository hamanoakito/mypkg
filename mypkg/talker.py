import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import math

R = 1
TREAD_WIDTH = 30
T = 0.5


class Coord(Node):
    def __init__(self):
        super().__init__("Coord")
        self.pub = self.create_publisher(Float32MultiArray, "coordinate", 10)
        self.create_timer(T, self.calc_cb)
        self.co = [0.0,0.0]
        self.right_angular_velocity = 10
        self.left_angular_velocity = 10

    def change_angular_velocity(self):
        if self.co[0] >= 60:
            self.right_angular_velocity = 10
            self.left_angular_velocity = 20
        

    def calc_cb(self):
        self.change_angular_velocity()

        msg = Float32MultiArray()
        msg.data = self.co
        self.pub.publish(msg)

        right_velocity = R * self.right_angular_velocity
        left_velocity = R * self.left_angular_velocity

        theta = ((right_velocity - left_velocity) * T) / TREAD_WIDTH
        self.co[0] = self.co[0] + ((right_velocity + left_velocity) * T * math.cos(theta)) / 2
        self.co[1] = self.co[1] + ((right_velocity + left_velocity) * T * math.sin(theta)) / 2
        
        


def main():
    rclpy.init()
    node = Coord()
    rclpy.spin(node)
