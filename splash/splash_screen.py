from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class SplashScreen(Screen):
    def on_enter(self):
        
        Clock.schedule_once(self.to_start, 3)

    def to_start(self, dt):
        self.manager.current = "start"
