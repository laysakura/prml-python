"""
    prmlpy.plot
    ~~~~~~~~~~~

    :synopsis: matplotlib を使った可視化系のプログラム群。

    matplotlib を使った可視化系のプログラム群。実行可能なものが揃っている。
"""

# standard modules

# 3rd party modules
from matplotlib import pyplot as plt
from matplotlib import gridspec

# original modules


MAX_SLIDERS = 10


def init_figure(n_sliders):
    """グラフ領域の横にウィジェットが並ぶ、典型的な図領域を作成する。

    配置は GridSpec ( http://matplotlib.org/users/gridspec.html ) を使用して調整。

    :param n_sliders: スライダーバーの個数。
    :return: (ax_graph, ax_slider_list)
    """
    # グラフ領域
    gs_graph = gridspec.GridSpec(1, 1)
    gs_graph.update(left=0.05, right=0.80, wspace=0.05)
    ax_graph = plt.subplot(gs_graph[:, :])

    # スライダーバー領域 (スライダーバーは最大10本まで入る)
    gs_slider = gridspec.GridSpec(MAX_SLIDERS, 1)
    gs_slider.update(left=0.80, right=1.00, wspace=0.05)
    ax_slider_list = [plt.subplot(gs_slider[i, :]) for i in range(n_sliders)]

    return ax_graph, ax_slider_list
