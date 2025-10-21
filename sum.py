sample_list = [1, 2, 3, 4, 5]
total_sum = sum(sample_list)
print(f"The sum of the list is: {total_sum}")

print("-----")

from datetime import timedelta
sample_list = [timedelta(days=2, hours=3), timedelta(hours=5, minutes=30), timedelta(days=1, minutes=45)]
total_sum = sum(sample_list, timedelta())
print(f"The sum of the list is: {total_sum}")