# import requests
# url = 'https://httpbin.org/post'
# data = {'key1': 'value1'}
# response = requests.post(url, data=data)
# print(response.text)



from datetime import datetime
import pytz
tz = pytz.timezone('Asia/Tokyo')
now = datetime.now(tz)
print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))


from datetime import datetime, timezone, timedelta
tokyo_tz = timezone(timedelta(hours=9))  #東京のタイムゾーンを取得
now = datetime.now(tokyo_tz)
print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))