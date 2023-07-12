#For running this file please make sure you downloaded following libraries
# SpeechRecognition , pyttsx3, PyAudio specific to your python version, googletrans 3.1.0a0 version


import  pygame
'''
pygame is an open source set of python modules. It is used to build games.
Pygame adds functionality on top of the excellent SDL library.
This allows us to create games as well as multimedia programs in the python language.
'''
from pygame.locals import*
'''
by * we imported every modules in pygame 
'''
import speech_recognition as sr
'''
It is a library specifically used for performing speech recognition, which supports many APIs.
'''
from googletrans import Translator
'''
Googletrans is a python library that implements Google Translate API.
It uses Google Translate Ajax API for detecting and translating different languages.
'''

import pyttsx3
'''
It is a library in python which inter-converts text to speech.
'''
import datetime
'''
The datetime module supplies classes for manipulating dates and times.
'''

from time import sleep


def translate_it(voice_input):
    '''
    this function will take a string input(voice_input) of hindi text specifically
    and convert it into english text
    '''
    translator=Translator()
    out=translator.translate(voice_input,src='hi',dest='en')
    return(out.text)

A_I=pyttsx3.init('sapi5')
voices=A_I.getProperty('voices')
A_I.setProperty('voice',voices[0].id)

def response(reply):
    '''
    this function will basically take a string input (in english and return a voice of that text.
    '''
    A_I.say(reply)                                    # Will give the audio response of string reply
    A_I.runAndWait()                                  # will wait some time and give voice reply

def time_():
    '''
    this function will provide us a reply(Good Morning, Good Evening etc) based on current time
    '''
    time_right_now=datetime.datetime.now().hour        # this function will give us the current tim's hour
    if time_right_now>=0 and time_right_now<12:        # if else condition will check the current hour and give respective reply
        reply="GOOD MORNING"
    elif time_right_now>=12 and time_right_now<16:
        reply="GOOD AFTERNOON"
    else:
        reply="GOOD EVENING"
    
    return reply                                       # will finally return the reply based on if else condition

def order1():
    '''
    It will take command from user through microphone and convert it into text
    and then returns that text.
    '''
    interpreter=sr.Recognizer()                               
    with sr.Microphone() as listened:                  # will use microphone attribute of speech recognization to hear our voice input
        text_2="speak for translation...."             # will show this text show user knows that he has to speak word for translation
        display_text_2=font.render(text_2.upper(),5,font_color) # the following are the conventions to show the multimedia representation of our programme in pygame window
        screen.blit(display_text_2,(65,315))
        pygame.display.update()
        response(text_2)                               # will call the response function defined earlier by us that will give the audio response
        print(text_2)
        interpreter.pause_threshold=0.9
        audio_heard=interpreter.listen(listened)       # will interpret the input voice in text
    try:
        print("interpreting your command...")
        request=interpreter.recognize_google(audio_heard,language='hi-in')  # will recognize that text(audio_heard) in hindi language and convert it into hindi text
        print("your voice input was= ",request)
    except Exception:
        #print(Exception)
        print("try saying again")                                           # it will simply take again input if the voice_input couldn't hear you
        return "NONE"
    
    return request                                                          # will finally return hindi text if the microphone heard the voice input


def order2():
    '''
    It will take command from user through microphone if he wants to continue translating more.
    '''
    interpreter=sr.Recognizer()
    with sr.Microphone() as listened:                           # will use microphone attribute of speech recognization to hear our voice input
        text_4="want to translate more..."                      # will show this text so user knows that if wants to translate more sentences/words
        display_text_4=font.render(text_4.upper(),5,font_color)         # the following are the conventions to show the multimedia representation of our programme in pygame window
        screen.blit(display_text_4,(65,315))
        pygame.display.update()
        response(text_4)                                        # will call the response function defined earlier by us that will give the audio response
        print(text_4)
        interpreter.pause_threshold=0.9
        audio_heard=interpreter.listen(listened)                # will interpret the input voice in text
    try:
        print("interpreting your command...")
        request=interpreter.recognize_google(audio_heard,language='en-in')  # will recognize that text(audio_heard) in english language(i.e either "yes" or "no") and convert it into hindi text
        print("your voice input was= ",request,"\n")
    except Exception:
        print(Exception)
        print("try saying again")                               # it will simply take again input if the voice_input couldn't hear you
        return "NONE"
    
    return request                                              # will finally return "yes" or "no" text if the microphone heard the voice input
    
        


#############################################################
'''
The following is the setup of our pygame window.
It will be our multimedia presentation of voice translation tool.
'''
pygame.init()
screen_width=500
screen_height=480
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Voice Translator')

#load images of the background and assistant image
assistant_img=pygame.image.load('assistant.png')
background_img=pygame.image.load('background.png')
color=(224,176,255)

# it will show us the text of command input on our multimedia representation on pygame window
# the following are the text convention and its font color
font=pygame.font.SysFont("Arial",18)
font_color=(0,0,0)
init=True
i=0
while init:                                            # this function will start the pygame window
    screen.blit(background_img,(0,0))                  # set following convention on our pygame window
    screen.blit(assistant_img,(15,100))
    for event in pygame.event.get():                   # this is the condition if user wants to end the file or pygame window
        if event.type==pygame.QUIT:
            init=False
    
    if i==0:                                           # this the first time pygame window/multimedia will represent the greetings like good morning or good evening
        pygame.draw.rect(screen,color,(50,300,400,50))
        pygame.draw.circle(screen,color,(80,280),10)
        pygame.draw.circle(screen,color,(95,265),8)
        text_0=time_()
        display_text_0=font.render(text_0,5,font_color)
        screen.blit(display_text_0,(65,315))
        pygame.display.update()
        response(text_0)
        print(text_0)
        i+=1
        continue

    elif i==1:                                         # this the next time it will run and window will run for translation this time
        pygame.draw.rect(screen,color,(50,300,400,50))
        pygame.draw.circle(screen,color,(80,280),10)
        pygame.draw.circle(screen,color,(95,265),8)
        voice_input=order1()

        text_3=translate_it(voice_input)
        pygame.draw.rect(screen,color,(50,300,400,50))
        pygame.draw.circle(screen,color,(80,280),10)
        pygame.draw.circle(screen,color,(95,265),8)
        display_text_3=font.render(text_3.upper(),5,font_color)
        screen.blit(display_text_3,(65,315))
        pygame.display.update()
        response(text_3)
        print(text_3)
        i+=1
        continue
    
    else:
                                                  #This is the next time it will run continuously if the user voice_input to continue for more translation
        pygame.draw.rect(screen,color,(50,300,400,50))
        pygame.draw.circle(screen,color,(80,280),10)
        pygame.draw.circle(screen,color,(95,265),8)
        voice_input=order2()                       #please speak up yes or no after a gap of 1.5-2 sec becoz of the compilation time it takes
        if voice_input.lower()=="yes":
            pygame.draw.rect(screen,color,(50,300,400,50))
            pygame.draw.circle(screen,color,(80,280),10)
            pygame.draw.circle(screen,color,(95,265),8)
            voice_heard=order1()
            text_5=translate_it(voice_heard)
            pygame.draw.rect(screen,color,(50,300,400,50))
            pygame.draw.circle(screen,color,(80,280),10)
            pygame.draw.circle(screen,color,(95,265),8)
            display_text_5=font.render(text_5.upper(),5,font_color)
            screen.blit(display_text_5,(65,315))
            pygame.display.update()
            response(text_5)
            print(text_5)
                
        else:                                                # this will finally stops if the voice input was "no" and finally end with voice response "thank you for using our service"
            sleep(0.5)
            text_6="THANK YOU FOR USING OUR SERVICE"
            pygame.draw.rect(screen,color,(50,300,400,50))
            pygame.draw.circle(screen,color,(80,280),10)
            pygame.draw.circle(screen,color,(95,2650),8)
            display_text_6=font.render(text_6.upper(),5,font_color)
            screen.blit(display_text_6,(65,315))
            pygame.display.update()
            response(text_6)
            print(text_6)
            init=False
                

    pygame.display.update()                                             #it keeps updating the display of pygame accordingly the changes we make
    i+=1
pygame.quit()                                                           # finally the pygame window quits if the init becomes false that is when the user says "no" as voice input for query of want to translate more
