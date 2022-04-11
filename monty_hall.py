# coding:utf-8
# ランダムデータの生成や計算ができるモジュール
import numpy as np

# グラフを描画できるモジュール
from matplotlib import pyplot as plt

# 乱数を生成できるモジュール
import random

# グラフの設定
def set_up_graph():
    # 横軸の名前 (日本語使えない)
    plt.xlabel("n")
    # 縦軸の名前(日本語使えない)
    plt.ylabel("a/n")
    # x軸の最大と最小を指定　float指定が必須(サイレントエラー)
    plt.xlim(0.0, 1000.0)
    # y軸の最大の最初を指定 float指定が必須(サイレントエラー)
    plt.ylim(0.0, 1.0)
    # 横軸のメモリ
    plt.xticks(np.arange(0, 1001, 100))
    # 縦軸のメモリ
    plt.yticks([0, 0.25, 0.33, 0.50, 0.67, 0.75, 1.00])
    # grid追加(0.50に収束しているのがみやすいように)
    plt.grid()


# グラフ描画
def render_graph(x, y, file_name):
    plt.figure()
    set_up_graph()
    plt.plot(x, y)
    plt.savefig(file_name)


# 1000回やった結果を取得
def get_result_array():
    # アタリと挑戦者が選ぶ扉を最初にランダムに決める
    # ２次元目の配列の１つ目の要素をアタリ、二つ目の要素をチャンレンジャーが選んだものとする
    win_and_choice = np.random.randint(0, 3, (1000, 2))
    return win_and_choice


# x軸の配列取得
def get_x_axis():
    return range(0, 1000)


# 扉を変えない場合のある時点の当たる確率を配列に。
def get_y_axis_1():
    # 最初の扉を選び変えない、という試行を繰り返して確率を計算する。
    # 一個目のグラフのy軸
    y_axis_1 = []
    # 試行回数のカウント変数(確率を扱うためにfloatにする)
    count = float(0)
    # 選んだ扉でアタリが出た回数のカウント変数(確率を扱うためにfloatにする)
    hit = float(0)

    for data in get_result_array():
        # pは相対度数としてください。
        # ここから自分で書く
        p = float(hit / count)
        y_axis_1.append(p)
    return y_axis_1


# 扉を変える場合のある時点の当たる確率を配列に。
def get_y_axis_2():
    # 扉を変える、という試行を繰り返して確率を計算する
    # 試行回数のカウント変数(確率を扱うためにfloatにする)
    count = float(0)
    hit = float(0)
    y_axis_2 = []
    for data in get_result_array():
        #ここから自分で書く
        #アタリ扉番号をwin　　という変数にして
        #選ぶ扉番号をchoice という変数にしてください。
        p = float(hit / count)
        y_axis_2.append(p)
    return y_axis_2


# 変えるか変えないかををランダムにやった時の当たる確率を配列に
def get_y_axis_3():
    y_axis_3 = []
    count = float(0)
    hit = float(0)
    for data in get_result_array():
        count += 1
        # アタリ
        win = data[0]
        # 挑戦者が選んだ扉
        choice = data[1]
        if win == choice:
            # 乱数を生成　1が変える　0が変えない
            is_changed = random.randint(0, 1)
            if is_changed == 0:
                hit += 1
            else:
                # 何もしない
                pass
        else:
            is_changed = random.randint(0, 1)
            if is_changed == 0:
                # 何もしない
                pass
            else:
                hit += 1
        p = float(hit / count)
        y_axis_3.append(p)
    return y_axis_3


def main():
    # printは説明用
    print(get_result_array())
    # x_axis = get_x_axis()
    # y_axis_1 = get_y_axis_1()
    # print(y_axis_1)
    # render_graph(x_axis, y_axis_1, "not_change.png")
    # y_axis_2 = get_y_axis_2()
    # print(y_axis_2)
    # render_graph(x_axis, y_axis_2, "change.png")
    # y_axis_3 = get_y_axis_3()
    # print(y_axis_3)
    # render_graph(x_axis, y_axis_3, "random.png")


if __name__ == "__main__":
    main()
