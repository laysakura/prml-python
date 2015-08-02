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
from matplotlib import gridspec

# original modules
from prmlpy.distribution.normal import normal_dist
from prmlpy.widgetwrapper.slider import SliderWrapper


def init_figure(slider_list=[]):
    """グラフ領域の横にウィジェットが並ぶ、典型的な図領域を作成する。

    配置は GridSpec ( http://matplotlib.org/users/gridspec.html ) を使用して調整。

    :param slider_list: スライダーバー情報のリスト。
    :type sliders: list of prmlpy.widgetwrapper.Slider
    :return: (ax_graph, ax_slider_list)
    """
    MAX_SLIDERS = 10

    # グラフ領域
    gs_graph = gridspec.GridSpec(1, 1)
    gs_graph.update(left=0.00, right=0.80, wspace=0.05)
    ax_graph = plt.subplot(gs_graph[:, :])

    # スライダーバー領域 (スライダーバーは最大10本まで入る)
    gs_slider = gridspec.GridSpec(MAX_SLIDERS, 1)
    gs_slider.update(left=0.80, right=1.00, wspace=0.05)
    ax_slider_list = []
    for i, slider in enumerate(slider_list):
        ax_slider_list.append(plt.subplot(gs_slider[i, :]))

    return ax_graph, ax_slider_list


def main():
    def update_plot(_):
        """matplotlib.widgets.*.on_changed に渡すコールバック関数。

        :param _:  matplotlib.widgets.*.on_changed のコールバックがセットする値だが、使わない。
        :return: None
        """
        mu = slider_mu.get_widget().val
        x_list = np.arange(0.0, 1.0, 0.001)
        y_list = normal_dist(x_list, mu, 0.2)
        line2d.set_ydata(y_list)

    slider_mu = SliderWrapper(label='mu', min_val=0.0, max_val=1.0, init_val=0.5)
    ax_graph, (ax_slider_mu,) = init_figure([slider_mu])
    slider_mu.instantiate(axis=ax_slider_mu, on_changed=update_plot)

    x_list = np.arange(0.0, 1.0, 0.001)
    y_list = normal_dist(x_list, 0.5, 0.2)

    line2d, = ax_graph.plot(x_list, y_list)

    plt.show()


if __name__ == '__main__':
    main()