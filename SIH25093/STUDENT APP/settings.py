from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class SettingsScreen(MDScreen):

    def home_button(self, instance):
        app = MDApp.get_running_app()
        app.screen_manager.current = "home"
