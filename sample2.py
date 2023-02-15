#セクション6 モジュールとパッケージ
#コマンドライン引数

#コマンドラインで引数を使えるようになる。（ターミナル）
import sys
print(sys.argv)

# ターミナル python3 sample2.py option1 option2
# ['sample2.py', 'option1', 'option2']

# importとas文
# __init__.pyはパッケージを読み込むときに一番初期に読み込まれるファイル。
# これがないとパッケージと認められない。

# import lesson_package.utils
# フルパスは長くなるが、わかりやすい。会社による
# fromで呼び出す方法もある
from lesson_package.tools import utils
# 関数だけを呼び出す方法もある(あまり好まれていない。どこから来ている関数かわからないから）
# また、同じ名前の関数と衝突する。
# from lesson_package.utils import say_twice
# from lesson_package import utils as u ←名前をつけることもできる

r = utils.say_twice('hello')

print(r)

# 自作モジュールをimportした時に作られるpycacheとは？
# よく使うデータへのアクセスを速くするために、より高速な記憶装置に一時的に保存する仕組み

# 絶対パスと相対パスのimport
# 階層が増えたら.で繋げば良い

# from lesson_package.talk import human
# print(human.sing())
# print(human.cry())

# from lesson_package.talk import animal
# print(animal.sing())
# print(animal.cry())

# 同じディレクトリにあるhumanとanimalを読み込むには？
from lesson_package.talk import * #アスタリスクを使う。
# init.pyに定義しに行かないとnameエラーになる。
# あまり推奨されていない。どのモジュールが読込まれているかわかりづらい.

print(animal.sing())
print(animal.cry())
print(human.sing())
print(human.cry())

# importErrorの使い所
# 新しいパッケージでも古いパッケージでもエラーが起きないようにする時に使う。
try:
    from lesson_package import utils# ディレクトリを移動してるのでエラーになる。　古いパッケージはこちら。
except ImportError:
    from lesson_package.tools import utils# 新しいパッケージの場合はこちら。

utils.say_twice('word')

# setup.pyでパッケージ化して配布する。(setup.py)
# from distutils.core import setup

# setup(
#     name='python_programing'
#     version='1.0.0',
#     packages=['lesson_package', 'lesson_package.talk', 'lesson_package.tools'],
#     url='https://tokio_python.appspot.com',
#     license='Free',
#     author='tokio',
#     author_email='',
#     description='sample=package'
#     )

# #どう実行するか？vscodeは知らん！

#組み込み関数について
# import builtins 常にこれがimportされているのと一緒
# builtins.print
#print(globals())

#誰が一番トップか？組み込み関数sortedを使って実装
ranking = {
    'A': 100,
    'B': 85,
    'C': 95,
}

#ランキングのgetをkeyにする。getした値＝100
# 値が高い順にしたいので、reverse=Trueを使う。s
print(sorted(ranking, key=ranking.get, reverse=True))

#標準ライブラリ
#よく使われるライブラリコンテナデータ型

s = 'sjbfvjknjkfsbvlsigrhbi'

d = {}
for c in s:
    if c not in d:#キーがあるか確認
        d[c] = 0#なければ入れる
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)#(cがなければ0を入れるというメソッド)
    d[c] += 1
print(d)

from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

print(d['f'])

#サードパーティーのライブラリ
#setupでまとめたライブラリをpypyリポジトリに上げることができる。
#環境設定
# pip install termcolor
from termcolor import colored

print('test')
print(colored('test', 'green'))

import collections#カンマ区切りはあまり推奨されていない。
import os
import sys
#サードパーティーのパッケージは改行すると良い
import termcolor
#自分で作ったパッケージも改行すると良い
import lesson_package
#ローカルのファイル
import sample
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(sample.__file__)

print(sys.path)
#ローカルのパッケージが優先される。
#標準パッケージやサイドパーティーをローカルに作るとそれが読み込まれる。
#sys.pathが書いていないところにパッケージを置いても読み込まれない。

#__name__,__main__
print(__name__)
