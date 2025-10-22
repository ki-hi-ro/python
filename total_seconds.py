from datetime import datetime

now = datetime.now()
epoch = datetime(1970, 1, 1)

total_seconds = (now - epoch).total_seconds()

# print("現在の日時:", now)
# print("エポックからの秒数:", total_seconds)

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"エポックからの時間: {int(hours)}時間 {int(minutes)}分 {int(seconds)}秒")