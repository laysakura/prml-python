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
import pylab

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
    """2D, 3Dグラフを描画するための情報を登録するクラス。

    1つのPlotterオブジェクトは共通のウィジェットを持ち、1つ以上のグラフを描画するというモデル。
    """

    def __init__(self, param_widget_wrappers):
        """グラフ群の共通項目を登録。

        :param param_widget_wrappers: 分布関数に渡すパラメータに紐付いた、 ParamWidgetWrapper の子クラスのインスタンス。
        """
        self._param_widget_wrappers = param_widget_wrappers
        self._graphs_update_info = []  # 描画先axis, 分布関数, 入力点, 更新すべきデータ集合 から成るdictのlist

    def register(self, ax_graph, dist_f, x, y=None, **imshow_kwargs):
        """グラフを1つ描画するための情報を登録。

        :param ax_graph: グラフのaxis。
        :param dist_f: 分布関数。
        :param x:
        :param y: Noneなら2次元グラフ。何かあれば等高線グラフ。
        :param **imshow_kwargs: imshow()に渡す引数。
        """
        def _update_graphs(_):
            """グラフ群の描画を更新する。
            """
            for g in self._graphs_update_info:
                _ax_graph, _dist_f, _x, _y, plot_data = g['ax_graph'], g['dist_f'], g['x'], g['y'], g['plot_data']
                outs = self._get_outputs_from_current_param_widgets(_dist_f, _x, _y)

                if plot_data is None and _y is None:  # 2次元グラフの初期プロット
                    g['plot_data'], = _ax_graph.plot(_x, outs)
                elif plot_data is None and _y is not None:  # 3次元グラフの初期プロット
                    g['plot_data'] = _ax_graph.imshow(outs, **imshow_kwargs)
                elif plot_data is not None and _y is None:  # 2次元グラフの更新
                    plot_data.set_ydata(outs)
                else:  # 3次元グラフの更新
                    plot_data.set_data(outs)

        self._graphs_update_info.append({'ax_graph': ax_graph, 'dist_f': dist_f, 'x': x, 'y': y, 'plot_data': None})
        _update_graphs(None)

        # 3次元グラフの時はカラーバーを表示
        if y is not None:
            g = self._graphs_update_info[-1]
            pylab.colorbar(g['plot_data'], ax=g['ax_graph'])

        for w in self._param_widget_wrappers:
            w.get_widget().on_changed(_update_graphs)

    def _get_outputs_from_current_param_widgets(self, dist_f, x, y):
        """現在のウィジェットの状態をパラメータとし、入力点情報に応じて出力値を返す。

        :param dist_f: 分布関数。
        :param x:
        :param y:
        :return: 出力値。
        """
        dist_f_params = {w.get_param_name(): w.get_widget().val for w in self._param_widget_wrappers}
        if y is None:
            return dist_f(x, dist_f_params)
        else:
            return dist_f(x, y, dist_f_params)
