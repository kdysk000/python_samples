# テーブルの作成 (CREATE TABLE)

import MySQLdb
 
# MySQLに接続
conn = MySQLdb.connect(
    host='172.24.87.57',  # 接続先サーバー名（IPアドレス）
    port=3306,          # MySQLのポート番号（デフォルト3306）
    db='sample_db',       # 接続するデータベース名
    user='root',          # ユーザー名
    passwd='secret'       # パスワード
)

# カーソルを取得
cur = conn.cursor()

try:
    # テーブルの作成
    # テーブル名 users
    # +----+--------+-----------+
    # | id | name   | password  |
    # +----+--------+-----------+
    sql = "create table users (id integer primary key auto_increment, name varchar(100), password varchar(100))"
    cur.execute("drop table users")  # 作成前に既存の同名テーブルを削除
    cur.execute(sql)

except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)

# 接続をクローズ
cur.close
conn.close