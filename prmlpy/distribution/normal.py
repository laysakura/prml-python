"""
    prmlpy.distribution.normal
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 正規分布のプロットを出力。

    正規分布のプロットを出力。
"""


# standard modules

# 3rd party modules
import numpy as np

# original modules


def normal_dist(x_list, mu, sigma):
    """
    (1.46) の正規分布に従い、入力点の集合に対し出力点を返却する。

    :param x_list: 入力点の集合。
    :param mu: 正規分布の平均値。
    :param sigma: 正規分布の分散の平方根。
    :return: 出力点の集合。
    """
    y_list = (1.0 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp((-1.0 / (2 * sigma**2)) * (x_list - mu)**2)
    return y_list
