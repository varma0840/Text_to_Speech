from gtts import gTTS
import os


mytxt=input("Type the text you want to listen in voice:")

language='en'

output=gTTS(text=mytxt, lang=language, slow=False)

output.save("speech.mp3")

os.system("start speech.mp3")
