# Print yesterday, today, and tomorrow
from datetime import datetime, timedelta

def print_dates():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    
    print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
    print("Today:", today.strftime('%Y-%m-%d'))
    print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))

input("Press Enter to show yesterday, today, and tomorrow...")
print_dates()

# Example:
# If today is 2025-02-21, the output will be:
# Yesterday: 2025-02-20
# Today: 2025-02-21
# Tomorrow: 2025-02-22

