import pyttsx3
engine = pyttsx3.init()
txt = open(r”c://user/kalyan/desktop/text.txt”).readlines()
engine.say(text)
engine.setProperty('rate',120)
engine.setProperty('volume', 0.9)
engine.runAndWait()
