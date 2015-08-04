"""
    prmlpy.widgetwrapper.slider
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: matplotlib.widgets.Slider のラッパー。

    matplotlib.widgets.Slider のラッパー。
"""


# standard modules

# 3rd party modules
from matplotlib import widgets as widgets

# original modules


class SliderWrapper:
    """matplotlib.widgets.Slider のラッパー。
    """

    def __init__(self, axis, label, min_val, max_val, init_val):
        """

        :param axis: スライダーバーを配置するaxis。
        :param label:
        :param min_val:
        :param max_val:
        :param init_val: スライダーバーの初期値。
        """
        self._label = label
        self._min_val = min_val
        self._max_val = max_val
        self._init_val = init_val
        # スライダーバーのウィジェットを作成
        self._widget = widgets.Slider(axis, self._label, self._min_val, self._max_val, valinit=self._init_val)

    def get_widget(self):
        """instantiate() されたウィジェットを返却。

        :return:
        """
        return self._widget
