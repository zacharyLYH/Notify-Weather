import requests
import json 
import datetime
import configureUserInfo as User

#hourly =[date time, temp, feels like, main, description, wind speeds ]
today = []
tomorrow = []

def getWeatherForecast():
    User.GetUserInfo.lat = 43.0408
    User.GetUserInfo.lon = -78.7812
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(User.GetUserInfo.lat) + "&lon=" + str(User.GetUserInfo.lon) +"&exclude=current,minutely,&appid=8c61803aa409e7f52a377ee97b668d6d&units=metric"
    response = requests.get(url)
    obj = response.json()
    text = json.dumps(obj)
    weather = json.loads(text)

    todayStats = weather.get("daily")[0]
    today.append(str(datetime.datetime.fromtimestamp(todayStats.get("dt"))))
    today.append(str(todayStats.get("temp").get("day")))
    today.append(str(todayStats.get("feels_like").get("day")))
    today.append(str(todayStats.get("weather")[0].get("main")))
    today.append(str(todayStats.get("weather")[0].get("description")))
    today.append(str(todayStats.get("wind_speed")))

    tomorrowsStats = weather.get("daily")[1]
    tomorrow.append(str(datetime.datetime.fromtimestamp(tomorrowsStats.get("dt"))))
    tomorrow.append(str(tomorrowsStats.get("temp").get("day")))
    tomorrow.append(str(tomorrowsStats.get("feels_like").get("day")))
    tomorrow.append(str(tomorrowsStats.get("weather")[0].get("main")))
    tomorrow.append(str(tomorrowsStats.get("weather")[0].get("description")))
    tomorrow.append(str(tomorrowsStats.get("wind_speed")))

#     print(today)
#     print(tomorrow)

# getWeatherForecast()

