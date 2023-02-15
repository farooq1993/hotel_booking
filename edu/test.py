#My first approch
# Python3 program to find number of days
# between two given dates
from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     
# Driver program
date1 = date(2023, 2, 10)
date2 = date(2023, 2, 20)
numOfDays(date1, date2)


"""
My Second Approch.
from dateutil import relativedelta
from datetime import datetime
 
# Parse the dates from strings into datetime objects
date1 = datetime.strptime("13/10/2018", "%d/%m/%Y")
date2 = datetime.strptime("25/12/2018", "%d/%m/%Y")
 
# Calculate the difference between the two dates
difference = relativedelta.relativedelta(date2, date1)
# Print the number of days between the two dates
print(difference.months,"months",difference.days, "days")
"""
 
# from datetime import datetime


# my_str = '2023-24-09'
# print("without format",my_str)
# # ✅ using uppercase Y directive
# date = datetime.strptime(my_str, '%Y-%d-%m')
# print("with format",date)
