"""
    prmlpy.plot.ch2_p69_beta_dist
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: ベータ分布の可視化。

    ベータ分布の可視化。
"""


# standard modules

# 3rd party modules
import numpy as np

# original modules
from matplotlib import pyplot as plt
from distribution.beta import beta_dist
from widgetwrapper.slider import SliderWrapper
import plot


INIT_A = 0.01
INIT_B = 0.01


def main():
    ax_graph_list, ax_slider_list = plot.init_figure(n_graphs=1, n_sliders=2)
    slider_a = SliderWrapper(
        param_name='a', axis=ax_slider_list[0], label='a', min_val=0.00, max_val=10.0, init_val=INIT_A)
    slider_b = SliderWrapper(
        param_name='b', axis=ax_slider_list[1], label='b', min_val=0.00, max_val=10.0, init_val=INIT_B)

    mu_list = np.arange(0.0 + 0.001, 1.0 - 0.001, 0.001)
    plot.Plotter.register(
        ax_graph_list[0], dist_f=beta_dist, param_widget_wrappers=[slider_a, slider_b], x_list=mu_list)

    plt.show()


if __name__ == '__main__':
    main()