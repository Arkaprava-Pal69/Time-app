# from kivy.app import App
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime

class ClockLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_time()
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        self.text = datetime.now().strftime("%H:%M:%S")

class ClockApp(App):
    def build(self):
        return ClockLabel()

if __name__ == "__main__":
    app = ClockApp()
    app.icon = "parrot.jpg"   # 👈 REAL CLOCK APP ICON
    app.run()
