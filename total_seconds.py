from datetime import datetime

now = datetime.now()
epoch = datetime(1970, 1, 1)

total_seconds = (now - epoch).total_seconds()

print("現在の日時:", now)
print("エポックからの秒数:", total_seconds)