import pyttsx3
import random
import datetime, time

mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]


def random_date():
    anno_ini = 2025
    anno_fine = 2025
    year = random.randint(anno_ini, anno_fine)
    month = random.randint(1, 12)
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        day = random.randint(1, 29 if is_leap else 28)
    
    return ([ str(day)+" "+str(mesi[month-1])+" "+str(year),giorni_settimana[datetime.date(year, month, day).weekday()] ])


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while 1:
	stringa=random_date()
	print(stringa[0])
	speak(stringa[0])
	time.sleep(7)
	speak(stringa[1])
	print(stringa[1])
	time.sleep(2)