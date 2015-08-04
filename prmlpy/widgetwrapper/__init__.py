"""
    prmlpy.widgetwrapper
    ~~~~~~~~~~~~~~~~~~~~

    :synopsis: matplotlab.widgets のラッパー。

    matplotlab.widgets のラッパー。
"""


# standard modules

# 3rd party modules

# original modules


class ParamWidgetWrapper:
    """prmlpy.widgetwrapper.* 分布関数のパラメータに紐づくウィジェットの親クラス。
    """

    def __init__(self, param_name, widget):
        """

        :param param_name: 分布関数中のパラメータ名。
        :param widget: ウィジェット
        """
        self._param_name = param_name
        self._widget = widget

    def get_param_name(self):
        """分布関数中のパラメータ名を返却。
        """
        return self._param_name

    def get_widget(self):
        """ウィジェットを取得。
        """
        return self._widget
