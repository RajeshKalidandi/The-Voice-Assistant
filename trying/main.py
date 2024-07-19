import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import os
import wikipedia
import pyautogui
import keyboard
import pyjokes
import datetime
import requests
import speedtest
import psutil
import randfacts
import requests
import random
from time import sleep
import time
import instaloader
from requests import get
from pytube import YouTube
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices") 
Assistant.setProperty('voices',voices[0].id)


def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    print("  ")
    Assistant.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = Cal_day()
    print(t)
    if (hour>=0) and (hour <=12) and ('AM' in t):
        Speak(f'Good morning boss, its {day} and the time is {t}')
        Speak("I am Online Boss , waiting for command")
    elif (hour >= 12) and (hour <16) and ('PM' in t):
        Speak(f"good afternoon boss, its {day} and the time is {t}")
        Speak("Jarvis At Your Service, tell me a command")
    else:
        Speak(f"good evening boss, its {day} and the time is {t}")
        Speak("How may i help you boss?")
        
def Cal_day():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        
        return day_of_the_week

def Clock_time(takequery):
    print(takequery)
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    Speak("Current time is "+time)
    
def locaiton():
    Speak("Wait boss, let me check")
    try:
        IP_Address =requests.get('https://api.ipify.org').text
        print(IP_Address)
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        print(url)
        geo_reqeust =get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        tZ = geo_data['timezone']
        longitude = geo_data['longitude']
        latidute = geo_data['latitude']
        org = geo_data['organization_name']
        print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
        Speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
        Speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
    except Exception as e:
        Speak("Sorry boss, due to network issue i am not able to find where we are.")
        pass


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExe()
        

    def takequery(self):
        self.query = sr.Recognizer()
        print("Listening....")
        self.query.pause_threshold = 1
        audio = self.query.listen(0,5)

        try:
            print("Recognizing....")
            self.query = self.query.recognize_google(audio, language="en-in")
            print(f"You said : {self.query}")

        except Exception as Error:
            return "None"

    def No_result_found(self):
        Speak('Boss I couldn\'t understand, could you please say it again.') 

    def TaskExe(self):  
        wish()
        while True :
            self.query = self.takequery()

            if 'hello jarvis' in self.query:
                a = "hello boss","hey boss","hi boss"
                Speak(random.choice(a))

            elif 'how are you' in self.query:
                Speak("I am Fine Boss !")
                Speak("Whats About You ?")
                
            elif 'good morning' in self.query:
                Speak("Good Morning Boss !")
                Speak("have a great day , enjoy the day boss")
                
            elif 'good afternoon' in self.query:
                Speak("Good afternoon boss")
                
            elif 'good evening' in self.query:
                Speak("Good evening boss")
                
            elif 'good night' in self.query:
                Speak("Good Night boss")
                
            
            elif " that's good" in self.query:  
                Speak("Thanks Boss !!")


            elif 'you need a break' in self.query:
                Speak("Ok Sir , You Can Call me Anytime !")
                Speak("Just Say Wake Up Jarvis!")
                break

            elif 'who invented you' in self.query:
                Speak("Iam Invented by my boss Krish , The Great Future AI Developer !")

            elif 'bye' in self.query:
                Speak("Ok boss , Bye !")

            elif 'who are you' in self.query:
                Speak("I am Jarvis , I am Personal AI Assistant of Krish , The Lastest Version Of Jarvis")


            elif 'google search' in self.query:
                Speak("Ok sir , This is What I Found For Your Search !")
                self.query = self.query.replace("Jarvis","")
                self.query = self.query.replace("google search","")
                self.query = self.query.replace("search","")
                self.query = self.query.replace("tell me about","")
                pywhatkit.search(self.query)
                Speak("Done Sir !")


            elif 'website' in self.query:
                Speak("Ok sir , Launching....")
                self.query = self.query.replace("Jarvis","")
                self.query = self.query.replace("website","")
                self.query = self.query.replace(" ","")
                web1 = self.query = self.query.replace("open","")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched !")

            elif 'launch' in self.query:
                Speak("Tell me The Name of the Website!")
                name = self.takequery()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                Speak("Done Sir!")


            elif 'wikipedia' in self.query:
                Speak("Searching Wikipedia....")
                self.query = self.query.replace("Jarvis","")
                self.query = self.query.replace("wikipedia","")
                self.query = self.query.replace("who is","")
                wiki = wikipedia.summary(self.query,30)
                Speak(f"According To Wikipedia : {wiki}")
                

            elif 'joke' in self.query:
                get = pyjokes.get_joke()
                Speak(get)

            elif 'repeat my words' in self.query:
                Speak("Speak Sir !")
                jj = self.takequery()
                Speak(f"You Said : {jj}")

            elif 'remember that' in self.query:
                remembermsg = self.query.replace("remember that","")
                remembermsg = self.query.replace("remember","")
                remembermsg = self.query.replace("jarvis","")
                Speak(f"You Tell me to Remind You That :" + remembermsg)
                remember = open('rdata.txt','w')
                remember.write(remembermsg)
                remember.close()

            elif 'what do you remember' in self.query:
                remember = open('rdata.txt','r')
                Speak("You Tell me That" + remember.read())

            elif 'shutdown' in self.query or 'down the system' in self.query:
                Speak("Do you really want to restart the the system boss ?")
                reply = self.takequery().lower()
                if 'yes' in reply:
                    Speak("Iam shutdowning the system Boss ! See you again !!")
                    os.system('shutdown /r /t 5')
                else:
                    Speak("as your wish boss")
                    
            elif 'restart' in self.query or 'restart the system' in self.query:
                Speak("Do you really want to restart the the system boss ?")
                reply = self.takequery().lower()
                if 'yes' in reply:
                    Speak("Iam shutdowning the system Boss ! See you again !!")
                    os.system('shutdown /r /t 1')
                else:
                    Speak("As your wish Boss!")

            elif 'are you ok' in self.query:
                Speak("i am ok, how are you boss??")
                f = self.takequery().lower()
                if 'i am' in f:
                    Speak("i will never make you cry, you will always happy, Boss !!")
                else:
                    Speak('never be sad, you know, everything is illusion')

            elif 'i am bored' in self.query:
                b = "Well you can try to learn something new boss.","Maybe you can binge watch some new series.","Mind watching some cool anime/series.","Maybe try learning something new boss","Theres always stuff to learn about."
                Speak(random.choice(b))
                
            elif 'is boring' in self.query or "is so boring" in self.query:
                a ="Well you can try to learn something new sir.","Maybe you can binge watch some new series.","Mind watching some cool anime/series.","Maybe try learning something new sir","Theres always stuff to learn about."
                Speak(random.choice(a))
            
            elif 'hello' in self.query:
                n = "hello boss.","Hello sir.","Welcome and hello Boss.","Hello sir, how are you?","Hello there."
                Speak(random.choice(n))
                
            elif 'good morning' in self.query:
                s = "Good morning and hello boss.","Well good morning boss have a good day today.","Good morning boss.","Good morning and have a great day boss."
                Speak(random.choice(s))
            
            elif 'good night' in self.query:
                w="Good night boss.","Well Good night boss.","Good night boss have a good sleep tonight.","Good night and have a good sleep boss."
                Speak(random.choice(w))
                
            elif 'how are you' in self.query:
                q="I am fine, how about you boss?","I'm doing fine boss.","I'm doing well boss and how about you?","I am fine as always boss.","I am fine as long as you maintain your computer."
                Speak(random.choice(q))
            
            elif 'you fine' in self.query:
                a="I am fine, how about you boss?","I'm doing fine boss'.","I'm doing well boss and how about you?","I am fine as always boss.","I am fine as long as you maintain your computer."  
                Speak(random.choice(a))
                
            elif 'i am fine' in self.query:
                f="Well good to know boss.","I am glad to hear about you, Keep Exercising.","So you are in good shape.","Well that is happy to know boss."
                Speak(random.choice(f))
                
            elif 'i am good' in self.query or 'doing fine' in self.query or 'doing ok' in self.query or "doing well" in self.query:
                d = "Well good to know boss.","I am glad to hear about you, Keep Exercising.","So you are in good shape.","Well that is happy to know boss."
                Speak(random.choice(d))
                
            elif 'i am sick' in self.query or 'not doing well' in self.query:
                a = "You should consult a doctor quickly.","Well that is bad, hope for a speedy recovery :-)","You should go and rest boss.","I am sorry to hear that boss hope for a speedy recovery :-)"
                Speak(random.choice(a))
                
            elif 'yes i am' in self.query or 'yes i will' in self.query:
                c ="Great boss.","Good to know boss.","Happy to know boss.","Great to know boss."
                Speak(random.choice(c))
                
            elif 'thank you' in self.query or 'thanks' in self.query:
                k = "No problem boss.","No problem your welcome boss.","No problem it is my duty to help you boss.","Your welcome sir it is my duty."
                Speak(random.choice(k))
                
            elif 'you are cool' in self.query:
                x = "Glad that you are impressed boss.","It seems that my service is satisfactory.","Thanks for the feedback looks like you're enjoying my service."
                Speak(random.choice(x))
                
            elif 'are wrong' in self.query:
                l = "Why are you saying that i'm wrong?","Impossible, computers cannot make mistakes.","Wrong about what boss?","Can you please explain to me why i was wrong?"
                Speak(random.choice(l))
                
            elif 'you real' in self.query:
                c = "Well i am boss that is till you turn me off!!!","Well i am real till you keep me on","I am real till you turn off this computer."
                Speak(random.choice(c))
                
            elif 'you a robot' in self.query or "are you robot" in self.query:
                z = "Yes i'm a robot but a smart one!","Yes i am, but a good one. let me prove it. how can i help you?","I am real till you turn off this computer."
                Speak(random.choice(z))
            
            elif 'are you created' in self.query or 'are you made' in self.query or 'are you invented' in self.query:
                h = "Well i am built using a language called python.","I was coded on a computer using python boss","I was coded using python and i had to undergo many challenges.","I was built using python to do tasks and json to store critical information."   
                Speak(random.choice(h))

            elif 'stupid' in self.query or 'you idiot' in self.query:
                e ="Don't Underestimate me dude","Thu Chutiye","I don't care the words of dogs"
                Speak(random.choice(e))
                
            elif 'old are you' in self.query:
                Speak("I'm quite young actually")
                
            elif 'do you like games' in self.query or 'like games' in self.query or 'which games' in self.query:
                p="I like games like freefire,minecraft.","Minecraft is cool and also you can contribute to the community using add-ons.","Minecraft cause you can code in it and create add-ons.","I prefer Minecraft get ready for the wild update."
                Speak(random.choice(p))
                
            elif 'Ok' in self.query:
                Speak("no problem")
                
            elif 'say something' in self.query or "speak something" in self.query:
                Speak("Well sir sometimes I don't have anything to say")
                
            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                Instagram_Pro()
                

            elif 'your favourite colour' in self.query:
                clr="my favorite colour is Blue boss","boss Blue is my favorite colour"
                Speak(random.choice(clr))


            elif 'do you have an imagination' in self.query or "do you imagine" in self.query:
                im="I do have an imagination. Sometimes I imagine I'm floating in space. It's magical","I do have an imagination. Sometimes I imagine that I'm fighting with group of enimes","I do have an imagination. Sometimes I imagine that I'm enjoying a summer vacation"
                Speak(random.choice(im))
                

            elif 'think of yourself' in self.query:
                se="Well boss i think I'm intelligent enough to answer your questions","i think I'm the smartest assistant","i think I'm the greatest invention of your's "
                Speak(random.choice(se))
                

            elif 'think of google' in self.query:
                go="well boss google is a good voice assistant for now","boss google is a good assistant but not as good as me","Google helps us explore the internet"
                Speak(random.choice(go))
                

            elif 'what to wear' in self.query :
                we="you can try white shirt on a black pant","you can try maroon shirt on a brown pant","you can wear blue shirt on a black pant","you can wear black shirt on a blue pant"
                Speak(random.choice(we))
                

            elif 'what am i thinking' in self.query:
                th="you're thinking that if jarvis guesses what i'm thinking. i'm going to freak out.","sorry boss i can't because brainless people doesn't think","sorry boss i can't match your intelligence levels"
                Speak(random.choice(th))
                

            elif 'tell me what do you want' in self.query or "what do you want" in self.query:
                dy="well boss i badly want a break from you","i want female version of Jarvis , boss i think you have created maya too","well boss i don't have hopes on anything"
                Speak(random.choice(dy))
                

            elif 'do you drink' in self.query:
                dr="sorry boss i'm not an alcoholic like you","i don't drink boss","sorry boss drinking is injurious to health"
                Speak(random.choice(dr))
                

            elif 'smoke' in self.query:
                sm="sorry boss i'm not a smoker like you","i don't smoke boss","sorry boss smoking is injurious to health"
                Speak(random.choice(sm))


            elif 'tell me about vision team' in self.query:
                vi="boss, vision team is the same team that created me","vision is a 5 men team who work on ai","vision is an intelligent team of a 5 men who belong to CSE AIML A section "
                Speak(random.choice(vi))
                

            elif 'what do you look like' in self.query:
                li="i think i look like chitti from robo","i don't know yet boss"
                Speak(random.choice(li))

            elif 'your crush' in self.query or "do you have a crush" in self.query:
                cu="i have a lots of crush on maya , the female version of me ","my crush is maya"
                Speak(random.choice(cu))

    
            elif 'do you know the way to moon' in self.query or 'do you know how to go to moon' in self.query or 'way to moon' in self.query:
                mn ="i can tell you if you have rocket.","i know the way but we can't reach to it without rockets"
                Speak(random.choice(mn))
                

            elif 'you scared of' in self.query:
                sc ="i scared of you when you are angry","i scared of low network","i scared of nightmares"
                Speak(random.choice(sc))
                

            elif 'mean by life' in self.query or 'what is meaning of life' in self.query or 'meaning of life' in self.query:
                li="living without any problems or tensions is called as life","sorry boss it's a big question i think i can't answer that question"
                Speak(random.choice(li))

            elif 'our maths teacher' in self.query or ' maths teacher' in self.query:
                hb="Hari Babu boss Sir ! Maths teacher boss","our maths sir is Hari Babu boss"
                Speak(random.choice(hb))

            elif 'who is your favorite faculty' in self.query:
                Speak("my favourite faculty is Hari Babu Sir and Lavanya Madam")

            elif 'pick up line'in self.query or 'tell me a pick up line' in self.query or 'how to impress a girl'in self.query or 'how to propose' in self.query:
                pl="I’m no mathematician, but I’m pretty good with numbers. Tell you what, give me yours and watch what I can do with it.","I seem to have lost my phone number. Can I have yours?","Are you a magician? Because whenever I look at you, everyone else disappears!","Are you sure you’re not tired? You’ve been running through my mind all day.","tell her that my friends are quite jealous of me cause i met a beauty that they never seen before","tell her do you know what happens in zero gravity i will be still falling for you"
                Speak(random.choice(pl))
    
        
            elif 'what do i eat' in self.query or "suggest me what to eat" in self.query:
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<10:
                    eat="well sir you can try Idly to start a good morning","well sir you can try Dosa to start a good morning","well sir you can try Puri to start a good morning"
                    Speak(random.choice(eat))
                elif hour>=10 and hour<15:
                    et="well sir you can try Burger for the lunch","well sir you can try Pizza for the lunch","well sir you can try Kfc for the lunch"
                    Speak(random.choice(et))
                else:
                    e="well sir you can eat Biryani for Dinner","well sir you can eat Mandi for Dinner","well sir you can eat Chappathi for Dinner"
                    Speak(random.choice(e))
                

            elif "where i am" in self.query or "where we are" in self.query or "location status" in self.query or "location" in self.query:
                locaiton()
            
            elif "how much battery left" in self.query or "battery status" in self.query or "how much power we have" in self.query or "system condition" in self.query:
                battery = psutil.sensors_battery()
                percentagee= battery.percent
                Speak(f"Sir our system have {percentagee} percent battery")
                if percentagee>=75:
                    Speak("we have enough power boss, we can perfectly continue our work")
                elif percentagee>=40 and percentagee<=75:
                    Speak("we should have to connect charging point to our system to charge our battery")
                elif percentagee>=15 and percentagee<=30:
                    Speak("we have low power Boss,we need to charge our system otherwise the system will be shutdown soon")
                elif percentagee<=15:
                    Speak("our system is going to shutdown soon , immediately we to charge our system")
                    
            elif "current time" in self.query or "time now" in self.query or "jarvis time" in self.query:
                Clock_time(self)
                
            
            elif "facts" in self.query or "fact" in self.query:
                a = randfacts.getFact()
                b = randfacts.getFact()
                c = randfacts.getFact()
                d = randfacts.getFact()
                e = randfacts.getFact()
                x = a, b, c, d, e
                facts = ("one", "two","three","four","five")
                for i in range(len(facts)):
                    Speak(f"Fact number {facts[i]}, {x[i]}")
                    
            elif "today" in self.query:
                    day = Cal_day()
                    Speak("Today is "+day)  
            
            
            elif 'ip address' in self.query:
                ip = requests.get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                Speak(f"your IP address is {ip}")
        
                
            elif 'your name' in self.query:
                Speak("My name is jarvis")
            
            elif 'my name' in self.query:
                Speak("your name is krish")
            
            elif 'college name' in self.query or "about my college" in self.query or "studying" in self.query:
                Speak("you are studing in Malla Reddy Engineering College, with B-tech in Computer Science and Artificail Intelligence") 
            
            elif 'what can you do' in self.query:
                Speak("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
            
            elif 'your age' in self.query or "are you young" in self.query:
                Speak("I am very young that u")
            
            elif 'dating' in self.query:
                Speak('Sorry not intreseted, I am having headache, we will catch up some other time')
            
            elif 'are you single' in self.query or "do you have girl friend" in self.query:
                Speak('No, I am in a relationship with wifi')
            
            elif 'are you there' in self.query:
                Speak('Yes boss I am here')
            
            elif 'tell me something' in self.query:
                Speak('boss, I don\'t have much to say, you should tell me something ,i will give you the company')
            
            elif 'thank you' in self.query:
                Speak('boss, I am here to help you..., your welcome')
            
            elif 'in your free time' in self.query:
                Speak('boss, I will be listening to all your words')
            
            elif 'i love you' in self.query:
                Speak('I love you too boss')
            
            elif 'can you hear me' in self.query:
                Speak('Yes Boss, I can hear you')
            
            elif 'do you ever get tired' in self.query:
                Speak('It would be impossible to tire of our conversation') 
           
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = 
        self.ui.setupUi(self)
        



        




