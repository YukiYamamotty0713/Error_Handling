import traceback
import subprocess
import sys
import datetime

try:
    # ここにメインの処理を記述
    # エラーを発生させる例外の発生
    x = 10
    y = 'hello'
    x+y
except Exception as e:
    # エラーが発生した場合の処理
    error_type = type(e).__name__  # エラータイプを取得
    error_message = str(e)  # エラーメッセージを取得
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # タイムスタンプを取得
    error_traceback = traceback.format_exc()  # エラーのトレースバック情報を取得

    # エラーデータを logging_error.py に渡す
    subprocess.run(["python", "logging_error.py", error_type, error_message, timestamp, error_traceback])
