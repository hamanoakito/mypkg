# SPDX-FileCopyrightText: 2025 Akito Hamano
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import math

#定数の宣言
#車輪半径
R = 1
#車輪と車輪の間の距離
TREAD_WIDTH = 30
#時間
T = 0.5

#Coordクラスの作成
class Coord(Node):
    def __init__(self):
        super().__init__("Coord")
        self.pub = self.create_publisher(Float32MultiArray, "coordinate", 10)
        self.create_timer(T, self.calc_cb)

        #初期座標
        self.co = [0.0,0.0]
        #左右の車輪の角速度
        self.right_angular_velocity = 10
        self.left_angular_velocity = 10

    #角速度を途中で変化させる
    def change_angular_velocity(self):
        if self.co[0] >= 60:
            self.right_angular_velocity = 10
            self.left_angular_velocity = 20

    #自己位置推定の座標計算    
    def calc_cb(self):
        self.change_angular_velocity()

        msg = Float32MultiArray()
        msg.data = self.co
        self.pub.publish(msg)

        #左右の車輪の速度
        right_velocity = R * self.right_angular_velocity
        left_velocity = R * self.left_angular_velocity
        #姿勢の角度
        theta = ((right_velocity - left_velocity) * T) / TREAD_WIDTH
        #座標の計算
        self.co[0] = self.co[0] + ((right_velocity + left_velocity) * T * math.cos(theta)) / 2
        self.co[1] = self.co[1] + ((right_velocity + left_velocity) * T * math.sin(theta)) / 2
        
def main():
    rclpy.init()
    node = Coord()
    rclpy.spin(node)
