# from lesson_package.tools import utils
from ..tools import utils#相対パス
# あまりpythonでは推奨されていない。ファイルを追わないといけないから。
def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')