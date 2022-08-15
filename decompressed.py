from tkinter import Tk,Label
from os import popen 
from time import sleep

win = Tk()
win.attributes('-topmost',True)
win.overrideredirect(True)

while True:
    output_stream = popen('curl -H "Accept: text/plain" https://icanhazdadjoke.com')
    try:
        joke = Label(text = output_stream.read())
        joke.pack(pady= 20)
        win.update()
    except:
        output_stream = popen('curl -H "Accept: text/plain" https://icanhazdadjoke.com')
    sleep(600)
    joke.destroy()