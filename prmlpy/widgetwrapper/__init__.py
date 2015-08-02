"""
    prmlpy.widgetwrapper
    ~~~~~~~~~~~~~~~~~~~~

    :synopsis: matplotlab.widgets のラッパー。

    matplotlib.widgets.Slider() などを呼び出すと、現在の subplot においてもう描画が始まってしまう。
    むしろ、以下の流れを実現したいので、このラッパーを作った。

    #. ラベルや最大値最小値などの基礎的な項目を widgetwrapper にて設定。
    #. figure内の配置を担当する関数に、 widgetwrapper のリストを渡す。
    #. figure内の配置を担当する関数が、適切に描画。
"""


# standard modules

# 3rd party modules

# original modules
