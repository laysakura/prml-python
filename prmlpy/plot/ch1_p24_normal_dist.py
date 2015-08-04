"""
    prmlpy.plot.ch1_p24_normal_dist
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 正規分布の可視化。

    正規分布の可視化。
"""


# standard modules

# 3rd party modules
from matplotlib import pyplot as plt
import numpy as np

# original modules
from widgetwrapper.slider import SliderWrapper
from distribution.normal import normal_dist
import plot


INIT_MU = 0.5
INIT_SIGMA = 0.01


def main():
    ax_graph, ax_slider_list = plot.init_figure(n_sliders=2)
    slider_mu = SliderWrapper(
        param_name='mu', axis=ax_slider_list[0], label='mu', min_val=0.0, max_val=1.0, init_val=INIT_MU)
    slider_sigma = SliderWrapper(
        param_name='sigma', axis=ax_slider_list[1], label='sigma', min_val=0.01, max_val=0.10, init_val=INIT_SIGMA)

    x_list = np.arange(0.0, 1.0, 0.001)
    plot.Plotter.register(ax_graph, dist_f=normal_dist, param_widget_wrappers=[slider_mu, slider_sigma], x_list=x_list)

    plt.show()


if __name__ == '__main__':
    main()
