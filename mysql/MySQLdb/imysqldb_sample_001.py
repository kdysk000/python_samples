# レコードの取得 (SELECT)

import MySQLdb
 
# MySQLに接続
conn = MySQLdb.connect(
    host='172.24.87.57',  # 接続先サーバー名（IPアドレス）
    port=3306,          # MySQLのポート番号（デフォルト3306）
    db='sample_db',       # 接続するデータベース名
    user='root',          # ユーザー名
    passwd='secret'       # パスワード
)

# テーブル名 users
# +----+-------------+-----------+
# | id | user_name   | password  |
# +----+-------------+-----------+

# カーソルを取得
cur = conn.cursor()

try:
    # SQL文を実行
    sql = "select * from users"
    cur.execute(sql)

    # 取得したレコードを1行ずつ表示
    for row in cur.fetchall():
        print(row)

except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)

# 接続をクローズ
cur.close
conn.close