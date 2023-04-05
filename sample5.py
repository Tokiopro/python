# try:
#     int_a = int(input('整数a:'))
#     int_b = int(input('整数b:'))
#     print(int_a ** 2)
#     print((int_a ** 2) / int_b)
# except(ValueError) as v:
#     print(type(v))
#     print('C')
# except(ZeroDivisionError) :
#     print('D')
# except:
#     print('E')
# else:
#     print('F')
# finally:
#     print('G')
    
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    print(user)
    print(status)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
    print(user)
    print(status)
    
    
#多重継承
class Person(object):
    def talk(self):
        print('talk')
        
class Car(object):
    def run(self):
        print('run')
        
# person,carクラスを継承している。
#左側に入れたものが優先される。なるべくない方が良い（混乱、バグを生み出す）
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')
        
#クラス変数
#クラス変数は全てのオブジェクトで共有される。
class Person(object):
    
    kind = 'human'
    def __init__(self, name):
        self.name = name
    
    def who_are_you(self):
        print(self.name, self.kind)
        
class T(object):
    words = []
    
    def add_word(self, word):
        self.words.append(word)
        
c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)
# cのリストも共有されてしまう。    

#クラスメソッドとスタティックメソッド
class Person(object):
    
    kind = 'human'
    
    def __init__(self):
        self.x = 100
        
    #インスタンスが作成されていなくても
    @classmethod
    #clsを引数に取る必要がある（クラス）
    def what_is_your_kind(cls):
        return cls.kind
    
    #スタティック
    @staticmethod
    def about(year):
        print('about human {}'.format(year))

#オブジェクトとして呼び出すのでinitが実行されている
#インスタンスを作成している
a=Person()

#クラスとして呼び出しているので、initは実行されない、ただし、kindのクラス変数は呼び出せる。
#クラスを参照しているだけ
b=Person

#特殊メソッド、前後にアンダースコアが二つついているもの。
class Word(object):
    
    def __init__(self, text):
        self.text = text
    
    #一番よく使われる特殊メソッド
    def __str__(self):
        return 'word'
    
    #テキストの長さを返す
    def __len__(self):
        return len(self.text)
    #Word.text + word.text2と本来ならしなければいけない
    # クラスを足し合わせるだけでよい
    def __add__(self, word):
        return self.text.lower() + word.text.lower()
    
    def __eq__(self, word: object) -> bool:
        return self.text.lower() == word.text.lower()
    
w = Word('test')
w2 = Word('test')
print(w + w2)

#文字列として呼ばれたときにstrで定義されている文字が呼び出される。
print(w)

#特殊メソッドeqをコメントアウトするとFalseになる。オブジェクトのidが違うため。
print(w == w2)
        
