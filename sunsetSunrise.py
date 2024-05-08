# import modules
from tkinter import *
from geopy.geocoders import Nominatim
import datetime
from suntime import Sun


# user defined funtion
def sun():
    try:

        geolocator = Nominatim(user_agent="geoapiExercises")

        ladd1 = str(e.get())
        location1 = geolocator.geocode(ladd1)

        latitude = location1.latitude
        longitude = location1.longitude

        sun = Sun(latitude, longitude)

        time_zone = datetime.datetime.now()

        sun_rise = sun.get_local_sunrise_time(time_zone)
        sun_dusk = sun.get_local_sunset_time(time_zone)

        res_rise = sun_rise.strftime('%H:%M')
        res_dusk = sun_dusk.strftime('%H:%M')

        result1.set(res_rise)
        result2.set(res_dusk)

    except:
        result1.set("oops! something get wrong")


# object of tkinter
# and background set to light grey
master = Tk()
master.configure(bg='light grey')
master.title("Sun")

# Variable Classes in tkinter
result1 = StringVar();
result2 = StringVar();

# Creating label for each information
# name using widget Label
Label(master, text="Enter place : ",
      bg="light grey").grid(row=1, sticky=W)
Label(master, text="Sunrise :",
      bg="light grey").grid(row=3, sticky=W)
Label(master, text="Dusk :",
      bg="light grey").grid(row=4, sticky=W)

# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=result1,
      bg="light grey").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=result2,
      bg="light grey").grid(row=4, column=1, sticky=W)

e = Entry(master, width=50)
e.grid(row=1, column=1)

# creating a button using the widget
b = Button(master, text="Check",
           command=sun, bg="white")
b.grid(row=1, column=2, columnspan=2,
       rowspan=2, padx=5, pady=5, )

mainloop()