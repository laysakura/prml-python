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
from widgetwrapper import ParamWidgetWrapper


class SliderWrapper(ParamWidgetWrapper):
    """matplotlib.widgets.Slider のラッパー。
    """

    def __init__(self, param_name, axis, label, min_val, max_val, init_val):
        """

        :param param_name: 分布関数中のパラメータ名。
        :param axis: スライダーバーを配置するaxis。
        :param label:
        :param min_val:
        :param max_val:
        :param init_val: スライダーバーの初期値。
        """
        self._min_val = min_val
        self._max_val = max_val
        self._init_val = init_val
        # スライダーバーのウィジェットを作成
        super(SliderWrapper, self).__init__(
            param_name,
            widgets.Slider(axis, label, self._min_val, self._max_val, valinit=self._init_val))
