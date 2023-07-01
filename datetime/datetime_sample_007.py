# 日時を指定したフォーマットで文字列に変換 (datetime.strftime)
# 戻り値は文字列
#
# %a：ロケールの曜日名を省略形で表示
# %A：ロケールの曜日名を表示
# %b：ロケールの月名を省略形で表示
# %B：ロケールの月名を表示
# %c：ロケールの適切な日付および時刻の表示
# %d：10進数で月の始めから何日目かを表示
# %f：10進数でマイクロ秒を表示
# %G：ISO weekの内過半数を含んだ西暦表記のISO 8601 year
# %H：10進数で24時間計での時を表示
# %I：10進数で12時間計での時を表示
# %j：10進数で年の初めから何日目かを表示
# %m：10進数で月を表示
# %M：10進数で分を表示
# %p：ロケールのAM・PMに対応する文字列
# %S：10進数で秒を表示
# %u：月曜日を1とする10進数表記のISO 8601 weekday
# %U：10進数で年の初めから何週目かを表示。年明けから最初の日曜日までの全ての曜日は0週目
# %w：曜日を10進表記した文字列を表示。表示は日曜日が0・土曜日が6
# %W：10進数で年の初めから何週目かを表示。年明けから最初の月曜日までの全ての曜日は0週目
# %x：ロケールの適切な日付を表示
# %X：ロケールの適切な時刻を表示
# %y：10進数で上2桁のない西暦年を表示
# %Y：10進数で上2桁が付いている西暦年を表示
# %Z：タイムゾーン名。タイムゾーンがない場合は空文字列

import datetime

today = datetime.datetime.now()

print(today.strftime('%Y–%m–%d %H:%M:%S'))
print(today.strftime('%A,%B %d,%Y'))


# 実行結果
# 2023-07-03 16:56:16.663788
# 2023-06-29 16:56:16.663788
# 2023-07-03
# 2023-06-29