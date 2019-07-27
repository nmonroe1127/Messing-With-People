import random
import time
import webbrowser
import pyautogui
import autopy
import pyttsx3

## Opening up a google webpage and then sleeping for ten seconds so that it can load properly
visit = "http://{}".format('google.com')
webbrowser.open(visit)
time.sleep(10)

## This is the first string that will be auto-typed into the google search bar.
string_warning = "Hi there. I hope you realize that I have complete control of your computer now." \
               " You can try to stop me, but that will not work. Just ask Nick nicely and he will" \
               " stop it. In five seconds I will start spamming you with webpages. "
string_position = 0
while string_position < len(string_warning):
    pyautogui.press(string_warning[string_position])
    string_position += 1

## We then have a separate string for the countdown. Just made a second for clarity
string_countdown = "5..........4..........3..........2..........1.........."
string_position = 0
while string_position < len(string_countdown):
    pyautogui.press(string_countdown[string_position])
    string_position += 1

## lets mess with people and have the speaker randomly start talking to them.
engine = pyttsx3.init()
engine.say('Well, I guess we all make mistakes sometimes. Im gonna make your computer freeze up now.')
engine.runAndWait()

## Now we can choose random sites and open them, also the mouse will spaz out.
# page_total = 0
# while page_total < 30:
#     sites = random.choice(['google.com/search?q=you+are+being+hacked',
#                            'google.com/search?q=just+give+up',
#                            'google.com/search?q=never+click+links',
#                            'youtube.com/results?search_query=you+have+been+hacked'])
#     visit = "http://{}".format(sites)
#     webbrowser.open(visit)
#     seconds = random.randrange(5, 10)
#
#     time.sleep(5/100)
#     page_total += 1
#     pos_x = random.randrange(300, 900)
#     pos_y = random.randrange(200, 700)
#     autopy.mouse.move(pos_x, pos_y)
