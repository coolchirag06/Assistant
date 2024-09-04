import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
from openai import OpenAI
import os
import pygame
from gtts import gTTS

recogniser = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def aiprocess(command):
    client = OpenAI(api_key = "sk-0dPcSN1P5S4cnJnPmYt2kZrgyRw4xrK-PGVF3J4q_AT3BlbkFJHFYDUG8hisaFsBhAfzp0ZCKoULpYbbL2hrpaiCNhcA"
    )
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "you are a ai assistant named assistant", "content": "answer the queries of user briefly"},
        {"role": "user", "content":command}
    ]
    )
    return completion.choices[0].message.content
    
def ProcessCommand(c):

    print("process kar raha hu...")
    splited_command = c.split(" ")
    if splited_command[0] == "open":
        if "open google" in c.lower():
            webbrowser.open("www.google.com")
        elif "open facebook" in c.lower():
            webbrowser.open("www.fb.com")
        elif "open twitter" in c.lower():
            webbrowser.open("www.x.com")
        elif "open youtube" in c.lower():
            webbrowser.open("www.youtube.com")
        elif "open youtube music" in c.lower():
            webbrowser.open("music.youtube.com")
        elif "open github" in c.lower():
            webbrowser.open("www.github.com")
        elif "open spotify" in c.lower():
            webbrowser.open("www.spotify.com")
        elif "open gmail" in c.lower():
            webbrowser.open("mail.google.com")
        elif "open whatsapp" in c.lower():
            webbrowser.open("www.whatsapp.com")
        elif "open google keep" in c.lower():
            webbrowser.open("keep.google.com")
        elif "open discord" in c.lower():
            webbrowser.open("www.discord.com")
        elif "open reddit" in c.lower():
            webbrowser.open("www.reddit.com")
    elif splited_command[0] == "play":
        song_undone = splited_command[1]
        song = song_undone.lower()
        link = music_library.music[song]
        webbrowser.open(link)
    else:
        #let openai handel the request
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing assistant")

    # obtain audio from the microphone
    #Listen for the wake word Assistant
    while True:
        r = sr.Recognizer()
        
        # recognize speech using google

        try:
            with sr.Microphone() as source:
                print("Listning...")
                word = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(word)
            if ("assistant" in command.lower()):
                speak("hanji")
                #listen for command
                with sr.Microphone() as source:
                    print("bolo ji...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    ProcessCommand(command)
                
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))