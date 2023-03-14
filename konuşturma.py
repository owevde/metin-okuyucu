# Importing the library
from gtts import gTTS
import os

# Providing the text
input_text = "ESSALAMU ELEYKUM VEREHMATULLAHİ VEBEREKETUH OMER YAHXİMİSEN"

# Setting the language
language = "ru"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# Playing the filecls

os.system("start demo.mp3")
# bu bek yah xi bul di asistanımızı yapa biliriz yakında....