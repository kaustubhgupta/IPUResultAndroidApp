from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog


class MainScreen(Screen):
    number = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = MDDialog(
            text="Oops! Something seems to have gone wrong with your enrollment number or our server is not responding! Please try again after sometime :/",
            radius=[20, 7, 20, 7],
        )
        self.semester_get = ''
        self.batch_get = ''
        self.menu_items_batch = [{"text": "17"}, {"text": "18"}]
        self.menu_batch = MDDropdownMenu(
            caller=self.ids.drop_batch,
            items=self.menu_items_batch,
            pos_hint={'center_x': .36, 'center_y': .4},
            callback=self.set_batch,
            width_mult=4,
        )
        self.menu_items_semester = [{"text": f"{i}"} for i in range(1, 9)]
        self.menu_semester = MDDropdownMenu(
            caller=self.ids.drop_semester,
            items=self.menu_items_semester,
            pos_hint={'center_x': .6, 'center_y': .4},
            callback=self.set_semester,
            width_mult=4,
        )
        self.request = ''
        self.data = ''

    def set_semester(self, instance):
        self.ids.drop_semester.text = instance.text
        self.semester_get = instance.text
        print(instance.text)
        self.menu_semester.dismiss()

    def set_batch(self, instance):
        self.ids.drop_batch.text = instance.text
        self.batch_get = instance.text
        print(instance.text)
        self.menu_batch.dismiss()

    def btn(self):

        baseurl = "https://ipuresultskg.herokuapp.com/"
        url = baseurl + 'api?rollNo={}&batch={}&semester={}'.format(self.number.text, self.batch_get, self.semester_get)
        self.request = UrlRequest(url=url, on_success=self.res)

    def res(self, *args):
        self.data = self.request.result
        #print(self.data)
        sm = self.ids['screen_manager']
        ans = self.data
        label = self.ids['marks']
        if ans is None:
            self.dialog.open()
        else:
            sm.current = "result-screen"
            marks = ' '.join([' '.join(i) + str('\n') for i in
                              [[j.strip() for j in i.split('  ') if j != ''] for i in ans[0].split('\n')[1:]]])
            to_send = "*MARKS SUMMARY Semester-{}*".format(self.semester_get) + str('\n') + "Name: " + str(
                ans[4]) + str(
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
