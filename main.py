from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class AirQualityLutskApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Air Quality", halign="center")


AirQualityLutskApp().run()