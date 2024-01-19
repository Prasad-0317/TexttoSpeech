from gtts import gTTS 
from playsound import playsound 
language = "en"
text = "hi" 
speech = gTTS(text = text,lang =language,slow=False,tld="co.in") 
speechhindi = gTTS(text=text,lang='hi')
speech.save("texttospeech1.mp3")
# speechhindi.save("v1.mp3")