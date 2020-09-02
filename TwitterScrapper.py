import GetOldTweets3 as got
from random import randrange

# #Based off of the GetOldTweets3 query search example. I added a search function, GUI, and the ability to randomly select a tweet out of 25 to show to the user.

def findtweet(tweet):
    try:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search)\
                                                .setSince("2019-09-01")\
                                                .setUntil("2020-09-1")\
                                                .setMaxTweets(25)\
                                                .setTopTweets(True)\
                                                .setEmoji("unicode")
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[tweet]
        return tweet.username + " said: " + tweet.text
    except:
        print("An error has occurred.")

# This was based off of the PySimpleGUI cookbook documentation examples. I added the ability to integrate what the person types with

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text("Enter what you want to look up on Twitter",justification="center",key='-OUTPUT-', size=(70,4))],
          [sg.Input(key='Input',justification="center")],
          [sg.Button('Search')]]

window = sg.Window('LonelyTwitter', layout)

while True:  # Event Loop
    event, values = window.read()
    search = values['Input']
    if event == sg.WIN_CLOSED:
        break
    if event == 'Search':       
        results = findtweet(randrange(26))
        print(results)
        window['-OUTPUT-'].update(results)
        
window.close()