from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


class MainScreen(Screen):
    number = ObjectProperty(None)

    def btn(self):
        print("Number: ", self.number.text)
        self.number.text = ''


class MainApp(MDApp):
    def build(self):
        kv =  Builder.load_file('result.kv')
        return MainScreen()


MainApp().run()
