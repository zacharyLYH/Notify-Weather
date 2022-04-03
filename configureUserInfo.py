import requests
import json 
import time

class GetUserInfo:
    lat = 0
    lon = 0
    name = ""
    zip = "a"
    day = {1: "MONDAY", 2: "TUESDAY", 3: "WEDNESDAY", 4:"THURSDAY", 5:"FRIDAY", 6: "SATURDAY", 7:"SUNDAY"}
    notiTime = {1: [], 2: [], 3:[], 4:[], 5:[], 6:[], 7:[]}
    phoneNum = 0
    wantLeaveHomeMsges = None
    wantNextDayWeatherMsges = None

    def is_valid_time(value):
        s = value[0:2] + ":" + value[2::]
        try:
            _ = time.strptime(value, '%H%M')
        except ValueError:
            return False
        return True

    #User sets their typical schedule here. Used to figure out what time on what day to send out notifications 
    def getNotiTime(self, day):
        print("\nIn 24 hour format, example: 0800 - 8AM, 2300 - 11pm")

        #A bug in the next 2 sections is if user supplies an input len (2 <= len <= 4), it passes.
        leaveHome = "0" 
        while(self.is_valid_time(leaveHome) == False):
            msg = "What time do you leave home on a typical "+ (self.day[day])+ "?: "
            leaveHome = input(msg)
            #leaveHome = str(int(leaveHome)-20)
            if(leaveHome == ""):
                self.notiTime[day].append(None)
            else:
                self.notiTime[day].append(leaveHome)
            if(len(leaveHome) == 0):
                break
        
        """A "feature" is if user wants nextDay notification and leaveHome notifications at the same time,
            it is allowed """
        nextDayWeather = "0"
        while(self.is_valid_time(nextDayWeather) == False or len(nextDayWeather) == 0):
            msg = "What time do you want next day weather on "+ (self.day[day]) + "?: "
            nextDayWeather = input(msg)
            #nextDayWeather = str(int(nextDayWeather)-20)
            if(nextDayWeather == ""):
                self.notiTime[day].append(None)
            else:
                self.notiTime[day].append(nextDayWeather)
            if(len(nextDayWeather) == 0):
                break

    #Welcome script
    def printWelcome(self):
        print(" _   _       _   _  __           __          __        _   _                ")      
        print("| \ | |     | | (_)/ _|          \ \        / /       | | | |               ")
        print("|  \| | ___ | |_ _| |_ _   _ _____\ \  /\  / /__  __ _| |_| |__   ___ _ __  ")
        print("| . ` |/ _ \| __| |  _| | | |______\ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__| ")
        print("| |\  | (_) | |_| | | | |_| |       \  /\  /  __/ (_| | |_| | | |  __/ |    ")
        print("|_| \_|\___/ \__|_|_|  \__, |        \/  \/ \___|\__,_|\__|_| |_|\___|_|    ")
        print("                      __/ |                                                 ")
        print("                    |___/                                                   ")
        #ASCII Art credit: https://www.ascii-art-generator.org/
        print("\nHello, welcome to NotifyWeather.")
        print("\nPlease answer the following questions to the best of your ability. Otherwise, leave blank and hit \"Enter\"!\n")
        print("Fields labeled with \"***\" Must be filled out")
        while(self.name.isalpha() == False):
            self.name = input("What should we call you (No space)?[A-Z, a-z] ***: ")
        #Assumes user inputs a real zip code. Does minimal checking.
        while(self.zip.isalpha() == True):
            self.zip = input("What is your zip code? ***: ")
            if(len(self.zip) != 5): #Weird but it works
                self.zip = "a"
        for i in range(1,8):
            self.getNotiTime(self, i)
        while(self.phoneNum != "" or (self.phoneNum.isdigit() == True and len(self.phoneNum) != 10 )):
            self.phoneNum = input("\nProvide your phone number (10digit): ")
        while(self.wantLeaveHomeMsges == None):
            temp = input("Do you want reminders on weather preperation before you leave home? [y/n]: ")
            if(temp == "y"):
                self.wantLeaveHomeMsges = True
            else:
                self.wantLeaveHomeMsges = False
        while(self.wantNextDayWeatherMsges == None):
            temp = input("Do you want to know the general weather for the next day the night before? [y/n]: ")
            if(temp == "y"):
                self.wantNextDayWeatherMsges = True 
            else:
                self.wantNextDayWeatherMsges = False
        self.printSummary(self)

    #Get coordinates script to get latitude and longitude from a provided zip code. This is used in getting weather info API. 
    def getCoordinates(self, zip):
        zipStr = str(zip)
        url = "http://api.openweathermap.org/geo/1.0/zip?zip=" + zipStr + ",US&appid=8c61803aa409e7f52a377ee97b668d6d"
        response = requests.get(url)
        obj = response.json()
        text = json.dumps(obj)
        y = json.loads(text)
        self.lat = y["lat"]
        self.lon = y['lon']
    
    def printSummary(self):
        print("\n")
        print(" _____                                                   ")
        print("/ ____|                                                  ")
        print("| (___  _   _ _ __ ___  _ __ ___   __ _ _ __ _   _       ")
        print("\___ \| | | | '_ ` _ \| '_ ` _ \ / _` | '__| | | |       ")
        print("____) | |_| | | | | | | | | | | | (_| | |  | |_| |       ")
        print("|_____/ \__,_|_| |_| |_|_| |_| |_|\__,_|_|   \__, |      ")
        print("                                            __/ |        ")
        print("                                            |___/        ")
        print("SUPPLIED INFORMATION: ")
        print("NAME: ", self.name)
        print("PHONE NUMBER: ", self.phoneNum)
        print("You want reminders for weather preperation for the day: ", self.wantLeaveHomeMsges)
        print("You want next day weather summary: ", self.wantNextDayWeatherMsges)
        for i in range(1,8):
            print("\n"+self.day[i]+ ": ")
            if(self.notiTime[i][0] == None):
                print("You leave home at: NOT SUPPLIED")
            else:
                print("You leave home at: ", self.notiTime[i][0])
            if(self.notiTime[i][1] == None):
                print("You want next day notifications at: NOT SUPPLIED")
            else:
                print("You want next day notifications at: ", self.notiTime[i][1])
        self.getCoordinates(self, self.zip)
        print("\nYour ZIP CODE is "+ self.zip+ ", so your LATITUDE is "+ str(self.lat)+ " and your LONGITUDE is " +str(self.lon) +".")
        print(" ______           _ ")
        print("|  ____|         | |")
        print("| |__   _ __   __| |")
        print("|  __| | '_ \ / _` |")
        print("| |____| | | | (_| |")
        print("|______|_| |_|\__,_|")

#GetUserInfo.printWelcome(GetUserInfo)

