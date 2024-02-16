from requests import get
from datetime import datetime


response = get("https://www.cbr-xml-daily.ru/daily_json.js")
data = response.json()
date_str = data["Date"]
date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
date = date_obj.date()
print(date)
