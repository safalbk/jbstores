# from datetime import datetime

# date_string = "Aug. 18, 2023, 1:13 p.m."
# date_format = "%b.  %d, %Y, %I:%M %p."

# # Convert the date string to a datetime object
# datetime_object = datetime.strptime(date_string, date_format)

# print(datetime_object)
from datetime import datetime

#Date as a string
dateString = "Aug. 18, 2023, 1:13 p.m."
print(f"Date as {type(dateString)} is {dateString}")

#Converting string date into datetime object
dateTimeObj = datetime.strptime(dateString, "%b.  %d, %Y, %I:%M %p.")
print(f"Date as {type(dateTimeObj)} is {dateTimeObj}")