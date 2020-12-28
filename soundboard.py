#https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
# Sample Python application demonstrating   
# How to create GridLayout in Kivy  


import os.path
from os import path
import glob
# import kivy module  
import kivy
import random

# base Class of your App inherits from the App class.    
# app:always refers to the instance of your application    
from kivy.app import App  
    
# creates the button in kivy   
# if not imported shows the error   
from kivy.uix.button import Button 
  
# The GridLayout arranges children in a matrix. 
# It takes the available space and 
# divides it into columns and rows, 
# then adds widgets to the resulting “cells”. 
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from functools import *
import requests




colors = [[1, 0, 0, 1],[0, 1, 0, 1],[0, 0, 1, 1],[1, 0, 1, 1] ]


key = "WEETTERSYEETTERS"
load_url = "http://137.74.119.216/apis/soundboard_api.php"
resp = requests.get(load_url+"?key="+key)
data = resp.json()

if resp.status_code == 200:
    print("API-version: "+data['version'])
    print("Checking for commands")
    if data['forcereload'] == True:
        print("    Reloading all sound files!")

    os.makedirs('data/categories/',exist_ok=True)
    
    print("Checking for missing files...")
    for i in data['categories']:
        if not path.exists('data/categories/'+i):
            print("    Creating missing category: "+str(i))
            os.mkdir('data/categories/'+i)
                
        print("    Checking sound files for "+str(i))
        #data['soundstorage']+i+"/"+s


        filenames = os.listdir('data/categories/'+i+'.')
            
        for s in data['categories'][i]:
            if not s in filenames or data['forcereload'] == True:
                print("        Downloading file: "+s)
                r = requests.get(data['soundstorage']+i+"/"+s)
                open("data/categories/"+i+"/"+s, 'wb').write(r.content)

    print("Done!")


    






    
elif resp.status_code == 404:
    print("Error Page was not found")
    quit()


# Declare both screens
class MenuScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols = 2)
        for i in data['categories']:
            button = Button(text=i)
            button.bind(on_press=partial(self.openCategory,i))
            self.layout.add_widget(button)
            
        self.add_widget(self.layout)

    def openCategory(self,instance,name):
        print(instance)
        root.screenSwitcher("sounds","left",{"instance":instance})
        



class SoundsScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        button = Button(text="Back")
        button.bind(on_press=self.mainMenu)
        #self.toplayout.add_widget(button)
        
        self.layout = GridLayout(cols = 3)
        catname = root.exdata['instance']
        for i in data['categories'][catname]:
            button = Button(text=i,background_color = random.choice(colors))
            button.bind(on_press=self.playSound)
            self.layout.add_widget(button)

        #self.add_widget(self.toplayout)
        self.add_widget(self.layout)


    def playSound(self,instance):
        print()
        sound = SoundLoader.load('data/categories/'+root.exdata['instance']+"/"+instance.text)
        if sound:
            print("Sound found at %s" % sound.source)
        print("Sound is %.3f seconds" % sound.length)
        sound.play()

    def mainMenu(self,instance):
        root.screenSwitcher("menu","right")



class SoundboardApp(App): 
  
    # to build the application we have to 
    # return a widget on the build() function.
        
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.exdata = {"instance":"Dera"}
        self.sm = ScreenManager()
        self.screens = {'menu':MenuScreen(),'sounds':SoundsScreen()}
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(SoundsScreen(name='sounds'))
        return self.sm

    def screenSwitcher(self,sr,dire,exdata={}):
        self.exdata = exdata
        self.screens['sounds'] = SoundsScreen()
        self.sm.switch_to(self.screens[sr], direction=dire)
    

root = SoundboardApp() 
root.run() 
