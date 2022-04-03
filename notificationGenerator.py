#This class functions get called when the system timer is up. ie, when we are scheduled for an update
import weatherAPI

class GenerateNotification:
    
    #Returns a list of [[Temp in celcius],[Cold/Warm/Chilly], [Items to bring], [Conditions], [Wind (Y/N)]]
    def whatToBring(self):
        ret = []
        temp = []
        weatherAPI.getWeatherForecast()
        statistics = weatherAPI.today
        temperature = statistics[1]
        ret.append([temperature])
        condition = statistics[3]
        windSpeed = statistics[5]

        #Temperature description
        if(float(temperature) <= 5):
            temp.append("cold")
        elif(float(temperature) > 5 and float(temperature) <= 21):
            temp.append("chilly")
        else:
            temp.append("warm")
        ret.append(temp)
        temp = []

        #Items to bring
        if(condition == "Rain" or condition == "Drizzle" or condition == "Thunderstorm"):
            temp.append("umbrella")
            temp.append("raincoat")
        elif(condition == "Snow" or condition == "Haze"):
            temp.append("winterJacket")
            temp.append("headWarmer")
        elif(condition == "Clear"):
            temp.append("hat")
            temp.append("sunglasses")
        elif(condition == "Clouds"):
            temp.append("sweater")
        ret.append(temp)
        temp = []

        #Actual condition
        ret.append([condition])

        #Wind
        if(float(windSpeed) > 15.0):
            ret.append(["Y"])
        else:
            ret.append(["N"])
        return ret
    
    #Returns a list of [[Temp in celcius],[Cold/Warm/Chilly], [Conditions], [Wind (Y/N)]]
    def nextDayStats(self):
        ret = []
        temp = []
        weatherAPI.getWeatherForecast()
        statistics = weatherAPI.tomorrow
        temperature = statistics[1]
        ret.append([temperature])
        condition = statistics[3]
        windSpeed = statistics[5]

        #Temperature description
        if(float(temperature) <= 5):
            temp.append("cold")
        elif(float(temperature) > 5 and float(temperature) <= 21):
            temp.append("chilly")
        else:
            temp.append("warm")
        ret.append(temp)
        temp = []

        #Actual condition
        ret.append([condition])

        #Wind
        if(float(windSpeed) > 15.0):
            ret.append(["Y"])
        else:
            ret.append(["N"])
        
        return ret

        # Cold = False
        # Warm = False
        # Chilly = False

        # Sweater = False
        # WinterJacket = False
        # LightClothing = False
        # Umbrella = False
        # Raincoat = True
        # Sunglasses = False
        # Hat = False
        # HeadWarmer = False

        # Snow = False
        # Clouds = False
        # Rain = False
        # Clear = False
        # Drizzle = False
        # Thunderstorm = False
        # Mist = False
        # Smoke = False
        # Haze = False
        # Dust = False
        # Fog = False
        # Sand = False
        # Ash = False
        # Squall = False
        # Tornado = False
        # Windy = False

# print(GenerateNotification.whatToBring(GenerateNotification))
# print(GenerateNotification.nextDayStats(GenerateNotification))