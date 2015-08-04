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


class Plotter:
    """グラフを描画するための情報を登録するクラス。
    """
    _dist_f = None
    _param_widget_wrappers = None
    _x_list = None
    _line2d = None

    @classmethod
    def register(cls, ax_graph, dist_f, param_widget_wrappers, x_list):
        """グラフを描画するための情報を登録。

        :param ax_graph: グラフのaxis。
        :param dist_f: 分布関数。
        :param param_widget_wrappers: 分布関数に渡すパラメータに紐付いた、 ParamWidgetWrapper の子クラスのインスタンス。
        :param x_list: 分布の横軸。
        """
        cls._dist_f = dist_f
        cls._param_widget_wrappers = param_widget_wrappers
        cls._x_list = x_list

        y_list = cls._get_y_list_from_current_param_widgets()  # 初期分布
        cls._line2d, = ax_graph.plot(cls._x_list, y_list)

        for w in param_widget_wrappers:
            w.get_widget().on_changed(cls._update_graph)

    @classmethod
    def _get_y_list_from_current_param_widgets(cls):
        dist_f_params = {w.get_param_name(): w.get_widget().val for w in cls._param_widget_wrappers}
        return Plotter._dist_f(Plotter._x_list, dist_f_params)

    @staticmethod
    def _update_graph(_):
        Plotter._line2d.set_ydata(Plotter._get_y_list_from_current_param_widgets())


INIT_MU = 0.5
INIT_SIGMA = 0.01


def main():
    ax_graph, ax_slider_list = plot.init_figure(n_sliders=2)
    slider_mu = SliderWrapper(
        param_name='mu', axis=ax_slider_list[0], label='mu', min_val=0.0, max_val=1.0, init_val=INIT_MU)
    slider_sigma = SliderWrapper(
        param_name='sigma', axis=ax_slider_list[1], label='sigma', min_val=0.01, max_val=0.10, init_val=INIT_SIGMA)

    x_list = np.arange(0.0, 1.0, 0.001)
    Plotter.register(ax_graph, dist_f=normal_dist, param_widget_wrappers=[slider_mu, slider_sigma], x_list=x_list)

    plt.show()


if __name__ == '__main__':
    main()
