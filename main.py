from plyer import notification      # Import (pip install plyer) (python3 -m pip install git+http://github.com/kivy/pyobjus/)
import schedule                    # Import (pip install schedule)
import time
import configureUserInfo
import notificationGenerator

def notify(temperature, feeling , items, condition, wind):
    windNoti = ""
    if(wind == "Y"):
        windNoti = "Expect strong winds!"
    else:
        windNoti = "Mild to no winds."
    notification.notify(
        message = "It's generally {} at {}°C later. Bring {}. Expect {}. {}\n".format(feeling, temperature, items, condition.lower(), windNoti),
        #app_icon = "./weather.ico",
        timeout = 5
    )

def notifyTmr(temperature, feeling, condition, wind):
    windNoti = ""
    if(wind == "Y"):
        windNoti = "Expect strong winds!"
    else:
        windNoti = "Mild to no winds."
    notification.notify(
        message = "It's going to be {}°C and {} tomorrow. Expect {}. {}\n".format(temperature, feeling, condition.lower(), windNoti),
        #app_icon = "./weather.ico",
        timeout = 5
    )

def format(string):
    return string[0:2] + ":" + string[2::]

def callAPI(case):
    output = []
    if case == 0:
        output = notificationGenerator.GenerateNotification.whatToBring(notificationGenerator.GenerateNotification)
    else:
        output = notificationGenerator.GenerateNotification.nextDayStats(notificationGenerator.GenerateNotification)

    return output
    
def main():
    User = configureUserInfo.GetUserInfo 
    User.printWelcome(User)

    for entry in User.notiTime:
        
        if User.notiTime[entry][0]:
            
            if entry == 1:
                if(User.wantLeaveHomeMsges):
                    later = callAPI(0)
                    time1 = format(User.notiTime[entry][0])
                    schedule.every().monday.at(time1).do(notify, later[0][0], later[1][0], later[2][0], later[3][0], later[4][0])

                if(User.wantNextDayWeatherMsges):
                    tomorrow = callAPI(1)
                    time2 = format(User.notiTime[entry][1])
                    schedule.every().monday.at(time2).do(notifyTmr, tomorrow[0][0], tomorrow[1][0], tomorrow[2][0], tomorrow[3][0])

            elif entry == 2:
                if(User.wantLeaveHomeMsges):
                    later = callAPI(0)
                    time1 = format(User.notiTime[entry][0])
                    schedule.every().tuesday.at(time1).do(notify, later[0][0], later[1][0], later[2][0], later[3][0], later[4][0])

                if(User.wantNextDayWeatherMsges):
                    tomorrow = callAPI(1)
                    time2 = format(User.notiTime[entry][1])
                    schedule.every().tuesday.at(time2).do(notifyTmr, tomorrow[0][0], tomorrow[1][0], tomorrow[2][0], tomorrow[3][0])

            elif entry == 3:
                if(User.wantLeaveHomeMsges):
                    later = callAPI(0)
                    time1 = format(User.notiTime[entry][0])
                    schedule.every().wednesday.at(time1).do(notify, later[0][0], later[1][0], later[2][0], later[3][0], later[4][0])

                if(User.wantNextDayWeatherMsges):
                    tomorrow = callAPI(1)
                    time2 = format(User.notiTime[entry][1])
                    schedule.every().wednesday.at(time2).do(notifyTmr, tomorrow[0][0], tomorrow[1][0], tomorrow[2][0], tomorrow[3][0])

            elif entry == 4:
                if(User.wantLeaveHomeMsges):
                    later = callAPI(0)
                    time1 = format(User.notiTime[entry][0])
                    schedule.every().thursday.at(time1).do(notify, later[0][0], later[1][0], later[2][0], later[3][0], later[4][0])

                if(User.wantNextDayWeatherMsges):
                    tomorrow = callAPI(1)
                    time2 = format(User.notiTime[entry][1])
                    schedule.every().thursday.at(time2).do(notifyTmr, tomorrow[0][0], tomorrow[1][0], tomorrow[2][0], tomorrow[3][0])

            elif entry == 5:
                if(User.wantLeaveHomeMsges):
                    later = callAPI(0)
                    time1 = format(User.notiTime[entry][0])
                    schedule.every().friday.at(time1).do(notify, later[0][0], later[1][0], later[2][0], later[3][0], later[4][0])

                if(User.wantNextDayWeatherMsges):
                    tomorrow = callAPI(1)
                    time2 = format(User.notiTime[entry][1])
                    schedule.every().friday.at(time2).do(notifyTmr, tomorrow[0][0], tomorrow[1][0], tomorrow[2][0], tomorrow[3][0])

            elif entry == 6:
                if(User.wantLeaveHomeMsges):
                    later = callAPI(0)
                    time1 = format(User.notiTime[entry][0])
                    schedule.every().saturday.at(time1).do(notify, later[0][0], later[1][0], later[2][0], later[3][0], later[4][0])
                    
                if(User.wantNextDayWeatherMsges):
                    tomorrow = callAPI(1)
                    time2 = format(User.notiTime[entry][1])
                    schedule.every().saturday.at(time2).do(notifyTmr, tomorrow[0][0], tomorrow[1][0], tomorrow[2][0], tomorrow[3][0])

            elif entry == 7:
                if(User.wantLeaveHomeMsges):
                    later = callAPI(0)
                    time1 = format(User.notiTime[entry][0])
                    schedule.every().sunday.at(time1).do(notify, later[0][0], later[1][0], later[2][0], later[3][0], later[4][0])

                if(User.wantNextDayWeatherMsges):
                    tomorrow = callAPI(1)
                    time2 = format(User.notiTime[entry][1])
                    schedule.every().sunday.at(time2).do(notifyTmr, tomorrow[0][0], tomorrow[1][0], tomorrow[2][0], tomorrow[3][0])
    while(True):   
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()