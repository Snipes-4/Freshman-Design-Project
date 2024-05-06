from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView

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
                root.manager.current = "encode"
            
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
            hint_text: "Input message"
            size_hint: .4, .2
            size: self.parent.x, self.parent.y
            pos_hint: {"bottom":1, "left":1}
            padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            font_size: 25
            halign: "center"
        Label:
            text: "User Input"
            size_hint: userinput.size_hint
            font_size: userinput.font_size
            pos: userinput.x, userinput.y+80
        TextInput:
            id: encodedinput
            hint_text: "Encoded message"
            size_hint: .4, .2
            size: self.parent.x, self.parent.y
            pos_hint: {"bottom":1, "right":1}
            padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            font_size: 25
            halign: "center"
        Label:
            text: "Encoded Input"
            size_hint: userinput.size_hint
            font_size: userinput.font_size
            pos: encodedinput.x, encodedinput.y+80

            
            
<DecodeScreen>
    FloatLayout:
        BackArrow:
            on_release: root.manager.current = "main"
        TextInput:
            multiline: False
            size_hint: (.5, .1)
    GridLayout:
        cols: 1
        spacing: 10
        size_hint_y: None
            
            
<LearnScreen>
    FloatLayout:                
        BackArrow:  
            on_release: root.manager.current = "main"  
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
