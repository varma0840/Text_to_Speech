from gtts import gTTS
import os


mytxt="Hello guys now u can here my voice"

language='en'

output=gTTS(text=mytxt, lang=language, slow=False)

output.save("speech.mp3")

os.system("start speech.mp3")