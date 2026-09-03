from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()
print(now)  # Output: 2023-10-10 12:34:56.789012

# Format the date and time
print(now.strftime("%y-%m-%d %H:%M:%S"))  # Output: 2023-10-10 12:34:56

#date arithmetics
tomorrow = now + timedelta(days=1)
print(tomorrow)  # Output: 2023-10-11 12:

diff = now + timedelta(days=5, hours=3, minutes=30)
print(diff)  # Output: 2023-10-09 12:34:56.789012

#parsing date strings
damola = datetime.strptime("2023-10-10 12:34:56", "%Y-%m-%d %H:%M:%S")
print(damola)  # Output: 2023-10-10 12:34:56