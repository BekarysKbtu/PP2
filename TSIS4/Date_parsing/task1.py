from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Five days ago was:", five_days_ago.strftime("%Y-%m-%d"))
