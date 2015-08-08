"""
    prmlpy.plot.ch2_p76_normal_dist_3d
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 2次元のガウス分布の等高線描画。
"""


# standard modules

# 3rd party modules
from matplotlib import pyplot as plt
import numpy as np

# original modules
from distribution.normal import normal_dist_3d
from widgetwrapper.slider import SliderWrapper
import plot


def main():
    ax_graph_list, ax_slider_list = plot.init_figure(n_graphs=1, n_sliders=5)

    slider_mu1 = SliderWrapper(
        param_name='mu1', axis=ax_slider_list[0], label='mu1', min_val=-1.0, max_val=1.0, init_val=0.0)
    slider_mu2 = SliderWrapper(
        param_name='mu2', axis=ax_slider_list[1], label='mu2', min_val=-1.0, max_val=1.0, init_val=0.0)
    slider_sigma1 = SliderWrapper(
        param_name='sigma1', axis=ax_slider_list[2], label='sigma1', min_val=0.1, max_val=2.0, init_val=1.0)
    slider_sigma2 = SliderWrapper(
        param_name='sigma2', axis=ax_slider_list[3], label='sigma2', min_val=0.1, max_val=2.0, init_val=1.0)
    slider_sigma12 = SliderWrapper(
        param_name='sigma12', axis=ax_slider_list[4], label='sigma12', min_val=-2.0, max_val=2.0, init_val=-0.8)

    _x = np.arange(-1.0, 1.0, 0.01)
    _y = np.arange(-1.0, 1.0, 0.01)
    x, y = np.meshgrid(_x, _y)

    plotter = plot.Plotter(param_widget_wrappers=[slider_mu1, slider_mu2, slider_sigma1, slider_sigma2, slider_sigma12])
    plotter.register(
        ax_graph_list[0], dist_f=normal_dist_3d, x=x, y=y, extent=[-1.0, 1.0, -1.0, 1.0])
    plt.show()

if __name__ == '__main__':
    main()
