# !/usr/bin/python3
#  Weather_api_working.py
#   A program to display weather data from weatherapi.com in tkinter
# JM Nelson Dec 2022
#   modified by CR Nelson


# importing requests which is used to query data from a website or api
import requests
# import tkinter
from tkinter import *

import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# imports a module called pretty print that formats python dictionaries into a readable format
from pprint import pprint as pp

# imports pillow which is used to view images
from PIL import ImageTk, Image
from urllib.request import urlopen

#set up a class for the api data
class Apidata:
    def __init__(self, Name, Path):
        self.Name = Name
        self.Path = Path

# create a method that updates the path.  I think we want to update rj to a new dictionary but I'm not sure.  The way
    # I did it before where I just rewrote the entire dictionary isn't working.,
    def new_path(self):
        place = str(entry_location.get())
        url = f'http://api.weatherapi.com/v1/current.json?key= {Key} &q= {place} &aqi=no'
        r = requests.get(url)
        rn = r.json()





# our secret key to access the api
Key = '67248c701bf249409d3191912220312'
# defining a location variable
place = '80467'

# API information https://www.weatherapi.com/docs/
# creates a url to pull the information from
url = f'http://api.weatherapi.com/v1/current.json?key= {Key} &q= {place} &aqi=no'
# gets the data from the url provided

r = requests.get(url)
# parses the data from r into a readable format for python (.json) and saves it as rj

rj = r.json()

# code that we can use to check the API status and print what the API returns
# print(r.status_code)
# print(pp(r.json()))

# defining variables from rj

location = Apidata("location", rj['location']['name'])
temp = Apidata('temp', rj['current']['temp_f'])
wind = Apidata('wind', rj['current']['wind_mph'])
winddir = Apidata('winddir', rj['current']['wind_dir'])
gust = Apidata('gust', rj['current']['gust_mph'])

time_date = Apidata('time_date', rj['current']['last_updated'])
condition = Apidata('condition', rj['current']['condition']['text'])
condition_icon = Apidata('condition_icon', rj['current']['condition']['icon'])

#  instead set up default window using customtkinter
watcher = customtkinter.CTk()  # create CTk window like you do with the Tk window
watcher.geometry("450x280")
watcher.title("Weather Watcher")


# creates a function that gets the data or refreshes the data
def refresh(event=None):
    location.new_path()
    temp.new_path()
    wind.new_path()
    winddir.new_path()
    gust.new_path()
    condition.new_path()
    time_date.new_path()

    title_label.configure(text=location.Path)
    temp_label.configure(text=temp.Path)
    wind_label1.configure(text=wind.Path)
    winddir_label.configure(text=winddir.Path)
    time_date_label.configure(text=time_date.Path)
    condition_label.configure(text=condition.Path)
    gust1.configure(text=gust.Path)

    image_url = ('http:' + rj['current']['condition']['icon'])
    response = requests.get(image_url)
    if response.status_code:
        fp = open('condition.png', 'wb')
        fp.write(response.content)
        fp.close()
    # then display the image to the label
    image = Image.open('condition.png')
    display = customtkinter.CTkImage(image, size=(80, 80))
    condition_icon_image_label = customtkinter.CTkLabel(watcher, image=display)


# create and grid widgets
title_label = customtkinter.CTkLabel(watcher, text=location.Path)
title_label.grid(row=0, column=0, columnspan=3)

temp_name_label = customtkinter.CTkLabel(watcher, text='Temperature')
temp_name_label.grid(row=1, column=0)

temp_label = customtkinter.CTkLabel(watcher, text=temp.Path)
temp_label.grid(row=2, column=0)

wind_label = customtkinter.CTkLabel(watcher, text='Wind Speed')
wind_label.grid(row=4, column=0)

wind_label1 = customtkinter.CTkLabel(watcher, text=wind.Path)
wind_label1.grid(row=5, column=0)

wind_direction_name_label = customtkinter.CTkLabel(watcher, text="Wind Direction")
wind_direction_name_label.grid(row=4, column=1)

winddir_label = customtkinter.CTkLabel(watcher, text=winddir.Path)
winddir_label.grid(row=5, column=1)

gust_label = customtkinter.CTkLabel(watcher, text='Gusting')
gust_label.grid(row=4, column=3)

gust1 = customtkinter.CTkLabel(watcher, text=gust.Path)
gust1.grid(row=5, column=3)

time_date_label = customtkinter.CTkLabel(watcher, text=time_date.Path)
time_date_label.grid(row=7, column=0)

condition_label = customtkinter.CTkLabel(watcher, text=condition.Path)
condition_label.grid(row=3, column=0)

# create input field
entry_location = Entry(watcher)
entry_location.insert(0, 'Location')
entry_location.grid(row=0, column=6, columnspan=2)
entry_location.bind('<Return>', refresh)

# Obtaining and creating an icon from the API for current weather condition
# first get the image
image_url = ('http:' + rj['current']['condition']['icon'])
response = requests.get(image_url)
if response.status_code:
    fp = open('condition.png', 'wb')
    fp.write(response.content)
    fp.close()
# then display the image to the label
image = Image.open('condition.png')
display = customtkinter.CTkImage(image, size=(80, 80))
condition_icon_image_label = customtkinter.CTkLabel(watcher, text="", image=display)
condition_icon_image_label.grid(row=3, column=1)

# creates a button that refreshes data
refresh_button = Button(watcher, text="Refresh", command=refresh)
refresh_button.grid(row=0, column=2, columnspan=2)

# loop the window as a window is just a continuously running program
watcher.mainloop()

