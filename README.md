# 対向二輪型車輪移動ロボットの自己位置推定
![test](https://github.com/hamanoakito/mypkg/actions/workflows/test.yml/badge.svg)


## 概要説明
- ros2で利用可能なパッケージです
- 車輪の角速度、半径、車輪間距離からロボットの(x,y)座標を計算して出力します


## ノード説明
### calculate
このノードがロボットの座標を計算します。

#### 使用方法
自分が使用するロボットの車輪の角速度、半径、車輪間距離を変更する。
現在のコードでは以下の部分である。
```python
R = 1                             #半径           11行目

TREAD_WIDTH = 30                  #車輪間距離     13行目

self.right_angular_velocity = 10  #右車輪の角速度 33行目
self.left_angular_velocity = 10   #左車輪の角速度 34行目
```
ここを変更して実行してください。

#### パブリッシュするトピック
- coordinate
  - x,y座標の数値を受け取ります
