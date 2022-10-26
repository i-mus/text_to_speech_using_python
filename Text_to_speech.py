from gtts import gTTS
import os
# generating audio from text data
text = "today is a good day"
output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')
os.system('start output.mp3')