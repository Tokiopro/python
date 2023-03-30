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
    def __init__(self, model='Model S', enable_auto_run=False):
        
        super().__init__(model)
    # runメソッドを上書きできる
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