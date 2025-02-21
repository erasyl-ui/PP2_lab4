# Subtract five days from the current date
from datetime import datetime, timedelta

def subtract_five_days():
    today = datetime.today()
    result = today - timedelta(days=5)
    return result.strftime('%Y-%m-%d')

input("Press Enter to subtract five days...")
print("Date five days ago:", subtract_five_days())

# Example:
# If today is 2025-02-21, the output will be:
# Date five days ago: 2025-02-16
