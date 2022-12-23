from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader


class HomePage(Screen):
    pass

class Page1(Screen):
    pass

class Page2(Screen):
    pass

class Page3(Screen):
    pass

class Page4(Screen):
    pass


class Page5(Screen):
    def play_sound(self):
        sound = SoundLoader.load('song.wav')
        if sound:
            sound.play()

class NavigationPage(Screen):
    pass

class ThanksPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainWidget(Widget):
    pass

kv = Builder.load_file('ARO.kv')


class ARO(App):
    def build(self):
        return kv

ARO().run()

