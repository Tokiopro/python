#クラスの定義

#(object)はなくてもあってもいい。継承でベースクラスで扱う場合はあった方が良い。
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)
    def say_something(self):
        print('hello')


#personというオブジェクトを作ってそこから呼び出す
person = Person()
person.say_something()

#クラスの初期化とクラス変数
