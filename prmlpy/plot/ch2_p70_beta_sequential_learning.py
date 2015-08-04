"""
    prmlpy.plot.ch2_p70_sequential_learning
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: 二項分布の逐次学習。

    「表」が出る真の確率(学習される対象) μ を REAL_MU として、この確率に従って、歪んだコインをD回トスする。

    事後分布 p(μ|D) は、事前分布 p(μ) と尤度関数 p(D|μ) の積に比例する。
    p(D|μ) が (2.9) の二項分布で与えられるので、 p(μ) は共役性を持ったベータ分布を仮定する。
    そうすると、 p(μ|D) は (2.18) のように、 p(μ|m, l, a, b) の形で与えられる。
    ただし、m, l はそれぞれ「表」と「裏」の出た回数で、 a, b は超パラメータ。

    得られた p(μ|m, l, a, b) を、D+1回目のイテレーションにおける事前分布と捉え直し、同一の処理を行う。
    これを繰り返すと、p(μ) が μ = REAL_MU を mode として徐々に鋭いピークを持つようになる。
"""


# standard modules
from random import random

# 3rd party modules
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.special import gamma

# original modules
import plot


REAL_MU = 0.20
MAX_D = 150    # ガンマ関数は「一般化した階乗」と呼ばれるだけあって、イテレーションを増やすとすぐに gamma(m + a + l + b) がオーバーフローを起こす


if __name__ == '__main__':
    #ax_graph, _ = plot.init_figure(n_sliders=0)
    fig = plt.figure()

    # [TODO] - a, b をスライダーバーで調整してから、ボタンを押すとイテレーション開始
    a = 8
    b = 6
    m = l = 0

    mu_list = np.arange(0.0, 1.0, 0.001)
    prior_dist = np.repeat([1.0], 1000)   # p(μ) の最初の予想。一様分布。

    frame_list = []

    for D in range(1, MAX_D):
        is_face = random() < REAL_MU  # 「表」が出たらTrue
        if is_face:
            m += 1
        else:
            l += 1

        frame_list.append(plt.plot(mu_list, prior_dist))

        posterior_dist = (gamma(m + a + l + b) / (gamma(m + a) * gamma(l + b))) * (mu_list ** (m + a - 1)) * ((1 - mu_list) ** (l + b - 1)) # (2.18)
        prior_dist = posterior_dist

    animation.ArtistAnimation(fig, frame_list, interval= 10, repeat_delay=2000)
    plt.show()
