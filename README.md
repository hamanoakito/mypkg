# 対向二輪型車輪移動ロボットの自己位置推定
![test](https://github.com/hamanoakito/mypkg/actions/workflows/test.yml/badge.svg)


## 概要説明
- ros2で利用可能なパッケージです
- 車輪の半径、車輪間距離、角速度からロボットの(x,y)座標を計算して出力します
- 摩擦などの外力などは考えず車輪の角速度のみで計算しています。ご了承ください


## ノード説明
### calculate
このノードがロボットの座標を計算します。
- この計算式は東北学院大学の「車輪移動ロボット」ページを参考にしています
- 詳細は[車輪移動ロボット](https://www.mech.tohoku-gakuin.ac.jp/rde/contents/course/robotics/indexframe.html)をご参照ください


#### 使用方法
自分が使用するロボットの車輪の半径、車輪間距離、角速度を変更する。
現在のコードでは以下の部分である。
```python
R = 1                             #半径           11行目

TREAD_WIDTH = 30                  #車輪間距離     13行目

self.right_angular_velocity = 10  #右車輪の角速度 33行目
self.left_angular_velocity = 10   #左車輪の角速度 34行目
```
ここを変更して実行してください。

#### パブリッシュされるトピック
- coordinate
  - x,y座標の数値を受け取ります





### check
テストを実行するために使用するノードです。
受け取った座標を端末に表示します。


## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます
- このパッケージのテストに利用したコンテナは下記のリンクのものを、本人の許可を得て使用しています
  - [ryuichiueda/ubuntu22.04-ros2:latest](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)
- © 2025 Akito Hamano


## 必要なソフトウェア
- python
  - テスト済みバージョン:3.7 ~ 3.10


## テスト環境
- ubuntu 24.04

