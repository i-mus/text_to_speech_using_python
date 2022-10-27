from gtts import gTTS
import os

# converting file data to audio
sec_text = open("demo.txt", "r").read()
language = "en"
sec_output = gTTS(text=sec_text, lang=language, slow=False)
sec_output.save("fileout.mp3")
os.system("start fileout.mp3")
