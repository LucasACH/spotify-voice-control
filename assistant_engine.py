import pyttsx3

class VirtualAssistant:

    # Initialize pyttsx3
    engine = pyttsx3.init()

    # Voices installed in PC
    voices = engine.getProperty("voices")

    # Set voice changing voices[index]
    engine.setProperty("voice", voices[0].id)

    # Set voice speed rate
    engine.setProperty("rate", 140)
    
    # To see voices installed in your PC, call VirtualAssistant().get_voices() 
    def get_voices(self):
        for voice in self.voices:
            print(voice.name)

    # To make it talk, call VirtualAssistant().talk(text)
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
