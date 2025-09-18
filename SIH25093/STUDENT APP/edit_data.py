from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3


class EditDataScreen(MDScreen):

    def student_data_button(self, instance):
        self.app = MDApp.get_running_app()
        self.app.screen_manager.current = "student_data"

    def show_options(self, instance):
        self.ids.top_app_bar.left_action_items = [
            ["home", lambda x: self.home_button(x)]
        ]
        self.ids.top_app_bar.right_action_items = [
            ["close", lambda x: self.cancel(instance)],
            ["check", lambda x: self.edit(instance)],
        ]
        if instance.text_hint == "Transaction Date":
            self.screen_manager.get_screen("add_entry").show_date_picker()

        if instance.text_hint == "Day":
            self.screen_manager.get_screen("add_entry").day_menu().open()
        
        if instance.text_hint == "Transaction Type":
            self.screen_manager.get_screen("add_entry").transaction_type_menu().open()

    def home_button(self, instance):
        self.app.screen_manager.current = "home"

    def edit(self, instance):
        row = self.screen_manager.get_screen("home").row
        self.row_item = [str(i) for i in row]
        print(self.row_item)
        if instance.text not in self.row_item:
            self.entry_id = self.screen_manager.get_screen("home").entry_id
            person_name = self.ids.person_name.text
            branch_name = self.ids.branch_name.text
            day = self.ids.day.text
            transaction_date = self.ids.transaction_date.text
            amount = self.ids.amount.text
            transaction_type = self.ids.transaction_type.text
            received_by = self.ids.received_by.text
            self.update_entry(self.entry_id, person_name, branch_name, day, transaction_date, amount, transaction_type, received_by)

    def update_entry(self, entry_id, person_name, branch_name, day, transaction_date, amount, transaction_type, received_by):
        self.conn = sqlite3.connect("account_details.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''UPDATE entries SET person_name = ?, 
                            branch_name = ?, 
                            day = ?, 
                            transaction_date = ?, 
                            amount = ?, 
                            transaction_type = ? 
                            received_by = ? 
                            WHERE id = ?''',
                            (person_name, branch_name, day, transaction_date, amount, transaction_type, received_by, entry_id))
        self.conn.commit()
        self.conn.close()
        self.screen_manager.get_screen("home").view_entry(self.entry_id)

    def cancel(self, instance):
        if instance.text not in self.row_item:
            self.app.screen_manager.current = "view"