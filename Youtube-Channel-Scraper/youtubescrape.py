# Name: Kennedy Anukam
# Purpose: Display Youtube Channel information with tkinter GUI
from tkinter import *
import urllib.request
import json

key = "AIzaSyCTDbH8xo45eIncPJIKyN5V-_klCMJ2rHI"


def channel_data():
    # Extracting channel name from entry
    name = e1.get()
    # Last element will be channel ID
    y_id = name.split('/')[-1]
    # Name of Youtube Channel from user, key from Google api
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + y_id + "&key=" + key).read()
    # Need JSON data
    sub = json.loads(data)['items'][0]["statistics"]["subscriberCount"]
    total_view = json.loads(data)['items'][0]["statistics"]["viewCount"]
    total_videos = json.loads(data)['items'][0]["statistics"]["videoCount"]
    # Setting tkinter labels to values
    l2.config(text=sub)
    l4.config(text=total_view)
    l6.config(text=total_videos)


def main():
    # Create a tkinter window display interface
    root = Tk()
    root.title("Youtube Scraper")
    # Sets display size to 500x200
    root.geometry("500x200")
    # User can enter into text box the channel URL
    e1 = Entry(root, textvariable=StringVar())
    # Setting size of text box
    e1.grid(row=1, column=2)
    # Creating a button which uses the channel_data function to get the URL, uses text boxes entry
    b1 = Button(root, text="Enter Channel URL", command=channel_data)
    b1.grid(row=2, column=2)

    # Setting labels on the tkinter display
    l1 = Label(root, text="total number of subscribers : ", font="times 15 bold")
    l1.grid(row=4, column=1)
    l2 = Label(root, font="times 15 bold")
    l2.grid(row=4, column=3)

    l3 = Label(root, text="total number of views : ", font="times 15 bold")
    l3.grid(row=6, column=1)
    l4 = Label(root, font="times 15 bold")
    l4.grid(row=6, column=3)

    l5 = Label(root, text="total number of videos : ", font="times 15 bold")
    l5.grid(row=8, column=1)
    l6 = Label(root, font="times 15 bold")
    l6.grid(row=8, column=3)

    root.mainloop()


if __name__ == '__main__':
    main()
