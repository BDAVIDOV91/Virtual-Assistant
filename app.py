import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import wikipedia


class Assistant:
        
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')
            r.pause_threshold = 0.7
            audio = r.listen(source)

            try:
                print('Recognizing')
                Query = r.recognize_google(audio, language = 'en-us')
                print('the command is printed =', Query)

            except Exception as e:
                print(e)
                print('Say that again please')
                return 'None'
            
            return Query


    def speak(audio):

        engine = pyttsx3.init()    
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()


    def tellDay():
        day = datetime.datetime.today().weekday() + 1
        dayDict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}

        if day in dayDict.keys():
            dayOfTheWeek = dayDict[day]
            print(dayOfTheWeek)
            Assistant.speak('The day is ' + dayOfTheWeek)


    def tellTime():

        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        Assistant.speak(f'The time is {hour} Hours and {min} Minutes')


    def hello():
        Assistant.speak('Hello! I am your desktop assistent. Tell me how may I help you ')


    def takeQuery():
        Assistant.hello()

        while(True):
            query = Assistant.takeCommand().lower()
            if 'open youtube' in query:
                Assistant.speak('Opening YouTube ')
                webbrowser.open('www.youtube.bg')
                continue

            elif 'open google' in query:
                Assistant.speak('Opening Google')
                webbrowser.open('www.google.bg')
                continue

            elif 'what day it is' in query:
                Assistant.tellDay()
                continue

            elif 'Whats the time' in query:
                Assistant.tellTime()
                continue

            elif 'bye' in query:
                Assistant.speak('Bye. Wish you to be the best at python proggraming')
                exit()

            
            elif 'from wikipedia' in query:
                Assistant.speak('Checking the wikipedia')
                query = query.replace('wikipedia', '')

                result = wikipedia.summary(query, sentences = 4)
                Assistant.speak('According to wikipedia')
                Assistant.speak(result)

            elif 'tell me your name ' in query:
                Assistant.speak('Hey I am Dot. Your dekstop Assistant')


if __name__ == '__main__':
    Assistant.takeQuery()


