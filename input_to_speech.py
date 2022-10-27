from gtts import gTTS
import os
from tkinter import *

root = Tk()


def text_to_speech():
    text = entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save("inp_output.mp3")
    os.system("start inp_output.mp3")


canvas = Canvas(root, width=400, height=300)
canvas.pack()
entry = Entry(root)
canvas.create_window(200, 180, window=entry)
button = Button(text="start", command=text_to_speech)
canvas.create_window(200, 230, window=button)
root.mainloop()
