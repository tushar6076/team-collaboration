from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3


class StudentDataScreen(MDScreen):

    def home_button(self, instance):
        self.app = MDApp.get_running_app()
        self.app.screen_manager.current = "home"

    def edit_data_button(self):
        self.row = self.screen_manager.get_screen("home").row
        edit_screen = self.app.screen_manager.current = "edit_data"
        edit_screen.ids.top_app_bar.title += str(self.row[0])
        edit_screen.ids.person_name.text = self.row[1]
        edit_screen.ids.branch_name.text = self.row[2]
        edit_screen.ids.day.text = self.row[3]
        edit_screen.ids.transaction_date.text = self.row[4]
        edit_screen.ids.amount.text = str(self.row[5])
        edit_screen.ids.transaction_type.text = self.row[6]
        edit_screen.ids.received_by.text = self.row[7]

    def delete_entry(self):
        self.conn = sqlite3.connect("account_details.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM entries WHERE id = ?", (self.entry_id,))
        self.conn.commit()
        self.conn.close()
        self.screen_manager.get_screen("home").load_entries()
        self.app.screen_manager.current = "home"