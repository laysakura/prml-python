# prml-python

## 使い方

### Pythonのインストール

[pyenvを使ってMacにPythonの環境を構築する](http://qiita.com/1000ch/items/93841f76ea52551b6a97) などを見てインストール。

Python 3.4.3 を使って動作検証をしている。

### 依存パッケージのインストール

```bash
$ ./setup.py
```

## 単体テスト実行

### テストに必要なパッケージのインストール

```bash
$ ./setup.py test
$ pip install nose  # nosetests コマンドがこうしなきゃ入らない...なぜ...
```

### 実行

```bash
$ nosetests
```
