# Calculate the difference between two dates in seconds
from datetime import datetime

def date_difference_in_seconds(date1, date2):
    dt1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    dt2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    return abs(int((dt2 - dt1).total_seconds()))

# User input
date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

print("Difference in seconds:", date_difference_in_seconds(date1, date2))

# Example:
# User enters:
# Enter first date: 2024-02-20 12:00:00
# Enter second date: 2024-02-21 14:30:00
# Output:
# Difference in seconds: 94500
# (This is 1 day + 2 hours 30 minutes = 94500 seconds)
