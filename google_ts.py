from gtts import gTTS
k = "Hello, you are welcome here and this is an example of your clip"
tts = gTTS(text=k, tld='com.au', lang='en',  slow=False)
tts.save('req_clip.mp3')
