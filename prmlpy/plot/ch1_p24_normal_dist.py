"""
    prmlpy.plot.ch1_p24_normal_dist.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 正規分布の可視化。

    正規分布の可視化。
"""


# standard modules

# 3rd party modules
import numpy as np
from matplotlib import pyplot as plt

# original modules
from prmlpy.distribution.normal import normal_dist


def main():
    x_list = np.arange(0.0, 1.0, 0.001)
    y_list = normal_dist(x_list, 0.5, 0.2)
    plt.plot(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    main()