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

    def __init__(self, widget):
        """

        :param widget: ウィジェット
        """
        self._widget = widget

    def get_widget(self):
        """ウィジェットを取得。
        """
        return self._widget
