from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
from decoder import Decoder
from encoder import Encoder

Builder.load_file("main.kv")

class MainScreen(Screen):
    pass

class EncodeScreen(Screen):
    encode_key_text_input = ObjectProperty()
    encode_message_text_input = ObjectProperty()
    encoded_label = ObjectProperty()
    
    def encode_message(self, message, key):
        e1 = Encoder(message, key)
        e1.encode()
        self.encoded_label.text = str(e1)
        

class DecodeScreen(Screen):
    edited_message_label = ObjectProperty()
    original_message_label = ObjectProperty()
    frequency_label = ObjectProperty()
    d1 = ''
    message = ''
    decoder_key = ''
    frequency = ''

    def set_message(self, message):
        DecodeScreen.message = message
    def set_key(self, key):
        DecodeScreen.decoder_key = key

    def on_enter(self):
        self.edited_message_label.text = self.message
        self.original_message_label.text = self.message
        self.d1 = Decoder(self.message)
        self.frequency = ''
        self.d1.frequency()
        for key,value in zip(self.d1.letter_frequency.keys(),self.d1.letter_frequency.values()):
            self.frequency += f"{key} : {value}%        "
        self.frequency_label.text = self.frequency
        if self.decoder_key != '':
            self.d1.generate_key(self.decoder_key)
            self.d1.decode_by_key()
            string_result = "".join(self.d1.message)
            self.edited_message_label.text = string_result

    def replace_letter(self, new_letter: str, select_letter: str):
        if (new_letter != '' and ord(new_letter) in range(97,122)) and select_letter != '':
            self.d1.replace_letter(select_letter, new_letter)
            string_result = "".join(self.d1.message)
            self.edited_message_label.text = string_result

    def undo_letter(self, select_letter: str):
        if select_letter != '':
            self.d1.undo(select_letter)
            string_result = "".join(self.d1.message)
            self.edited_message_label.text = string_result

    def clear_message(self):
        self.d1 = Decoder(self.message)
        self.on_enter()

class WithKeyScreen(Screen):
    message_text_input = ObjectProperty()
    key_text_input = ObjectProperty()

    def submit_messageandkey(self):
        self.message = self.message_text_input.text
        self.key = self.key_text_input.text
        DecodeScreen.set_message(self, self.message)
        DecodeScreen.set_key(self, self.key)
        self.manager.current = 'decode'
        

class WithoutKeyScreen(Screen):
    message_text_input = ObjectProperty()

    def submit_message(self):
        self.message = self.message_text_input.text
        DecodeScreen.set_message(self, self.message)
        self.manager.current = 'decode'

class LearnScreen(Screen):
    pass

class InputScreen(Screen):
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
