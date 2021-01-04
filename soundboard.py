import APIhandler

#import concurrent.futures
#import asyncio
import threading

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix import floatlayout,anchorlayout,stacklayout,progressbar
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.network import urlrequest

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


from builderString import *
Builder.load_string(builderString)





# Declare both screens
class MenuScreen(Screen):
	def on_enter(self,):
		#### EI TÄHÄN ####
		pass



class StartScreen(Screen):
	def on_enter(self,):
		self.ptimer = Clock.schedule_interval(self.progressChecker, 0.5)
		self.apithred = threading.Thread(target=APIhandler.checkAPI)
		self.apithred.setDaemon(True)
		self.apithred.start()

	def progressChecker(self,callback):
		
		if APIhandler.allDone:
			Clock.unschedule(self.ptimer)
			self.manager.current = "menu"
		self.ids.loading_progress.value = APIhandler.totalDownloads



class Soundboard(App):

	def build(self):
		sm = ScreenManager()
		sm.add_widget(StartScreen(name='start'))
		sm.add_widget(MenuScreen(name='menu'))

		return sm


if __name__ == '__main__':
	Soundboard().run()
