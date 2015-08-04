"""
    prmlpy.distribution.beta
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: ベータ分布のプロットを出力。

    ベータ分布のプロットを出力。
"""


# standard modules

# 3rd party modules
from scipy.special import gamma

# original modules


def beta_dist(mu_list, params):
    """(2.13) のベータ分布に従い、入力点の集合に対し出力点を返却する。

    :param mu_list: 入力点の集合。一つ一つの値は、p.66で言うところの「表」が出る確率。
    :param params['a']: 超パラメータ。
    :param params['b']: 超パラメータ。
    :return: 出力点の集合。
    """
    a, b = params['a'], params['b']
    return (gamma(a + b) / (gamma(a) * gamma(b))) * (mu_list ** (a - 1)) * ((1 - mu_list) ** (b - 1))
