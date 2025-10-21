from datetime import datetime

date_string = "2024-06-15 14:30:00"

date_format = "%Y-%m-%d %H:%M:%S" 
parsed_date = datetime.strptime(date_string, date_format)

print("original date and time:", date_string)
print(type(date_string))

print("Parsed date and time:", parsed_date)
print(type(parsed_date))