#ファイルの作成
#wをaに変えると中の文字に追加できる(append)
f = open('text.txt', 'w')
#テキストファイルの中に文字列を記述する
f.write('Test')
f.close()

#withステートメントでファイルをクローズする。

with open('text.txt', 'w') as f:
#テキストファイルの中に文字列を記述する
    f.write('Test\n')
#f.close()がいらなくなる
#withを使う方が推奨されている

with open('test.txt', 'r') as f:
    while True:
        #一行だけ読み込む
        line = f.readline()
        #チャンクを使って読み出すこともできる。
        #2文字ずつ読み込む
        #チャンクはネットワークのパケットを読み込むときなどにも使う。
        chunk = 2
        line = f.read(chunk)
        print(line, end='')
        if not line:
            break
        
#seakを使って移動する、あまり使わない

#書き込み、読み込みモード
# w+書き込み＋読み込み
# r+読み込み＋書き込み　事前にファイルがないとエラーになる。
with open('test.txt', 'w+') as f:
    f.write(f.read())

