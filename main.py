from kivy.app import App
from kivy.uix.label import Label


class CarpetApp(App):
    def build(self):
        return Label(text="Carpet Map App")


CarpetApp().run()
