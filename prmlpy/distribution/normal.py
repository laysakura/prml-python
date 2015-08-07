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


def normal_dist(x_list, params):
    """(1.46) の正規分布に従い、入力点の集合に対し出力点を返却する。

    :param x_list: 入力点の集合。
    :param params['mu']: 正規分布の平均値。
    :param params['sigma']: 正規分布の分散の平方根。
    :return: 出力点の集合。
    """
    mu, sigma = params['mu'], params['sigma']
    return (1.0 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp((-1.0 / (2 * sigma**2)) * (x_list - mu)**2)


def normal_dist_3d(x1, x2, params):
    """(2.43) の正規分布に従い、入力点の集合に対し出力点を返却する。

    次元はD=2で固定。
    共分散行列は、

        |-                -|
    Σ = | σ1 ** 2  σ12     |
        | σ12      σ2 ** 2 |
        |-                -|

    となる。ただし、共分散の性質より、 σ12 == σ21 なことに注意。

    行列式は、
    |Σ| = σ1^2 σ2^2 - σ12^2

    逆行列は、
                     |-          -|
    Σ^(-1) = (1/|Σ|) | σ2^2  -σ12 |
                     | -σ12  σ1^2 |
                     |-          -|

    x = (x1, x2)^T , μ = (μ1, μ2)^T
    とすると、マハラノビス距離は
    (x - μ)^T Σ^(-1) (x - μ) = (1/|Σ|) (σ2^2 x1^2 - 2 σ12^2 x1 x2 + σ1^2 x2^2)
    という風に、成分で書き下せる。

    :param x1: 入力点の集合。numpy.meshgrid() の返り値。
    :param x2: 入力点の集合。numpy.meshgrid() の返り値。
    :param params['mu1']: 正規分布の平均値。x1方向。
    :param params['mu2']: 正規分布の平均値。x2方向。
    :param params['sigma1']: x1方向についての分散。
    :param params['sigma2']: x2方向についての分散。
    :param params['sigma12']: x1,x2方向についての共分散。
    :return: 出力点の集合。
    """
    mu1, mu2 = params['mu1'], params['mu2']
    sigma1, sigma2, sigma12 = params['sigma1'], params['sigma2'], params['sigma12']

    det_sigma = sigma1**2 * sigma2**2 - sigma12**2
    mahalanobis_distance = (
        (1.0 / det_sigma) * (sigma2**2 * (x1 - mu1)**2 - 2 * sigma12**2 * (x1 - mu1) * (x2 - mu2) + sigma1**2 * (x2 - mu2)**2))

    return (
        (1.0 / (2 * np.pi)) * (1.0 / np.sqrt(det_sigma))
        * np.exp(-0.5 * mahalanobis_distance))