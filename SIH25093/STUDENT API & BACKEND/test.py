import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import mainthread

import requests
import threading

kivy.require('2.0.0')

API_URL = "http://127.0.0.1:8000"

class KivyClient(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Click to fetch data")
        self.root.add_widget(self.label)
        
        btn = Button(text="Fetch from API", on_press=self.fetch_data)
        self.root.add_widget(btn)

        return self.root

    def fetch_data(self, instance):
        self.label.text = "Fetching..."
        # Use a new thread for the network request
        threading.Thread(target=self._fetch_data_thread).start()

    def _fetch_data_thread(self):
        try:
            response = requests.get(f"{API_URL}/data")
            response.raise_for_status()
            data = response.json()
            self.update_label(data.get("message", "Error fetching message"))
        except requests.exceptions.RequestException as e:
            self.update_label(f"Connection Error: {e}")

    @mainthread
    def update_label(self, text):
        self.label.text = text

if __name__ == '__main__':
    KivyClient().run()