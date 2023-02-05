# リスト型=配列
l = [1, 20, 30, 40, 5, 8, 90]

print(l[0])
# 後ろから取ってくることもできる
list = l[-1]
# 2番目から5番目まで(2,3,4)
print(l[2:5])
# 省略できる [:2]0から2番目まで、[2:]2番目から最後まで
print(l[:2])
print(l[2:])
print(l[::2])
print(l[::-1])
# [::2]ふたつ飛ばしで取得、[::-1]後ろから取得

# リストの操作
# 指定して代入できる。
l[0] = 'x'
l[2:5] = ['c', 'd', 'e']

#空の配列を入れたい場合は、[]を代入するだけ。全部をからにする場合は[:] = []
#append=一番最後に値を追加
#insert(要素数、値)で位代入できる
#pop＝取り出して削除
#del=存在こと削除してしまう
#remove=指定した値を消すことができるremove('x')

#配列を結合するとき a += b
#a.extend(b)というメソッドでも結合できる。

r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
#index(3)だと、インデックス番号を探してくれる。
print(r.index(3,3))
#カンマをつけると、一つ目の数字のインデックス番号移行を検索
#count=要素数を数える

#配列に5は存在するか？
if 5 in r:
    print('exist')
    
#並び替え、reverse=Trueを入れると逆順
r.sort()
r.sort(reverse=True)
#もう一度reverseすると元に戻る
r.reverse()
print(r)

#文字を単語ごとに要素分けして配列に入れる場合
s = 'My name is Mike.'
to_split = s.split('!!')#空白を入れて、要素わけする。存在しない文字列にした場合と全てを一つの要素として配列にしてしまう。
#空白はバリューエラー
print(to_split)

#joinは代入して結合する
x = ' a '.join(to_split)
print(x)

i = [1,2,3]
j = i
j[0] = 100
#この場合、iも入れ替わってしまう。
#なぜ？メモリーに保存してるiのアドレスをjに入れているから（参照渡し）
#リストやディクショナリーは参照渡し、数値などは値わたしなのでコピーする必要はない。

#どう避けるか？コピーを使う。
j = i.copy()
#または[:]を使っても同じことができる。可読性を考慮するとコピーを使った方が良い。

#リストの使い所
#乗客が乗降するタクシー、5人までしか乗れない
seat = []
min = 0
max = 5
check = min <= len(seat) < max
#一人のる
seat.append('p')
print(seat)
print(check)
#一人降りる
seat.pop(0)

#要素数が変動するものに対して論理和などでチェックするという使い方・

#タプル型 ()の中にある配列
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#リストとタプルの違いは？
#リストはブランケットの鉤括弧[]
#タプルはパレンティスの丸括弧()
#タプルはt[0] = 100 などの代入ができない
#使用する場面、ケースとしては、値を代入したら後から変更されたくない、読み込み専用とするときに使われる場合が多い。

#indexなどの読み込み操作などはできる。t[0] = [1]のような代入はできない
#help(tuple)でみるとわかる。
t.index(1)

#タプルは,をつけた時点でタプルになる。t, でもタプルになる。バグの原因になりやすい。
#t=(1)とするとintegerになってしまう。t = (1,)としなければならない。（一つだけのタプルはあまりない）
#タプルにネストしたリストを入れることはできる。
t2 = ([1, 2, 3], [4, 5, 6])

#タプル同士は足すことができる。
new_tuple = (1, 2, 3) + (4, 5, 6)

#タプルのアンパッキング
num_tuple = (10, 20)
print(num_tuple)#(10, 20)

x, y = num_tuple#カンマで区切れば、アンパッキングできる
print(x, y)#10,20

x, y = 10, 20#pythonの中身的には、タプルを作って展開している、ということになる。
print(x, y)

min, max = 0, 100
print(min, max)
#↑のような定義は長いと冗長的になるので、良くない・

#アンパッキングを利用しえて数字の入れ替えができる。
a = 100
b = 200
print(a, b)#100, 200
a, b = b, a#入れ換えている
print(a, b)

#タプルの使い所
#ユーザーが選択肢の中から二つ選ぶ
chose_from_two = ('A', 'B', 'C')

answer = []#answerはリストで定義
answer.append('A')
answer.append('C')

print(chose_from_two)#('A', 'B', 'C')
print(answer)#['A', 'C']

#良くないパターン

bad_chose_from_two = ['A', 'B', 'C']#タプルではなくリストで定義

bad_answer = []#answerはリストで定義
bad_chose_from_two.append('A')#間違って開発者が選択肢に答えを入れてしまう。
bad_chose_from_two.append('C')#タプルにappendは使えないので、バグが発生する。

print(chose_from_two)#['A', 'B', 'C', 'A', 'C']
print(answer)#['A', 'C']
#タプルで宣言した中身は書き換えられないので、バグの発生率を抑えることができる。]

#辞書型（ディクショナリー、dict)
d = { 'x': 10, 'y': 20 }
d['x']#keyを鉤括弧で指定すると値にアクセスできる
#→10
d['x'] = 100#xに値を代入
d['z'] = 200#新しく追加
d[1] = 10000#追加

#他の辞書の作り方
dict(a=10, b=20)
#tupleを使う,配列の中に辞書を作っている。
dict([('a', 10), ('b', 20)])

#辞書型のメソッド

test = {'x': 10, 'y': 20}
# help(test)

test.keys()
test.values()

#他の辞書型で辞書をアップデートさせたいとき
test2 = {'x': 1000, 'j': 500}
#updateメソッドを使う
test.update(test2)
print(test)
#{'x': 1000, 'y': 20, 'j': 500}

#辞書型の中身はdict['key']という方法もあるが、getメソッドを使ってアクセスすることもできる。
#何が違うか？
#dict['key']で存在しないものにアクセスするとエラーが発生する。
#getメソッドで存在しないものにアクセスするとNoneTypeというものが返してくる。
print(test.get('z'))#None
#取り除くメソッドpop
test.pop('x')#{'y': 20, 'j': 500}

#削除するメソッドdel
del test['y']#yを削除
print(test)#{'j': 500}
#変数自体を消してしまうとエラーが起きてしまう。
#del test#NameError: name 'test' is not defined
#辞書を空にするには？

test.clear()#{}
print(test)

#特定のキーが入っているかどうか？
test = {'a': 100, 'b': 200 }
print(test)
print('a' in test)#testという辞書の中にaというキーは入っているか？
#Trueと返ってくる。ない場合はFalse

#辞書のコピー
#リストと同様、下の場合は参照渡しになってしまい、xの'a'の値も変更されてしまう。
x = {'a': 1 }
y = x
y['a'] = 1000
print(x)
print(y)
#{'a': 1000}
#{'a': 1000}

#コピーメソッドを使う
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
#{'a': 1}
#{'a': 1000}

#辞書型の使い所
#果物を売るオンラインサイト

fluits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fluits['apple'])

#リストでも定義できるが、リストは検索に時間がかかる。
#appleを取り出したい時、一番最初からリストのどこにappleがあるか探しに行く処理を書かなければならない。
l= [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]

#辞書型はハッシュテーブルというものを用いているので、検索スピードが早い。プログラムの中身的な違い。

#集合型
a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
#<class 'set'>
b = {2, 3, 3, 6, 7}

#集合の論理和
print(a - b)#{1, 4, 5}
print(b - a)#{7}
print(a & b)#{2, 3, 6}
#aまたはb
print(a | b)#{1, 2, 3, 4, 5, 6, 7}
#aの排他のb　どちらかにあるが重複はしていない
print(a ^ b)#{1, 4, 5, 7}

#集合のメソッド
s = {1, 2, 3, 4, 5}
#集合には並びがない、インデックスがないのでs[0]としてもエラーになる。
s.add(6)#６を入れるメソッド
s.remove(6)#６を削除するメソッド
s.clear()#sの中身を空にするメソッド
print(s)#set()パレンティスの形で返ってくる（）という形
#a = {}とするとdict型になる

#集合の使い所
#共通の友達を見つける。

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)#D

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)#リストから集合型に型を変換してどんな種類の果物を買ったのか？
print(kind)

"""
制御フローとコード構造（セクション5)
"""

#コメント
"""
この中にコメントできる
この中にコメントできる
この中にコメントできる
この中にコメントできる
"""
#ここにもコメントできる。ただし、pythonの暗黙のルールとして
#変数の横ではなく、上にコメントする。

#1行が長くなる時
#pythonは80文字以上になると次の行に改行するべきというルールがある。
# バックスラッシュつけると改行できる。
x = 1+1+1+1+1+1+1+1\
    +1+1+1+1+1+1+1

#またパレンティスの丸括弧でも改行できる
y = (1+1+1+1+1+1+1+1
    +1+1+1+1+1+1+1)

#if文
x = 10
if x < 0:
    print('negative')#pythonはインデントで次の行に行く（スペースは4つが好ましい）
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0:#pythonはインデントを綺麗に合わせないとエラーが起きてしまう。
        print('b is positive')

#比較演算子と論理演算子
a == b
a != b
a < b
a <= b
a >= b

# aもbも真であれば真
if a > 0:
    if b > 0:
        print('a and b are positive')
        
#andを使って行数を減らす↓
        
if a > 0 and b > 0:
    print('a and b are positive')
    
    
#aまたはbが真であれば真
if a > 0 or b > 0:
    print('a or b is positive')

#inとnotの使い所
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

if not a == b:
    print('not equal')

if a < b:
    print('not equal')
    
#notはいつ使うのか？

is_ok = True
# ==や!= などの等号を使う必要がない。
if not is_ok:
    print('hello')
    
#値が入っていない判定をするテクニック
is_ok = 0#False
is_ok = 1#True
#値が入っていればtrue
#空のリストはFalseになる。
# False, 0, 0.0, [], {}, (), set()
if is_ok:
    print('ok!')
else:
    print('No!')
    
#Noneを判定する場合
#pythonはnullをNoneという。
is_empty = None
#print(help (is_empty))

#is_empty is None=これはNoneですか？という時に使う（＝＝はおすすめされていない)
if is_empty is not None:#Noneではない
    print('Not None!!!')
    
print(1 == True)
print(1 is True)#Falseになる.オブジェクトが一緒でなければならない。

#基本的にNoneかどうか判定するときにisを使う。

#while文とcontinue文とbreak文

count = 0
# while count < 5:
#     print(count)
#     count += 1#これがないと無限ループになってしまう
# #0 1 2 3 4

# while True:
#     if count >= 5:
#         break

#     if count == 2:
#         count +=1
#         continue#0 1 3 4 2のときはスキップする。
    
#     print(count)
#     count += 1
    
#while else文

while count < 5:
    if count == 1:
        break#完全にループから抜けるのでdoneは表示されない　0だけ
    print(count)
    count += 1
else:
    print('done')

#input関数

# while True:
#     word = input('Enter:')#コンソール上で入力を求める。
#     if word == 'ok':#okじゃなければループ
#         break
#     print('next')
    
#integerにしたい場合
# while True:
#     word = input('Enter:')
#     num = int(word)#integer型に変換
#     if num == 100:
#         break
#     print('next')
    
#for文とbreak文とcontinue文
some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):#iがsme_listの要素数より少ない時
    print(some_list[i])
    i += 1
    
#forループはin演算子をつかってiterator(反復処理をするもの)をinで入れて行って全部回せる。
for i in some_list:#1, 2, 3, 4, 5
    print(i)
    
for s in 'abcde':
    print(s)#a b c d e
    
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)
    
#for else文
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break#elseも実行されない。
    print(fruit)
else:
    print('I ate all')
    
#range関数
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i  in num_list:
    print(i)

#いちいちリストを作るのは面倒臭い
#range関数で0から9まで作ってくれるrange(10)

for i in range(2, 10, 3):#2~9で3個飛ばし 2, 5, 8
    print(i)

for _ in range(10):#iを使う必要がない場合（＿）を使う・
    print('hello')

#enumerate関数
#forで回すときにインデックスを表示する場合は？
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i,fruit)
    i += 1#これでもできる
    
for i, fruit in enumerate(['apple', 'banana', 'orange']):#enumerateがイテレーターをそれぞれに入れてくれる。
    print(i,fruit)
    
#zip関数
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruit[i], drinks[i])
    
#もっと簡単に書くことができる。zip関数
#indexを指定する必要がなくなる
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
    
#辞書をfor文で処理をする
d = {'x': 100, 'y': 200}
print(d.items())#dict_items([('x', 100), ('y', 200)])リストの中にキーとバリューのtupleがある
#tupleのアンパッキングを利用して、キーとバリューをk, vに入れている。よく使われるメソッド
for k, v in d.items():
    print(k, ':', v)#x : 100 y : 200

#関数定義
def say_something():
    print('hi')
    
print(say_something)#pythonは順次処理なので、関数を呼び出す前に関数が定義されている必要がある。
type(say_something)#<function say_something at 0x1055391f0>　functionという型
f = say_something
f()

#関数の返り値、戻り値
def said_something():
    s = 'hi'
    return s#returnで返す。
    
result = said_something()#resultにhiが入ってくる。
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"
    
result = what_is_this('red')
print(result)

#関数は何度も同じコードを呼び出すものにする。
#ifを何度も呼び出したい時。

num: int = 10#型を一応宣言できる。
#今の所このような書き方はされていないが、一応できる。

def add_num(a: int,b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)#30
#文字列を入れた場合は？

r = add_num('a', 'b')
print(r)#ab
#関数が実行されてしまう。pythonは型を宣言して、間違った型が入ってきてもエラーでは返してくれない

#位置引数とキーワード引数とデフォルト引数
# def menu(entree, drink, dessert):
#     print(entree)
#     print(drink)
#     print(dessert)
    
# menu('beef', 'beer', 'ice')#順番通りに出力される。
#わかりやすく書くには？
#キーワード引数を使う。

# def menu(entree, drink, dessert):
#     print('entree = ', entree)
#     print('drink = ',drink)
#     print('entree = ', dessert)
    
# menu(entree='beef', dessert='ice', drink='beer')
#entree =  beef
#drink =  beer
#entree =  ice
#menu(dessert='ice', 'beef', drink='beer')←この場合だと動かない
#位置引数とキーワード引数が衝突し、pythonが判断できない
#drinkにbeerがキーワード引数で入れられているが、位置引数的にはbeefだから。

#デフォルト引数
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ',drink)
    print('entree = ', dessert)
    
menu(entree='chicken', drink='beer')#上書きされる。desertはiceのまま
# entree =  chicken
# drink =  beer
# entree =  ice

#デフォルト引数で気をつけること
def test_func(x, l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

#注意点
#もう一度実行するとどうなる？
r = test_func(100)
print(r)#[100, 100]となる。
#リストのアドレスを参照して試合。一回目に呼び出された時のl.append(x)

#リストはデフォルト引数で与えるべきではない、バグにつながる。

#空のリストをデフォルト値と定義したい場合、
#pythonでどう記述する？

def test_func2(x, l=None):
    if l is None:#Noneの時にからのリストを返す。
        l =[]
    l.append(x)
    return l

r = test_func2(100)
r = test_func2(100)
print(r)#[100]

#位置引数のタプル化

#引数が多数あるときに*argsとすることで引数をまとめて受け取れる。
def say_something(*args):
    print(args)#('Hi!', 'Mike', 'Nance')
    
say_something('Hi!', 'Mike', 'Nancy')

def say_something(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)
        
say_something('Hi!', 'Mike', 'Nancy')
# word =  Hi!
# Mike
# Nance
t = ('mike', 'Nancy')
say_something('Hi!', *t)
#自分でタプルを作って、展開する記法
#タプルをアンパッキングして、*argsでまたタプル化して入れて展開。
#あまり使われない。

#キーワード引数に辞書化

#**kwargs=keyword argumentsの略称
#辞書型で受け取る。(辞書化する)
def menu(**kwargs):
    for k, v in kwargs.items():#keyとvalueを扱える。
        print(k, v)
        
#dict(辞書型)を定義
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice',
}
menu(**d)#アスタリスクをつけることで、辞書が展開されて渡される。
#アスタリスクをつけない場合はエラーTypeError: menu() takes 0 positional arguments but 1 was given

#**はアプリケーション開発でよく見られる

#位置引数とタプル化と辞書化はまとめてできる。

def menu(food, *args, **kwargs):#def menu(food, **kwargs, *args):と順序を入れ替えるとエラーになる。
    print(food)
    print(args)
    print(kwargs)
    
menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

# banana food
# ('apple', 'orange') *args
# {'entree': 'beef', 'drink': 'coffee'} **kwargs

#Docstring

#print(function, __doc__)#docstringをprintで見ることができる。

#関数内関数
#定義する場合＝その関数の中だけで使う関数(インナー関数)

def outer(a, b):
    def plus(c, d):#この関数(outer)の中だけで使う関数(plus)
        return c + d
    
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)
    
outer(1, 2)#6
