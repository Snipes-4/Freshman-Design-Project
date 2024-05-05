from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color

Builder.load_string("""
#:set DECODE_COLOR "#7D2F5C"
#:set ENCODE_COLOR "#EA3033"
#:set LEARN_COLOR "#4A6C6F" 
#:set BACKGROUND_COLOR "#32322C"

<MainScreenButton@Button>
    text_size: self.size
    font_size: 60
    size_hint:(.75, 1)
    pos_hint: {'center_x': .5, 'center_y': .5}
    valign: "middle"
    halign: "center"
    bold: "True"
    background_normal: ""
    
<MainScreen>
    BoxLayout:
        orientation: "vertical"
        padding: 50
        spacing: 30
        MainScreenButton:
            text: "Decode"
            background_color: DECODE_COLOR
            on_release:
                root.manager.transition.direction = "up"
                root.manager.current = "decode"
                
        MainScreenButton:
            text: "Encode"
            background_color: ENCODE_COLOR
            on_release:
                root.manager.transition.direction = "up"
                root.manager.current = "encode"
        MainScreenButton:
            text: "Learn"
            background_color: LEARN_COLOR
            on_release:
                root.manager.transition.direction = "up"
                root.manager.current = "learn"
            
<BackArrow@Button>
    pos_hint: {"top":1, "left":1, "x":.005}
    size_hint: None, None
    size: 60,60
    background_color: (0,0,0,0)
    Image:
        source: "images/backarrow.png"
        pos: self.parent.pos
        size_hint: None, None
        size: self.parent.size
        
<EncodeScreen>
    FloatLayout:
        BackArrow:
            on_release: root.manager.current = "main"
        TextInput:
            id: userinput
            focus: True
            hint_text: "Input message"
            size_hint: .4, .2
            size: self.parent.x, self.parent.y
            pos_hint: {"bottom":1, "left":1}
            padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            font_size: 25
            halign: "center"
            multiline:False
            on_text_validate: encodedmessage.text="encoded ory ong and sawdawdawdwadawdawdawdawdwag" # this is how our message gets encoded
        Label:
            text: "User Input"
            size_hint: userinput.size_hint
            font_size: userinput.font_size
            pos: userinput.x, userinput.y+80
        TextInput:
            id: keyinput
            hint_text: "Input cipher key"
            size_hint: .4, .2
            size: self.parent.x, self.parent.y
            pos_hint: {"bottom":1, "right":1}
            padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            font_size: 25
            halign: "center"
            focus: False
        Label:
            text: "Encoding Key"
            size_hint: userinput.size_hint
            font_size: userinput.font_size
            pos: keyinput.x, keyinput.y+80
        Label:
            id: encodedmessage
            size_hint_y: None
            text_size: self.width, None
            font_size: 40
            height: self.texture_size[1]
            pos_hint: {"center_y":.6}
            padding_x: 30
            
            
            
<DecodeScreen>
    FloatLayout:
        BackArrow:
            on_release: root.manager.current = "main"
        GridLayout:
            rows:3
            rows_minimum: {0: 20, 1: 20, 2: 50}
            Label:
                text:"uhh eerm"
                size_hint_y: .3
            Label:
                text:"what the spruce"
                size_hint_y: .3
                
            GridLayout: 
                cols:3
                GridLayout:
                    rows:2
                    TextInput:
                        hint_text: "Selected Letter"
                    TextInput:
                        hint_text: "Replace with"
                GridLayout:
                    rows:3
                    Button:
                        text:"Clear"
                    Button:
                        text:"Undo"
                    Button:
                        text:"Replace"
                Label:
                    font_size: '40sp'
                    outline_color: 0, 0, 0
                    outline_width: 1
                    text: 'frequency'
                    
    
            
            
            
<LearnScreen>
    FloatLayout:                
        BackArrow:  
            on_release: root.manager.current = "main"
        Carousel:
            # SLIDE 1
            FloatLayout:
                Label:
                    pos_x: -20
                    pos_hint: {"center_y": .83}
                    text: "What is cryptography and what are ciphers?"
                    font_size: '35'
                    bold: True
                Label:
                    text:"Cryptography, at its most basic level, is the practice and study of manipulating messages and information to make communication more secure and private. It is a field that pervades many others, such as mathematics and computer science."
                    pos: (10, 50)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                Label:
                    text:"Ciphers are a particular form of cryptography, in which messages have their letters and words shifted and changed to make them difficult or impossible to understand without a key, a piece of information that allows someone to decode the cipher text. Examples of very basic ciphers are the Caesar cipher and the substitution cipher."
                    pos: (10, -100)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
            # SLIDE 2
            FloatLayout:
                Label:
                    id: title2
                    pos_x: -20
                    pos_hint: {"center_y": .86}
                    text: "History of cryptography"
                    font_size: '35'
                    bold: True
                Label:
                    text:"Cryptography as a practice has existed for thousands of years. The earliest known use of cryptography was around 1900 BCE in Egypt, and many other historical civilizations are known to have used cryptography, such as the Greeks and Romans."
                    pos: (10, title2.y-100)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                Label:
                    text:"One of the most significant discoveries in the history of cryptography was the discovery of frequency analysis, which is a process that measures the frequency of characters or groups of characters to aid in the decoding of cipher text."
                    pos: (10, 0)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                Label:
                    text:"The development of frequency analysis made making secured messages nearly impossible until the development of polyalphabetic cipher, a cipher that utilizes many different substitution alphabets to encode messages."
                    pos: (10, -100)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                Label:
                    text:"Ultimately, modern cryptography is done using the assumption that a system of ciphers itself is not secure enough, and that the protection of a message’s key was the best form of protection and security in the modern age."
                    pos: (10, -190)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
            # SLIDE 2
            FloatLayout:
                Label:
                    id: title2
                    pos_x: -20
                    pos_hint: {"center_y": .86}
                    text: "History of cryptography"
                    font_size: '35'
                    bold: True
                Label:
                    text:"Cryptography as a practice has existed for thousands of years. The earliest known use of cryptography was around 1900 BCE in Egypt, and many other historical civilizations are known to have used cryptography, such as the Greeks and Romans."
                    pos: (10, title2.y-100)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                Label:
                    text:"One of the most significant discoveries in the history of cryptography was the discovery of frequency analysis, which is a process that measures the frequency of characters or groups of characters to aid in the decoding of cipher text."
                    pos: (10, 0)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                Label:
                    text:"The development of frequency analysis made making secured messages nearly impossible until the development of polyalphabetic cipher, a cipher that utilizes many different substitution alphabets to encode messages."
                    pos: (10, -100)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                Label:
                    text:"Ultimately, modern cryptography is done using the assumption that a system of ciphers itself is not secure enough, and that the protection of a message’s key was the best form of protection and security in the modern age."
                    pos: (10, -190)
                    text_size: root.width-90, None
                    size: self.texture_size
                    font_size: '20'
                    
          
""")


class MainScreen(Screen):
    pass


class EncodeScreen(Screen):
    pass


class DecodeScreen(Screen):
    pass


class LearnScreen(Screen):
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
        return sm


if __name__ == '__main__':
    Test().run()
