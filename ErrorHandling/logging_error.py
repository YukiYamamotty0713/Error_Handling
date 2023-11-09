import sys
'''
以下エラーが起きたpythonファイルの例外処理欄に貼り付け
  # エラーが発生した場合の処理
    error_type = type(e).__name__  # エラータイプを取得
    error_message = str(e)  # エラーメッセージを取得
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # タイムスタンプを取得
    error_traceback = traceback.format_exc()  # エラーのトレースバック情報を取得

    # エラーデータを logging_error.py に渡す
    subprocess.run(["python", "logging_error.py", error_type, error_message, timestamp, error_traceback])
'''

if len(sys.argv) > 1:
    error_type = sys.argv[1]
    error_message = sys.argv[2]
    timestamp = sys.argv[3]
    error_traceback = sys.argv[4]

    # エラーログファイルに書き込む
    with open('execution_history.log', 'a') as log_file:
        log_file.write("-------------------------------------------------\n")
        log_file.write(f"Timestamp: {timestamp}\n")
        log_file.write(f"Error Type: {error_type}\n")
        log_file.write(f"Error Message: {error_message}\n")
        log_file.write(f"Error Traceback:\n{error_traceback}\n")
    
    
 
