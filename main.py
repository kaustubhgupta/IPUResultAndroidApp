from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class WindowManager(ScreenManager):
    pass


class About(Screen):
    pass


class Contact(Screen):
    pass


class Website(Screen):
    pass


class Telegrambot(Screen):
    pass


class MyGrid(Screen):
    number = ObjectProperty(None)

    def btn(self):
        print("Number: ", self.number.text)
        self.number.text = ''


class ResultApp(MDApp):
    def build(self):
        kv = Builder.load_file('result.kv')
        return kv


ResultApp().run()
