from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json


class MainScreen(Screen):
    number = ObjectProperty(None)

    def btn(self):
        # print("Number: ", self.number.text)
        baseurl = "https://ipuresultskg.herokuapp.com/"
        url = baseurl + 'api?rollNo={}&batch=18&semester=1'.format(self.number.text)
        self.request = UrlRequest(url=url, on_success=self.res)

    def res(self, *args):
        self.data = self.request.result
        print(self.data)
        sm = self.ids['screen_manager']
        sm.current = "result-screen"
        ans = self.data
        label = self.ids['marks']
        if ans is None:
            label.text = "Result not found"
        else:
            marks = ' '.join([' '.join(i) + str('\n') for i in [[j.strip() for j in i.split('  ') if j != ''] for i in ans[0].split('\n')[1:]]])
            to_send = "*MARKS SUMMARY Semester-1*"  + str('\n') + "Name: " + str(ans[4]) + str(
                '\n') + "Enrollment Number: " + str(ans[5]) + str('\n') + "College: " + str(ans[1]) + str('\n') + str(
                "Branch: ") + str(ans[2]) + str('\n') + "Percentage: " + str(ans[10]) + str(
                '%\n') + "College Rank :{}/{}".format(ans[6], ans[7]) + str('\n') + "University Rank :{}/{}\n".format(
                ans[8], ans[9]) + '\nMarks Format\n*Subject  Internal  External  Total*\n\n\n' + marks

            label.text = to_send


class MainApp(MDApp):
    def build(self):
        Builder.load_file('result.kv')
        return MainScreen()


MainApp().run()
