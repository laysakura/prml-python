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


def init_plot_area():
    plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)


def main():
    global line2d, axfreq, slider_mu

    init_plot_area()

    x_list = np.arange(0.0, 1.0, 0.001)
    y_list = normal_dist(x_list, 0.5, 0.2)

    line2d, = plt.plot(x_list, y_list)

    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
    slider_mu = widgets.Slider(axfreq, 'mu', 0.0, 1.0, valinit=0.5)
    slider_mu.on_changed(update_plot)

    plt.show()


if __name__ == '__main__':
    main()