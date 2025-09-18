import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.list import ThreeLineListItem
from home import HomeScreen
from class_data import ClassDataScreen
from student_data import StudentDataScreen
from registration import RegistrationScreen
from edit_data import EditDataScreen
from settings import SettingsScreen
from datetime import datetime

Builder.load_file('home.kv')
Builder.load_file('class_data.kv')
Builder.load_file('student_data.kv')
Builder.load_file('settings.kv')
Builder.load_file('navigation_drawer.kv')

class ConvertorApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.primary_hue = '300'
        self.screen_manager = MDScreenManager()
        self.screen_manager.add_widget(HomeScreen(name = 'home'))
        self.screen_manager.add_widget(ClassDataScreen(name = 'class_data'))
        self.screen_manager.add_widget(StudentDataScreen(name = 'student_data'))
        self.screen_manager.add_widget(RegistrationScreen(name = 'registration'))
        self.screen_manager.add_widget(EditDataScreen(name = "edit_screen"))
        self.screen_manager.add_widget(SettingsScreen(name = 'settings'))

        return self.screen_manager

    def on_start(self):
        '''if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])
            '''

    def change_theme_style(self, active):
        if active:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def select_theme_color(self, chip):
        for child in self.screen_manager.get_screen("settings").ids.theme_color_layout.children:
            
            if child.text == chip.text:
                child.active = True
                self.theme_cls.primary_palette = chip.text
            else:
                child.active = False

    def go_to_students_data(self):
        pass
        #incomplete

    def academics(self):
        pass

    def achievements(self):
        pass

    def notice(self):
        pass

    def department(self):
        pass

    def placement(self):
        pass
    
if __name__ == "__main__" :
    ConvertorApp().run()
