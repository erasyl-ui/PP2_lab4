# Remove microseconds from the current datetime
from datetime import datetime

def drop_microseconds():
    now = datetime.now()
    return now.replace(microsecond=0)

input("Press Enter to remove microseconds...")
print("Current datetime without microseconds:", drop_microseconds())

# Example:
# If the current datetime is 2025-02-21 15:30:45.123456, the output will be:
# Current datetime without microseconds: 2025-02-21 15:30:45
