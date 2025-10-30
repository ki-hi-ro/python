OPEN = '11:00'

def is_store_open(time) -> bool: 
    return OPEN <= time

def enter_store(time):
    if is_store_open(time):
        print(f"{time}が{OPEN}以上なので、お店に入ります")
    else:
        print(f"{time}が{OPEN}以前なので、他のお店に入ります")

now = '10:30'
print("現在の時刻:", now)
enter_store(now)

after_one_hour = '11:30'
print("1時間後の時刻:", after_one_hour)
enter_store(after_one_hour)