from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
from decoder import Decoder

Builder.load_file("main.kv")

class MainScreen(Screen):
    pass


class EncodeScreen(Screen):
    pass


class DecodeScreen(Screen):
    pass


class LearnScreen(Screen):
    pass

class InputScreen(Screen):
    pass

class WithKeyScreen(Screen):
    pass

class WithoutKeyScreen(Screen):
    pass


class Test(App):
    def build(self):
        Window.background_normal = ""
        Window.clearcolor = "#32322C"
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(EncodeScreen(name='encode'))
        sm.add_widget(DecodeScreen(name='decode'))
        sm.add_widget(LearnScreen(name='learn'))
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(WithoutKeyScreen(name='withoutkey'))
        sm.add_widget(WithKeyScreen(name='withkey'))
        return sm


if __name__ == '__main__':
    Test().run()
