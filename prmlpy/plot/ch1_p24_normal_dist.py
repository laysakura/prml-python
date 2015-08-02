"""
    prmlpy.plot.ch1_p24_normal_dist.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 正規分布の可視化。

    正規分布の可視化。
"""


# standard modules

# 3rd party modules
import numpy as np

# original modules
from matplotlib import pyplot as plt
from prmlpy.distribution.normal import normal_dist
from prmlpy.widgetwrapper.slider import SliderWrapper
import prmlpy.plot


def main():
    def update_plot(_):
        """matplotlib.widgets.*.on_changed に渡すコールバック関数。

        :param _:  matplotlib.widgets.*.on_changed のコールバックがセットする値だが、使わない。
        :return: None
        """
        mu = slider_mu.get_widget().val
        sigma = slider_sigma.get_widget().val

        y_list = normal_dist(x_list, mu, sigma)
        line2d.set_ydata(y_list)

    INIT_MU = 0.5
    INIT_SIGMA = 0.01

    slider_mu = SliderWrapper(label='mu', min_val=0.0, max_val=1.0, init_val=INIT_MU)
    slider_sigma = SliderWrapper(label='sigma', min_val=0.01, max_val=0.10, init_val=INIT_SIGMA)

    ax_graph, (ax_slider_mu, ax_slider_sigma) = prmlpy.plot.init_figure([slider_mu, slider_sigma])

    slider_mu.instantiate(axis=ax_slider_mu, on_changed=update_plot)
    slider_sigma.instantiate(axis=ax_slider_sigma, on_changed=update_plot)

    x_list = np.arange(0.0, 1.0, 0.001)
    y_list = normal_dist(x_list, INIT_MU, INIT_SIGMA)

    line2d, = ax_graph.plot(x_list, y_list)

    plt.show()


if __name__ == '__main__':
    main()