from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from splash.splash_screen import SplashScreen
from Start.start_screen import StartScreen
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

Window.size = (360, 640)
LabelBase.register(name='Gandom', fn_regular='fonts/Gandom.ttf')
LabelBase.register(name='Sade', fn_regular='fonts/A Sade.ttf')
LabelBase.register(name='Sarvenaz', fn_regular='fonts/Digi Sarvenaz.ttf')

class PersianLabel(Label):
    persian_text = StringProperty("") 
    
    def on_persian_text(self, instance, value):
        if value:
            reshaped_text = arabic_reshaper.reshape(value)
            bidi_text = get_display(reshaped_text)
            self.text = bidi_text

class HukhtaApp(App):
    def build(self):
        Builder.load_file("splash/splash.kv")
        Builder.load_file("Start/start.kv")
        fs = ScreenManager(transition = FadeTransition())
        fs.add_widget(SplashScreen(name = "splash"))
        fs.add_widget(StartScreen(name = "start"))

        return fs

HukhtaApp().run()

