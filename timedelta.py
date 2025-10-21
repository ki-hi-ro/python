from datetime import datetime, timedelta

now = datetime.now()

after_30_days = now + timedelta(days=30)
after_10_hours = now + timedelta(hours=10)
after_5_minutes = now + timedelta(minutes=5)
after_1_second = now + timedelta(seconds=1)

print("Current date and time:", now)
print("Date and time after 30 days:", after_30_days)
print("Date and time after 10 hours:", after_10_hours)
print("Date and time after 5 minutes:", after_5_minutes)
print("Date and time after 1 second:", after_1_second)