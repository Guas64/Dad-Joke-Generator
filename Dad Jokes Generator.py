from tkinter import Tk,Label
from os import popen 
from time import sleep

#â€™¦
#â€“
#â€¨
#â€˜

win = Tk()
win.attributes('-topmost',True)
win.overrideredirect(True)

def StringChecks(string):
    StringList = [*string]
    FinalList = ""
    for x in range(len(StringList)):
        if StringList[x] == "â":
            if StringList[x + 1] == "€":
                if StringList[x + 2] == "™" or "¦" or "“" or "¨" or "˜":
                    StringList[x + 0] = ""
                    StringList[x + 1] = ""
                    StringList[x + 2] = ""
                
    for x in StringList:
        FinalList = FinalList + x
    return FinalList

while True:
    output_stream = popen('curl -H "Accept: text/plain" https://icanhazdadjoke.com')
    try:
        joke = Label(text = StringChecks(output_stream.read()))
        joke.pack(pady= 20)
        win.update()
    except:
        output_stream = popen('curl -H "Accept: text/plain" https://icanhazdadjoke.com')
        joke = Label(text = StringChecks(output_stream.read()))
        joke.pack(pady= 20)
        win.update()
    sleep(600)
    joke.destroy()