import pyttsx3


engine = pyttsx3.init()
hello = "ethan"
engine.say(f"{hello} this shit wack")
engine.runAndWait()