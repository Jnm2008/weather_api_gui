# importing requests which is used to query data from a website or api
import requests
# import tkinter
from tkinter import *
# imports a module called pretty print that formats python dictionaries into a readable format
from pprint import pprint as pp

#imports pillow which is used to view images
from PIL import ImageTk, Image
from urllib.request import urlopen

# our secret key to access the api
Key = 'ac57ff02bfce4b6883011257222911'
# defining a location variable
place = '80467'

# API information https://www.weatherapi.com/docs/
# creates a url to pull the information from
url = 'http://api.weatherapi.com/v1/current.json?key=' + Key + '&q=' + place + '&aqi=no'
# gets the data from the url provided
global r
r = requests.get(url)
# parses the data from r into a readable format for python and saves it as rj
global rj
rj = r.json()

# code that we can use to check the API status and print what the API returns
# print(r.status_code)
# print(pp(r.json()))

# defining variables from rj
location = rj['location']['name']
temp = rj['current']['temp_f']
time_date = rj['current']['last_updated']
condition = rj['current']['condition']['text']
condition_icon = rj['current']['condition']['icon']


# defining an image for the current condition that is pulled from the API (not working)
'''image_url = ('http:' + rj['current']['condition']['icon'])
response = requests.get(image_url)
if response.status_code:
    fp = open('condition.png', 'wb')
    fp.write(response.content)
    fp.close()

load = Image.open("condition.png")
condition_icon = ImageTk.PhotoImage(load)'''





# impliment Tkinter
root = Tk()
#creates the icon for root
root.iconbitmap('cloudy_1_.ico')
#sets the defualt root window size
root.geometry('350x350')
#creates a name for the root window
root.title('Weather')

# creates a function that gets the data or refreshes the data (not currently working)
def refresh():
    place = str(entry_location)
    url = 'http://api.weatherapi.com/v1/current.json?key=' + Key + '&q=' + place + '&aqi=no'
    r = requests.get(url)
    rj = r.json()

# create widgets
title_label = Label(root, text=location)
temp_label = Label(root, text=temp)
time_date_label = Label(root, text=time_date)
condition_label = Label(root, text=condition)
'''condition_icon_image_label = Label(root, image=condition_icon)
condition_icon_image_label.image = condition_icon'''


# create input field
entry_location = Entry(root)
entry_location.insert(0, 'Location')

# put the widgets onto the grid
title_label.grid(row=0, column=0, columnspan=3, )
temp_label.grid(row=1, column=0)
condition_label.grid(row=2, column=0)
#condition_icon_image_label.grid(row=2, column=1)
time_date_label.grid(row=3, column=0)
entry_location.grid(row=1, column=3, columnspan=2)



# creates a button that refreshes data (mpt currently working)
refresh_button = Button(root, text="Refresh", command=refresh)
refresh_button.grid(row=0, column=3, columnspan=2)

# loop the window as a window is just a continuously running program
root.mainloop()

