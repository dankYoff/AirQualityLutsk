from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class AirQualityApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Air Quality", halign="center")


AirQualityApp().run()