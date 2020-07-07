from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json


class MainScreen(Screen):
    number = ObjectProperty(None)

    def btn(self):
        #print("Number: ", self.number.text)
        baseurl = "https://ipuresultskg.herokuapp.com/"
        url = baseurl + 'api?rollNo={}&batch=18&semester=1'.format(self.number.text)
        self.request = UrlRequest(url=url, on_success=self.res)

    def res(self, *args):
        self.data = self.request.result
        print(self.data)


class MainApp(MDApp):
    def build(self):
        kv =  Builder.load_file('result.kv')
        return MainScreen()


MainApp().run()
