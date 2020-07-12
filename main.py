import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class Touch(Widget):
    btn = ObjectProperty(None)
    def on_touch_down(self, touch):
        print("down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("mpve", touch)
    def on_touch_up(self, touch):
        print("up", touch)
        self.btn.opacity = 1



class MyWidget(Widget):
    name = ObjectProperty(None)
    password = ObjectProperty(None)

    def btn(self):
        print("nama : ", " ", self.name.text, "Password : ", " ", self.password.text)
        self.name.text = ""
        self.password.text = ""

class MyApp(App):
    def build(self):


        return Touch()






if __name__ == "__main__":
    MyApp().run()
