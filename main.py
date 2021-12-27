from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
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

Builder.load_string("""

<FirstScreen>
    GridLayout:
        rows: 2

        Label:
            text: "QuickMath"

        GridLayout:
            cols: 2

            Button:
                text: "Unit Converters"
                size_hint: 0.1, 0.1
                on_press : 
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = .25
                    root.manager.current = "third"

            Button:
                text: "Calculator"
                size_hint: 0.1, 0.1
                on_press : 
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = .25
                    root.manager.current = "second"


<SecondScreen>
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        Label:
            id:input
            background_color: (0,0,0)
            foreground_color:(255, 255, 255)
            text:"0"
            halign:"right"
            font_size:60
            size_hint:(1, .20)
        GridLayout:
            cols:4
            rows:5
            # first row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"<-"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "first"
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"C"
                on_press:root.clear()
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"%"
                on_press:root.pressed('%')                
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"/"
                on_press:root.pressed('/')
            # second row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"7"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(7)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"8"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(8)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"9"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(9)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"X"
                on_press:root.pressed('*')
            # third row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"4"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(4)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"5"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(5)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"6"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(6)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"-"
                on_press:root.pressed('-')
            # fourth row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"1"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(1)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"2"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(2)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"3"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(3)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"+"
                on_press:root.pressed('+')
            # fifth row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"x[sup]n[/sup]"
                background_color:(157/255,157/255, 157/255, 1)
                markup:True
                on_press:root.pressed('**')
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"0"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(0)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"."
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed('.')
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"="
                on_press:root.answer()


<ThirdScreen>

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            text: ''    

        Label:
            id: click_label
            text: "Pick Unit Below"
            font_size: 32
        Label:
            text: ''

        Spinner:
            id: main_spinner
            text: "length"
            values: ["length", "time", "mass"]

            on_text: root.choice(main_spinner.text, spinner_id, spinner2_id) 

        GridLayout:
            rows: 2
            cols: 2

            TextInput:
                id: from_id
                text: ""
                on_text: root.length(from_id.text, to_id.text, spinner_id.text, spinner2_id.text)

            Spinner:
                id: spinner_id
                text: "-"
                values: ["km", "m", "cm","mm","mil"]



            TextInput:
                id: to_id
                text: ""

            Spinner:
                id: spinner2_id
                text: "-"
                values: ["km", "m", "cm","mm","mil"]

                #on_text: root.spinner_clicked(spinner_id.text)



        Label:
            text: ''
        Label:
            text: ''
        Label:
            text: ''


    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        Button:
            text: "First Screen"
            size_hint: 0.3, 0.1
            #pos: 280,200
            on_press : 
                root.manager.transition.direction = 'left'
                root.manager.current = "first"

""")


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    def clear(self):
        self.ids.input.text = "0"

    def back(self):
        expression = self.ids.input.text
        expression = expression[:-1]
        self.ids.input.text = expression

    # function take button inuputs pressed
    # by user
    def pressed(self, button):
        # expression to store all text field values
        expression = self.ids.input.text
        # if text field expression contains
        # error then set it to empty field
        if "Error" in expression:
            expression = "0"
        # if text filed expression contains
        # 0 then first set the field to empty and
        # display the button text pressed by user
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"

    def answer(self):
        expression = self.ids.input.text
        try:
            # evaluate text field expression
            # using eval() function
            self.ids.input.text = str(eval(expression))

        except:
            # set text field to Error if
            # try block throws an error
            self.ids.input.text = "Error"


class ThirdScreen(Screen):
    def choice(self, main_spinner, spinnerv_id, spinner2v_id):
        if self.ids.main_spinner.text == "length":
            self.ids.spinner_id.values = ['km', 'm', 'cm', 'mm', 'mil']
            self.ids.spinner2_id.values = ['km', 'm', 'cm', 'mm', 'mil']

            self.ids.spinner_id.text = f'-'
            self.ids.spinner2_id.text = f'-'

        if self.ids.main_spinner.text == "mass":
            self.ids.spinner_id.values = ['mg', 'g', 'kg', 't']
            self.ids.spinner2_id.values = ['mg', 'g', 'kg', 't']

            self.ids.spinner_id.text = f'-'
            self.ids.spinner2_id.text = f'-'

        if self.ids.main_spinner.text == "time":
            self.ids.spinner_id.values = ['msec', 'sec', 'min', 'hour', 'day', 'year']
            self.ids.spinner2_id.values = ['msec', 'sec', 'min', 'hour', 'day', 'year']

            self.ids.spinner_id.text = f'-'
            self.ids.spinner2_id.text = f'-'

    # LENGHT

    def length(self, from_value, to_id, value, value2):
        if value == "km" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "km" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 100000}'
        if value == "km" and value2 == "mm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1e+6}'
        if value == "km" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1.609}'
        if value == "m" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "m" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 100}'
        if value == "m" and value2 == "mm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "m" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1609}'
        if value == "cm" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1e-5}'
        if value == "cm" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 100}'
        if value == "cm" and value2 == "mm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 10}'
        if value == "cm" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 160934}'
        if value == "mm" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1e+6}'
        if value == "mm" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "mm" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 10}'
        if value == "mm" and value2 == "mil":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1.609e+6}'
        if value == "mil" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1.609}'
        if value == "mil" and value2 == "m":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1609}'
        if value == "mil" and value2 == "cm":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 160934}'
        if value == "mil" and value2 == "km":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1.609e+6}'

        # MASS

        if value == "mg" and value2 == "g":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "mg" and value2 == "kg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1e+6}'
        if value == "mg" and value2 == "t":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1e+9}'
        if value == "g" and value2 == "mg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "g" and value2 == "kg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "g" and value2 == "t":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1e+6}'
        if value == "kg" and value2 == "mg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1e+9}'
        if value == "kg" and value2 == "g":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "kg" and value2 == "t":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "t" and value2 == "mg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1e+9}'
        if value == "t" and value2 == "g":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1e+6}'
        if value == "t" and value2 == "kg":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1000}'

        # TIME

        if value == "msec" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1000}'
        if value == "msec" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 60000}'
        if value == "msec" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 3.6e+6}'
        if value == "msec" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 8.64e+7}'
        if value == "msec" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 3.154e+10}'
        if value == "sec" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "sec" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 60}'
        if value == "sec" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 3600}'
        if value == "sec" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 86400}'
        if value == "sec" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 3.154e+7}'
        if value == "min" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 60000}'
        if value == "min" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 60}'
        if value == "min" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 60}'
        if value == "min" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 1440}'
        if value == "min" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 525600}'
        if value == "hour" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 3.6e+6}'
        if value == "hour" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 3600}'
        if value == "hour" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 60}'
        if value == "hour" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 24}'
        if value == "hour" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1000}'
        if value == "day" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 8.64e+7}'
        if value == "day" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 86400}'
        if value == "day" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 1440}'
        if value == "day" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 24}'
        if value == "day" and value2 == "year":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) / 365}'
        if value == "year" and value2 == "msec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 3.154e+10}'
        if value == "year" and value2 == "sec":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 3.154e+7}'
        if value == "year" and value2 == "min":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 525600}'
        if value == "year" and value2 == "hour":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 8760}'
        if value == "year" and value2 == "day":
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = f'{int(from_value) * 365}'

        if value == value2:
            if from_value == "":
                from_value = 0
                self.ids.to_id.text = '0'
            else:
                self.ids.to_id.text = from_value


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))

        return sm


MyApp().run()