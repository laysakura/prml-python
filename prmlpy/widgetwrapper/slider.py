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

        同名のインスタンス変数にアクセス可能。

        :param param_name: 分布関数中のパラメータ名。
        :param axis: スライダーバーを配置するaxis。
        :param label:
        :param min_val:
        :param max_val:
        :param init_val: スライダーバーの初期値。
        """
        self.param_name = param_name
        self.axis = axis
        self.label = label
        self.min_val = min_val
        self.max_val = max_val
        self.init_val = init_val

        self._text = None  # スライダーバー内のテキスト

        # スライダーバーのウィジェットを作成
        super(SliderWrapper, self).__init__(
            widgets.Slider(axis, label, self.min_val, self.max_val, valinit=self.init_val, color='aqua'))

    def update_text(self, s):
        """スライダーバーにテキストを表示する。
        """
        if self._text:
            self._text.remove()
        self._text = self.axis.text(self.min_val, 0, s)
