from twitter import *
from tkinter import *
from tKinter import *


def showTweets(x, num):
    #display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        w = Label(master, text=line1 + "\n" + line2 + "\n\n")
        w.pack()


def getTweets():
    
    x = t.statuses.home_timeline(screen_name="__no__fly__zone")
    return x


def tweet():

    global entryWidget

    if entryWidget.get().strip() == "":
        print "Empty"
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0, END)
        print "Working!"

#Put in token token_key, con_secret, con_secret_key
t = Twitter(
    auth=OAuth('165917647-OMgDOCzs2Wg396DSCKZMSBqe5wJBM6gwBFnMos9j', 'KfndRQZ3sqhQvEETRlUnEMVVzkAYv2m4Ell1DOIppmSVe', '	23Qq1YLlnflPQZOGhS8AGP1gD', 'QIaVraa2qjutyVwFIWxPwCd9iBAbo2EwsiNFMVR9HMKoTDQXgk'))


numberOfTweets = 5

master = Tk()
showTweets(getTweets(), numberOfTweets)

master.title("Tkinter Entry Widget")
master['padx'] = 40
master['pady'] = 20
#Create a text frame to hold the next Label and the Entry Widget

textFrame = Frame(master)

#Create a label in textFrame

entryLabel = Label(textFrame)
entryLabel["text"] = "Make a new Tweet:"
entryLabel.pack(side=LEFT)

#Create an entry widget in textFrame

entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()
button = Button(master, text="Submit", command=tweet)
button.pack()

master.mainloop() 