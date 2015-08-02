"""
    prmlpy.plot.ch2_p69_beta_dist
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 正規分布の可視化。

    正規分布の可視化。
"""


# standard modules

# 3rd party modules
import numpy as np

# original modules
from matplotlib import pyplot as plt
from prmlpy.distribution.beta import beta_dist
from prmlpy.widgetwrapper.slider import SliderWrapper
import prmlpy.plot


def main():
    def update_plot(_):
        """matplotlib.widgets.*.on_changed に渡すコールバック関数。

        :param _:  matplotlib.widgets.*.on_changed のコールバックがセットする値だが、使わない。
        """
        a = slider_a.get_widget().val
        b = slider_b.get_widget().val

        y_list = beta_dist(mu_list, a, b)
        line2d.set_ydata(y_list)

    INIT_A = 0.01
    INIT_B = 0.01

    slider_a = SliderWrapper(label='a', min_val=0.00, max_val=10.0, init_val=INIT_A)
    slider_b = SliderWrapper(label='b', min_val=0.00, max_val=10.0, init_val=INIT_B)

    ax_graph, (ax_slider_a, ax_slider_b) = prmlpy.plot.init_figure([slider_a, slider_b])

    slider_a.instantiate(axis=ax_slider_a, on_changed=update_plot)
    slider_b.instantiate(axis=ax_slider_b, on_changed=update_plot)

    mu_list = np.arange(0.0, 1.0, 0.001)
    y_list = beta_dist(mu_list, INIT_A, INIT_B)

    line2d, = ax_graph.plot(mu_list, y_list)

    plt.show()


if __name__ == '__main__':
    main()