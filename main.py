from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView
from functools import partial
from kivy.core.window import Window
import time
from kivy.base import runTouchApp
from kivy.graphics.texture import Texture


Builder.load_string("""

<FirstScreen>
    Image:
        source: 'gradient.png'
        allow_stretch: True
        keep_ratio: False      
               
    GridLayout:
        rows: 3

        Label:
            text: "QuickMath"
            size_hint_y: 0.2
            size: self.texture_size

    
        GridLayout:
            cols: 3

            Button:
                size_hint_x: 0.6
                size: self.texture_size
                on_press : 
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = .25
                    root.manager.current = "third"
                background_color: 0,0,0,0 
                canvas.before:
                    Color:
                        rgba: (209/255,228/255,238/255,0.3) if self.state=='normal' else (0,.7,.7,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [(0, 0), (100, 100), (100, 100), (0, 0)]
                Image:
                    source: 'conv_logo.png'
                    width: 300
                    height: 300
                    allow_stretch: True
                    keep_ratio: False
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    
            Label:
                text: ""

            Button:
                size_hint_x: 0.6
                size: self.texture_size
                on_press : 
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = .25
                    root.manager.current = "second"
                background_color: 0,0,0,0 
                canvas.before:
                    Color:
                        rgba: (209/255,228/255,238/255,0.3) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [(100, 100), (0, 0), (0, 0), (100, 100)]
                Image:
                    source: 'calc_logo.png'
                    width: 200
                    height: 200
                    allow_stretch: True
                    keep_ratio: False
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    
        Label:
            text: "V-1.0"
            size_hint_y: 0.2
            size: self.texture_size


<SecondScreen>
    Image:
        source: 'gradient (4).png'
        allow_stretch: True
        keep_ratio: False 
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        Label:
            id:input
            background_color: (0,0,0)
            foreground_color:(255, 255, 255)
            text:"0"
            halign:"right"
            font_size:108
            size_hint:(1, .20)
            background_normal: 'gradient_log.png'
        GridLayout:
            cols:4
            rows:5
            spacing: -3
            # first row
            Button:
                size_hint:(.2, .2)
                background_normal: 'Free_Sample_By_Wix2.jfif'
                font_size:32
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "first"
            Button:
                size_hint:(.2, .2)
                font_size:80
                background_color:(2.05, 2.29, 2.29, .6) 
                text:"C"
                on_press:root.clear()
            Button:
                size_hint:(.2, .2)
                font_size:80
                text:"/"
                on_press:root.pressed('/')
            Button:
                size_hint:(.2, .2)
                font_size:80
                on_press:root.back()
                background_color:(2.22,1.08, 1.08, 0.7)
                Image:
                    source: 'backspace.png'
                    image_size: 0.5
                    allow_stretch: True
                    keep_ratio: False
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y          
            # second row
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]7[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(7)
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]8[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(8)
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]9[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(9)
            Button:
                size_hint:(.2, .2)
                font_size:80
                text:"X"
                on_press:root.pressed('*')
            # third row
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]4[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(4)
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]5[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(5)
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]6[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(6)
            Button:
                size_hint:(.2, .2)
                font_size:80
                text:"-"
                on_press:root.pressed('-')
            # fourth row
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]1[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(1)
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]2[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(2)
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]3[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(3)
            Button:
                size_hint:(.2, .2)
                font_size:80
                text:"+"
                on_press:root.pressed('+')
            # fifth row
            Button:                
                markup: True
                size_hint:(.2, .2)
                font_size:60
                text:"[font=Leaner-Thin]x[sup]n[/sup][/font]"
                background_color:(157/255,157/255, 157/255, 1)
                markup:True
                on_press:root.pressed('**')
            Button:
                markup: True
                size_hint:(.2, .2)
                font_size:80
                text:"[font=Leaner-Thin]0[/font]"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(0)
            Button:
                size_hint:(.2, .2)
                font_size:80
                text:"."
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed('.')
            Button:
                size_hint:(.2, .2)
                font_size:80
                background_color:(2.55, 2.22, 1.14, 0.9) 
                text:"="
                on_press:root.answer()


<ThirdScreen>
    Image:
        source: 'gradient.png'
        allow_stretch: True
        keep_ratio: False 

    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            orientation: "vertical"
            GridLayout:
                rows: 1
                cols: 2
                size_hint_y: 0.3
                Spinner:
                    id: main_spinner
                    size_hint_y: 0.3
                    size: self.texture_size
                    text: "Length"
                    values: ["Length", "Time", "Mass"]
                    on_text: root.choice() 
                    animation:
                Button:
                    size_hint:(.2, .2)
                    background_normal: 'Free_Sample_By_Wix.jfif'
                    on_press :
                        root.manager.transition.direction = 'left'
                        root.manager.current = "first"


            GridLayout:
                rows: 2 
                cols: 2
                GridLayout:
                    size_hint_x: 1.5
                    width: 2
                    width: 2
                    rows: 2
                    cols: 1
                    spacing: 1.5
        
                    Label:
                        id: from_id
                        text: "0"
                        text_size: self.size
                        font_size:80
                        background_normal: 'gradient_log.png'
                        color: (1, 1, 1, 1)
                        on_text: root.length(from_id.text, spinner_id.text, spinner2_id.text)
                        
                    Label:
                        id: to_id
                        text: "0"
                        text_size: self.size
                        font_size:80
                        halign: 'left'
                        valign: 'bottom'
                        background_normal: 'gradient_log_2.png'
                        color: (1, 1, 1, 1)
                        #on_text: root.pressed()
        
                GridLayout:
                    rows: 2
                    cols: 1
                    
                    Spinner:
                        id: spinner_id
                        font_size:80
                        text: "-"
                        values: ["km", "m", "cm","mm","mil"]
                        on_text: root.length(from_id.text, spinner_id.text, spinner2_id.text)

        
                    Spinner:
                        id: spinner2_id
                        font_size:80
                        text: "-"
                        values: ["km", "m", "cm","mm","mil"]
                        on_text: root.length(from_id.text, spinner_id.text, spinner2_id.text)

    
        BoxLayout:
            size_hint_y: 1.3
            height: 1.3
            orientation: "vertical"
            size: root.width, root.height
            GridLayout:
                cols:3
                rows:5
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]7[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(7)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]8[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(8)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]9[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(9)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]4[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(4)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]5[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(5)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]6[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(6)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]1[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(1)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]2[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(2)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]3[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(3)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    markup:True
                    on_press:root.back()
                    background_color:(2.22,1.08, 1.08, 1)
                    Image:
                        source: 'backspace.png'
                        image_size: 0.5
                        allow_stretch: True
                        keep_ratio: False
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    font_size:80
                    text:"[font=Leaner-Thin]0[/font]"
                    background_color:(157/255,157/255, 157/255, 1)
                    on_press:root.pressed(0)
                Button:
                    markup: True
                    size_hint:(.2, .2)
                    background_color:(2.05, 2.29, 2.29, .6) 
                    font_size:80
                    text:"[font=Leaner-Thin]C[/font]"
                    on_press:root.clear()


""")


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    def clear(self):
        expression = self.ids.input.text
        self.ids.input.font_size = f"108"
        self.ids.input.text = "0"

    def pressed(self, button):
        # expression to store all text field values
        expression = self.ids.input.text
        #if expression.isdigit() == True:

        if len(expression) == 9:
            self.ids.input.font_size = f"98"
        if len(expression) == 10:
            self.ids.input.font_size = f"88"
        if len(expression) == 11:
            self.ids.input.font_size = f"78"
        if len(expression) == 12:
            self.ids.input.font_size = f"68"
        if len(expression) == 13:
            self.ids.input.font_size = f"68"
        if len(expression) == 14:
            self.ids.input.font_size = f"65"
        if len(expression) == 15:
            self.ids.input.font_size = f"65"

        if len(expression) == 15:
            expression = expression[:-1]
        if len(expression) >= 15:
            self.ids.input.font_size = f'65'


        if button == "+":
            if expression[len(expression)-1] == "+":
                expression = expression[:-1]
        if button == "*":
            if expression[len(expression)-1] == "/":
                expression = expression[:-1]
        if button == "/":
            if expression[len(expression)-1] == "*":
                expression = expression[:-1]


        if "Error" in expression:
            expression = "0"

        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"

    def answer(self):
        expression = self.ids.input.text
        try:
            self.ids.input.text = str(eval(expression))
            round_ = round(float(self.ids.input.text), 9)
            if len(expression) >= 15:
                self.ids.input.text = "{:.2e}".format(expression)
            self.ids.input.text = str(round_)

        except:
            self.ids.input.text = "Error"

    def back(self):
        expression = self.ids.input.text
        expression = expression[:-1]
        if len(expression) == 8:
            self.ids.input.font_size = f"108"
        if len(expression) == 9:
            self.ids.input.font_size = f"98"
        if len(expression) == 10:
            self.ids.input.font_size = f"88"
        if len(expression) == 11:
            self.ids.input.font_size = f"78"
        if len(expression) == 12:
            self.ids.input.font_size = f"68"
        if len(expression) == 13:
            self.ids.input.font_size = f"68"
        if len(expression) == 14:
            self.ids.input.font_size = f"65"
        if len(expression) == 15:
            self.ids.input.font_size = f"65"
        if expression == "":
            expression = "0"
        self.ids.input.text = expression




class ThirdScreen(Screen):
    def choice(self):
        if self.ids.main_spinner.text == "Length":
            self.ids.spinner_id.values = ['km', 'm', 'cm', 'mm', 'mil']
            self.ids.spinner2_id.values = ['km', 'm', 'cm', 'mm', 'mil']

            self.ids.spinner_id.text = f'-'
            self.ids.spinner2_id.text = f'-'

        if self.ids.main_spinner.text == "Mass":
            self.ids.spinner_id.values = ['mg', 'g', 'kg', 't']
            self.ids.spinner2_id.values = ['mg', 'g', 'kg', 't']

            self.ids.spinner_id.text = f'-'
            self.ids.spinner2_id.text = f'-'

        if self.ids.main_spinner.text == "Time":
            self.ids.spinner_id.values = ['msec', 'sec', 'min', 'hour', 'day', 'year']
            self.ids.spinner2_id.values = ['msec', 'sec', 'min', 'hour', 'day', 'year']

            self.ids.spinner_id.text = f'-'
            self.ids.spinner2_id.text = f'-'

    # KEYBOARD

    def pressed(self, button):
        # expression to store all text field values
        expression = self.ids.from_id.text
        # if text field expression contains
        # error then set it to empty field
        if "Error" in expression:
            expression = "0"
        # if text filed expression contains
        # 0 then first set the field to empty and
        # display the button text pressed by user
        if expression == "0":
            self.ids.from_id.text = ""
            self.ids.from_id.text = f"{button}"
        else:
            self.ids.from_id.text = f"{expression}{button}"

    def back(self):
        expression = self.ids.from_id.text
        expression = expression[:-1]
        if expression == "":
            expression = "0"
        self.ids.from_id.text = expression
    def clear(self):
        self.ids.from_id.text = "0"


    # LENGHT

    def length(self, from_value, value, value2):
        if value == "km" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
                self.ids.from_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "km" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 100000}'
        if value == "km" and value2 == "mm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1e+6}'
        if value == "km" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1.609}'
        if value == "m" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "m" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 100}'
        if value == "m" and value2 == "mm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "m" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1609}'
        if value == "cm" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1e-5}'
        if value == "cm" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 100}'
        if value == "cm" and value2 == "mm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 10}'
        if value == "cm" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 160934}'
        if value == "mm" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1e+6}'
        if value == "mm" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "mm" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 10}'
        if value == "mm" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1.609e+6}'
        if value == "mil" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1.609}'
        if value == "mil" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1609}'
        if value == "mil" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 160934}'
        if value == "mil" and value2 == "mm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1.609e+6}'

        # MASS

        if value == "mg" and value2 == "g":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "mg" and value2 == "kg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1e+6}'
        if value == "mg" and value2 == "t":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1e+9}'
        if value == "g" and value2 == "mg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "g" and value2 == "kg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "g" and value2 == "t":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1e+6}'
        if value == "kg" and value2 == "mg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1e+9}'
        if value == "kg" and value2 == "g":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "kg" and value2 == "t":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "t" and value2 == "mg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1e+9}'
        if value == "t" and value2 == "g":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1e+6}'
        if value == "t" and value2 == "kg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1000}'

        # TIME

        if value == "msec" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "msec" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 60000}'
        if value == "msec" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 3.6e+6}'
        if value == "msec" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 8.64e+7}'
        if value == "msec" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 3.154e+10}'
        if value == "sec" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "sec" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 60}'
        if value == "sec" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 3600}'
        if value == "sec" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 86400}'
        if value == "sec" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 3.154e+7}'
        if value == "min" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 60000}'
        if value == "min" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 60}'
        if value == "min" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 60}'
        if value == "min" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 1440}'
        if value == "min" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 525600}'
        if value == "hour" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 3.6e+6}'
        if value == "hour" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 3600}'
        if value == "hour" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 60}'
        if value == "hour" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 24}'
        if value == "hour" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "day" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 8.64e+7}'
        if value == "day" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 86400}'
        if value == "day" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 1440}'
        if value == "day" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 24}'
        if value == "day" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) / 365}'
        if value == "year" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 3.154e+10}'
        if value == "year" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 3.154e+7}'
        if value == "year" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 525600}'
        if value == "year" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 8760}'
        if value == "year" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                if not from_value.isdigit():
                    from_value = "".join(c for c in from_value if c.isdecimal())
                    expression = self.ids.from_id.text
                    expression = expression[:-1]
                    self.ids.from_id.text = expression
                self.ids.to_id.text = f'{int(from_value) * 365}'
        if from_value == "":
            self.ids.to_id.text = '0'
            self.ids.from_id.text = '0'


        if value == value2:
            if from_value == "":
                self.ids.to_id.text = '0'
                self.ids.from_id.text = '0'
            else:
                self.ids.to_id.text = from_value


class MyApp(App):
    def build(self):
        self.icon = "app_logo.png"
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))

        return sm

MyApp().run()


#===================================================================
#*******************************************************************
#        ___        ___________  _______      _______    ___   ______
#       / _ \       | | \   | |  |      |     |  __  |   | |  | _____|
#      / / \ \      | |\ \  | |  |   ___  |   | |  |  |  | | | |
#     / /   \ \     | | \ \ | |  |  |   |  |  | |__| |   | |   | |
#    / /-----\ \    | |  \ \| |  |  |   |  |  |____ |    | |     | |
#   / /-------\ \   | |   \ | |  |  |___|  |  | | | |    | |       | |
#  / /         \ \  | |    \  |  |        |   | |  | |   | |   ___ | |
# / /           \ \ | |     | |  |______|     | |   | |  | |  |_____|
#
#********************************************************************
#====================================================================
