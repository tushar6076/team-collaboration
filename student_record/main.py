import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.list import ThreeLineListItem
from home import Home
import sqlite3
from datetime import datetime

Builder.load_file('home.kv')
Builder.load_file('student_data.kv')
Builder.load_file('settings.kv')

class ConvertorApp(MDApp):

    def build(self):
        with open ('data.db', 'a'):
            pass

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.primary_hue = '300'
        self.manager = MDScreenManager()
        self.manager.add_widget(Home(name = 'home'))

        return self.manager
    
    def on_start(self):
        db = sqlite3.connect('data.db')
        cr = db.cursor()
        cr.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    
if __name__ == "__main__" :
    ConvertorApp().run()
