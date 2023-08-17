import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests


    
# print(f"Status Code: {r.status_code}, Content: {r.json()}")

class MyApp(App) :
    # def __init__(self):
    #     self.input_field = None
    #     self.button = None
    #     self.root = None


    def build(self):
        self.root = kivy.uix.boxlayout.BoxLayout(orientation="vertical")

        # Add an input field
        self.input_field = TextInput(text="Enter your text here")
        self.root.add_widget(self.input_field)

        # Add a button
        self.button = Button(text="Click me!")
        self.button.bind(on_press=self.send)

        self.root.add_widget(self.button)

        return self.root
    
    def send(self,button):
        text = self.input_field.text
        print(text)
        requests.post('http://192.168.1.6:8000',headers={"text":text})


MyApp().run()