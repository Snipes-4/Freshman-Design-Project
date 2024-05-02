from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder

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
    
<MenuScreen>
    BoxLayout:
        orientation: "vertical"
        padding: 50
        spacing: 30
        MainScreenButton:
            text: "Decode"
            background_color: DECODE_COLOR
        MainScreenButton:
            text: "Encode"
            background_color: ENCODE_COLOR
            on_press:
                root.manager.transition.direction = "up"
                root.manager.current = "encode"
        MainScreenButton:
            text: "Learn"
            background_color: LEARN_COLOR
            
<EncodeScreen>
    FloatLayout:
        Button:
            size_hint: (.1,.13)
            pos_hint: {'center_x': 0.05, 'center_y': .93}
            background_color: (0,0,0,0)
            on_release:
                root.manager.current = "main"
            Image:
                source: "images/backarrow.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size_hint: (self.parent.width, self.parent.height)
        
        
""")


class MenuScreen(Screen):
    pass


class EncodeScreen(Screen):
    pass


class Test(App):
    def build(self):
        Window.background_normal = ""
        Window.clearcolor = BG_COLOR
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='main'))
        sm.add_widget(EncodeScreen(name='encode'))
        return sm


if __name__ == '__main__':
    Test().run()
