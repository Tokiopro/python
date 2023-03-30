#クラスの定義

#(object)はなくてもあってもいい。継承でベースクラスで扱う場合はあった方が良い。
class Person(object):
    #初期化↓コンストラクタという。
    def __init__(self, name):
        #プロパティの前にselfがないと値が保持されない
        #selfは自分自身（インスタンス自信）
        self.name = name
        print(self.name)
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        #自分自身の他のメソッドも呼ぶことができる。
        self.run()

    def run(self):
        print('run')

    #クラスのコンストラクタとデストラクタ

    #デストラクタ
    def __del__(self):
        print('good bye')


#personというオブジェクトを作ってそこから呼び出す
#引数を与えないと、nameという引数に値が入らないのでエラーになる。
person = Person('Mike')
person.say_something()
del person

#クラスの初期化とクラス変数

#クラスの継承

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(serf):
        print('run')

#Carクラスを継承している。
class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        #上記のCarクラスの__init__に上書きしている
        # self.model = model
        #これを避けるために、親クラスの要請というものがある。
        #親クラスの初期化を呼び出し、変数モデルを格納している。
        #superは親への要請。親のメソッドを呼び出す。
        super().__init__(model)
        #プロパティを使用してオートランをTrueにさせないようにする。
        #変数の前に_を置いて、外から見えないようにする。
        self._enable_auto_run=enable_auto_run
        self.passwd = passwd
        # アンダースコアが二個の場合は？
        # 完全に隠すことができる
        # クラスの中からはアクセスできる。クラスを生成してからアクセスはできない。
        # 明示的に書き換えないでほしい時にアンダースコアは使用する。
        
    #プロパティがつくと、()で呼び出すのではなく、クラス変数として扱われるので、.で呼び出す。
    @property#デコレータを使って読み込みはできるけど、設定はできなくなる。
    def enable_auto_run(self):
        return self._enable_auto_run
    
    #setterを使用して設定できるようにする。
    #propertyがついている変数名をつける
    #使用するときはある条件が合致した時だけ。セッター、ゲッターを使用する。
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
        
    # runメソッドを上書きできるs
    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

car = Car()
car.run()

toyota_car = ToyotaCar()
#Carクラスを継承しているのでrunを呼び出せる。
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

#メソッドのオーバーライド
#上書きする,carクラスにinitでmodelのインスタンスを作成
toyota_car = ToyotaCar('Lexus')
#クラス変数は.で呼び出せる。
print(toyota_car.model)
print(toyota_car.run())

tesla_car = TeslaCar('Models S', passwd='111')
print(tesla_car.enable_auto_run)

# クラスを構造体として扱うときの注意点

class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

#クラスを生成してから、後から自分で値を入れるとバグが発生しやすい
#アンダースコアを二個つけていても、後から追加できる、アクセスできてしまう。新しい変数を作成してしまうから。

# ダックタイピング

