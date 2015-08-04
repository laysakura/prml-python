# prml-python

![ガンマ分布のパラメータをリアルタイムで変更](/doc/screenshot/ch1_p24_normal_dist.gif?raw=true)
_ガンマ分布のパラメータをリアルタイムで変更_

![二項分布の逐次学習](/doc/screenshot/ch2_p70_sequential_learning.gif?raw=true)
_二項分布の逐次学習_


## 使い方

### 動作検証環境

|        |                    |
|--------|--------------------|
| OS     | Mac OS X Marverics |
| Python | Python 3.4.3       |


### Pythonのインストール

[pyenvを使ってMacにPythonの環境を構築する](http://qiita.com/1000ch/items/93841f76ea52551b6a97) などを見てインストール。

```bash
$ python --version
```

で所望のバージョンがインストールされていることの確認。

### 依存パッケージのインストール

```bash
$ pip install scipy  # scipyは、setup.py に書くだけじゃうまくインストールできない。。
$ ./setup.py install
```

### matplotlib の設定

[Python 3.3でmatplitlibとpylabを使おうとしたら...](http://qiita.com/katryo/items/918667f28301fdec89ba) を読み、 `~/.matplotlib/matplotlibrc` の `backend` を `TkAgg` に変更。
これをしないと、グラフが表示されなかった。

### 動作検証

```bash
$ PYTHONPATH=prmlpy python prmlpy/plot/ch1_p24_normal_dist.py
```

グラフが表示されればOK。


## 可視化サンプルの動かし方

```bash
$ PYTHONPATH=prmlpy python prmlpy/plot/foobar.py
```

または

```bash
$ python -m prmlpy.plot.foobar
```

立ち上がった画面でスライダーバーとか動かして遊ぶ。
