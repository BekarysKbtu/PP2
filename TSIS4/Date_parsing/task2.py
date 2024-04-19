from datetime import timedelta, datetime

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday was:", yesterday.strftime("%Y-%m-%d"))
print("Today is:", today.strftime("%Y-%m-%d"))
print("Tomorrow will be:", tomorrow.strftime("%Y-%m-%d"))
