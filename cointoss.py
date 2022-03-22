# coding:utf-8

# ランダムデータの生成や計算ができるモジュール
import numpy as np

# グラフを描画できるモジュール

from matplotlib import pyplot as plt

# 横軸に試行回数、縦軸に表がでた相対度数(a/n)をとってグラフ化する

# グラフの設定
def set_up_graph():
    plt.xlabel("n")  # 横軸の名前 (日本語使えない)
    plt.ylabel("a/n")  # 縦軸の名前(日本語使えない)
    plt.xlim(0.0, 1000.0)  # x軸の最大と最小を指定　float指定が必須(サイレントエラー)
    plt.ylim(0.0, 1.0)  # y軸の最大の最初を指定 float指定が必須(サイレントエラー)
    plt.xticks(np.arange(0, 1001, 100))  # 横軸のメモリ
    plt.yticks([0, 0.25, 0.50, 0.75, 1.00])  # 縦軸のメモリ
    plt.grid()  # grid追加(0.50に収束しているのがみやすいように)


# グラフの描画
def render_graph(x, y, file_name):
    plt.figure()
    set_up_graph()
    plt.plot(x, y)
    plt.savefig(file_name)


# 結果取得
def get_result_array():
    return np.random.randint(low=0, high=2, size=(1000,))


# x軸を定義
def get_x_axis():
    return range(1, 1001)  # x軸の値を配列に


# y軸の値を配列に
def get_y_axis():
    # numpyでランダムに1と０を取得して配列に格納
    result = np.random.randint(low=0, high=2, size=(1000,))
    # y軸の値を配列に(実際にいれる値は後でfor文で入れる)
    y_axis = []
    # 試行回数のカウント変数(確率を扱うためにfloatにする)
    count = float(0)
    # 表が出た回数のカウント変数(確率を扱うためにfloatにする)
    front = float(0)
    # y_axisを作成(相対度数)
    for i in result:
        # numpyint64をネイティブのintに変換
        i = int(i)
        count += 1
        if i == 1:
            front += 1
        p = float(front / count)
        y_axis.append(p)
    return y_axis


def main():
    print(get_result_array())
    x_axis = get_x_axis()
    y_axis = get_y_axis()
    render_graph(x_axis, y_axis, "cointoss.png")


if __name__ == "__main__":
    main()
