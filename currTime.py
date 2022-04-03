# From https://www.programiz.com/python-programming/datetime/current-time
from datetime import datetime

def get():
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
    return currentTime

