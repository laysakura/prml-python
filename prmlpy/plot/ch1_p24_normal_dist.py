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
import sys
print(sys.path)

from widgetwrapper.slider import SliderWrapper
from distribution.normal import normal_dist, normal_dist2
import plot


class Plotter:
    _f = None
    _parameters = None

    x_list = np.arange(0.0, 1.0, 0.001)
    y_list = normal_dist(x_list, 0.5, 0.01)

    line2d = None

    def __init__(self, ax_graph, f, parameters):
        Plotter._f = f
        Plotter._parameters = parameters

        Plotter.line2d, = ax_graph.plot(Plotter.x_list, Plotter.y_list)
        for param in Plotter._parameters:
            param['val_from'].get_widget().on_changed(Plotter.update)

    def update(_):
        f_params = {}
        for param in Plotter._parameters:
            f_params[param['name']] = param['val_from'].get_widget().val
        Plotter.y_list = Plotter._f(Plotter.x_list, f_params)
        Plotter.line2d.set_ydata(Plotter.y_list)


INIT_MU = 0.5
INIT_SIGMA = 0.01


def main():
    ax_graph, ax_slider_list = plot.init_figure(n_sliders=2)
    slider_mu = SliderWrapper(axis=ax_slider_list[0], label='mu', min_val=0.0, max_val=1.0, init_val=INIT_MU)
    slider_sigma = SliderWrapper(axis=ax_slider_list[1], label='sigma', min_val=0.01, max_val=0.10, init_val=INIT_SIGMA)

    Plotter(ax_graph, f=normal_dist2, parameters=[{ 'name': 'mu', 'val_from': slider_mu }, {'name': 'sigma', 'val_from': slider_sigma} ])

    plt.show()


if __name__ == '__main__':
    main()
