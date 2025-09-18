from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty

class ItemDrawer(ThreeLineListItem):
    icon = StringProperty()

class ClassDataScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = MDApp.get_running_app()
        self.screen_manager = app.screen_manager
        filter_options = ["ROLL_NO", "NAME", "ATTENDANCE"]
        filter_option_item = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{day}",
                "height": dp(40),
                "on_release": lambda x = day: self.filter_callback(x),
            } for day in filter_options
        ]
        self.filter_menu = MDDropdownMenu(
            items = filter_option_item,
            position = "bottom",
            width_mult = 2,
            caller = self,
        )

    def filter_callback(self, obj="ROLL_NO"):
        pass

    def back_button(self, instance):
        self.screen_manager.current = "home"

    def fetch_details(self, rows):
        for row in rows:
            item = ItemDrawer(text=f"{row[0]} {row[1]}", secondary_text=f"{row[2]} {row[3]}", tertiary_text=f"{row[6]}", icon="file-document-box")
            item.bind(on_release=lambda x, entry_id=row[0]: self.student_data(entry_id))
            self.screen_manager.get_screen("home").ids.student_list.add_widget(item)
        self.conn.close()

    def search_option(self):
        self.top_app_bar = self.ids.top_app_bar
        self.search_input = self.ids.search_input
        self.search_button = self.ids.search_button
        
        if not self.search_bar_active:
            anim = Animation(opacity=1, duration=1, transition="out_quart")
            anim.start(self.search_input)
            self.top_app_bar.title = ""
            self.search_bar_active = True
        else:
            anim = Animation(opacity=0, duration=0.5, 
                             transition="in_quart", 
                             )
            self.top_app_bar.title = "Account Details"
            self.search_input.text = ""
            anim.start(self.search_input)
            self.search_bar_active = False

    def search(self, instance, text):
        pass
    
    def student_data(self, entry_id):
        pass