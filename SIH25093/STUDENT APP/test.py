import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp

# KivyMD uses Kivy's markup language, so the core logic is in Kivy.
# Kivy's webbrowser module handles opening the URL on all platforms.

KV = '''
MDScreen:

    MDLabel:
        text: 
            "For more information, visit the KivyMD " \
            "[ref=https://kivymd.readthedocs.io/en/latest/][color=0000ff][u]documentation[/u][/color][/ref]."
        halign: "center"
        markup: True
        on_ref_press: app.open_link(args[1])
'''

class LinkApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def open_link(self, url):
        """Opens the specified URL in a web browser."""
        webbrowser.open(url)

if __name__ == '__main__':
    LinkApp().run()
