# importing requests which is used to query data from a website or api
import requests
# import tkinter
from tkinter import *
# imports a module called pretty print that formats python dictionaries into a readable format
from pprint import pprint as pp

# our secret key to access the api
Key = 'ac57ff02bfce4b6883011257222911'
# defining a location variable
place = '80467'

# API information https://www.weatherapi.com/docs/
# creates a url to pull the information from
url = 'http://api.weatherapi.com/v1/current.json?key=' + Key + '&q=' + place + '&aqi=no'
# gets the data from the url provided
r = requests.get(url)
# parses the data from r into a readable format for python and saves it as rj
rj = r.json()

# defining variables from rj
location = rj['location']['name']
temp = rj['current']['temp_f']
querry_time = rj['current']['last_updated']


# code that we can use to check the API status and print what the API returns
# print(r.status_code)
# print(pp(r.json()))

# creates a function that gets the data or refreshes the data (not currently working)
def refresh():
    place = str(entry_location)
    url = 'http://api.weatherapi.com/v1/current.json?key=' + Key + '&q=' + place + '&aqi=no'
    r = requests.get(url)
    rj = r.json()





# impliment Tkinter
main = Tk()
main.title('Weather')

# create widgets
title = Label(main, text=location)
temptext = Label(main, text=temp)
timeanddate = Label(main, text=querry_time)

# create buttons

# creates a button that refreshes data (mpt currently working)
refresh_button = Button(main, text="Refresh", command=refresh,)

# create input field
entry_location = Entry(main)
entry_location.insert(0, 'Location')

# put the widgets onto the grid
title.grid(row=0, column=0, columnspan=3, )
temptext.grid(row=1, column=0)
timeanddate.grid(row=2, column=0)
refresh_button.grid(row=0, column=3, columnspan=2)
entry_location.grid(row=1, column=3, columnspan=2)

# loop the window as a window is just a continuously running program
main.mainloop()
