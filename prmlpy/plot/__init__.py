"""
    prmlpy.plot
    ~~~~~~~~~~~

    :synopsis: matplotlib を使った可視化系のプログラム群。

    matplotlib を使った可視化系のプログラム群。実行可能なものが揃っている。
"""

# standard modules

# 3rd party modules
from matplotlib import pyplot as plt
from matplotlib import gridspec

# original modules


MAX_SLIDERS = 10


def init_figure(n_graphs, n_sliders):
    """グラフ領域の横にウィジェットが並ぶ、典型的な図領域を作成する。

    配置は GridSpec ( http://matplotlib.org/users/gridspec.html ) を使用して調整。

    :param n_sliders: グラフ領域のの個数。
    :param n_sliders: スライダーバーの個数。
    :return: (ax_graph, ax_slider_list)
    """
    # グラフ領域
    gs_graph = gridspec.GridSpec(n_graphs, 1)
    gs_graph.update(left=0.05, right=0.70, wspace=0.05)
    ax_graph_list = [plt.subplot(gs_graph[i, :]) for i in range(n_graphs)]

    # スライダーバー領域 (スライダーバーは最大10本まで入る)
    gs_slider = gridspec.GridSpec(MAX_SLIDERS, 1)
    gs_slider.update(left=0.80, right=1.00, wspace=0.05)
    ax_slider_list = [plt.subplot(gs_slider[i, :]) for i in range(n_sliders)]

    return ax_graph_list, ax_slider_list


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


class Plotter3d:
    """3Dグラフを描画するための情報を登録するクラス。
    """
    _ax_graph = None
    _dist_f = None
    _param_widget_wrappers = None
    _x = None
    _y = None
    _im = None

    @classmethod
    def register(cls, ax_graph, dist_f, param_widget_wrappers, x, y, **imshow_kwargs):
        """グラフを描画するための情報を登録。

        :param ax_graph: グラフのaxis。
        :param dist_f: 分布関数。
        :param param_widget_wrappers: 分布関数に渡すパラメータに紐付いた、 ParamWidgetWrapper の子クラスのインスタンス。
        :param x:
        :param y:
        :param **imshow_kwargs: imshow()に渡す引数。
        """
        cls._ax_graph = ax_graph
        cls._dist_f = dist_f
        cls._param_widget_wrappers = param_widget_wrappers
        cls._x, cls._y = x, y

        z = cls._get_z_from_current_param_widgets()  # 初期分布
        cls._im = cls._ax_graph.imshow(z, **imshow_kwargs)
        import pylab
        pylab.colorbar(cls._im, ax=cls._ax_graph)

        for w in param_widget_wrappers:
            w.get_widget().on_changed(cls._update_graph)

    @classmethod
    def _get_z_from_current_param_widgets(cls):
        dist_f_params = {w.get_param_name(): w.get_widget().val for w in cls._param_widget_wrappers}
        return Plotter3d._dist_f(Plotter3d._x, Plotter3d._y, dist_f_params)

    @staticmethod
    def _update_graph(_):
        z = Plotter3d._get_z_from_current_param_widgets()
        Plotter3d._im.set_data(z)
