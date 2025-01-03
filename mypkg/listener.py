import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import matplotlib.pyplot as plt

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            Float32MultiArray,        # 受信するメッセージ型
            'countup',              # トピック名
            self.listener_callback,  # コールバック関数
            10                       # キューサイズ
        )
        
        # プロットの準備
        self.x_data = []  # x座標
        self.y_data = []  # y座標
        plt.ion()          # インタラクティブモード開始
        self.fig, self.ax = plt.subplots()  # グラフ作成
        self.ax.set_xlabel('X')  # X軸のラベル
        self.ax.set_ylabel('Y')  # Y軸のラベル
        self.ax.set_xlim(0, 100)  # X軸の範囲
        self.ax.set_ylim(0, 100)  # Y軸の範囲

    def listener_callback(self, msg):
        # msg.data が [x, y] のペアと仮定
        x = msg.data[0]
        y = msg.data[1]
        
        # 受信した座標をデータに追加
        self.x_data.append(x)
        self.y_data.append(y)
        
        # プロットの更新
        self.ax.clear()  # 古いプロットを消去
        self.ax.scatter(self.x_data, self.y_data, color='blue')  # 新しい点をプロット
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_xlim(0, 100)  # X軸の範囲を設定
        self.ax.set_ylim(0, 100)  # Y軸の範囲を設定
        plt.draw()  # プロットを描画
        plt.pause(0.1)  # 少し待機して画面を更新

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)

if __name__ == "__main__":
    main()

