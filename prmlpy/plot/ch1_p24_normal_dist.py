"""
    prmlpy.plot.ch1_p24_normal_dist.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 正規分布の可視化。

    正規分布の可視化。
"""


# standard modules

# 3rd party modules
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import widgets as widgets
from matplotlib import gridspec

# original modules
from prmlpy.distribution.normal import normal_dist


# global vars
_widgets = {
    'sliders': {},
}
line2d = None  # mtaplotlib.pyplot.plot() の返り値。ウィジェットのコールバックで再設定する。

# [TODO] - あとで widgets で一般化
axfreq = None
slider_mu = None



def update_plot(_):
    """
    matplotlib.widgets.*.on_changed に渡すコールバック関数。

    :param _:  matplotlib.widgets.*.on_changed のコールバックがセットする値だが、使わない。
    :return: None
    """
    mu = slider_mu.val
    x_list = np.arange(0.0, 1.0, 0.001)
    y_list = normal_dist(x_list, mu, 0.2)
    global line2d
    line2d.set_ydata(y_list)


def init_figure():
    """
    グラフ領域の横にウィジェットが並ぶ、典型的な図領域を作成する。

    配置は GridSpec ( http://matplotlib.org/users/gridspec.html ) を使用して調整。

    :return: (ax_graph, ax_widget)
    """
    # グラフ領域
    gs_graph = gridspec.GridSpec(1, 1)
    gs_graph.update(left=0.00, right=0.80, wspace=0.05)
    ax_graph = plt.subplot(gs_graph[:, :])

    # スライダーバー領域 (スライダーバーは最大10本まで入る)
    gs_slider = gridspec.GridSpec(10, 1)
    gs_slider.update(left=0.80, right=1.00, wspace=0.05)
    ax_slider0 = plt.subplot(gs_slider[0, :])

    return ax_graph, ax_slider0


def main():
    global line2d, axfreq, slider_mu

    ax_graph, ax_slider0 = init_figure()

    x_list = np.arange(0.0, 1.0, 0.001)
    y_list = normal_dist(x_list, 0.5, 0.2)

    line2d, = ax_graph.plot(x_list, y_list)

    #axfreq = plot.axes([0.25, 0.1, 0.65, 0.03])
    slider_mu = widgets.Slider(ax_slider0, 'mu', 0.0, 1.0, valinit=0.5)
    slider_mu.on_changed(update_plot)

    plt.show()


if __name__ == '__main__':
    main()