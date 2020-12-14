from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import webbrowser
import certifi as cfi

kv = '''
<MainScreen>:
    name: "Main-Layout"
    number: number
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                name: "home-screen"
                MDLabel:
                    text: "[b]Welcome to IPU Results App[/b]"
                    halign: "center"
                    font_style: "H4"
                    markup: True
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Home"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12

                    Widget:


            Screen:
                name: "about-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "About"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12

                    Widget:

                MDLabel:
                    text: "This app is made as an [b]extension to the current website[/b] and [b]telegram bot[/b].[i] Using this app you can fetch your results which usually come in the form of long PDFs which are difficult to analyse. There are numerous columns with different subject codes which often confuses the student. We aim to resolve this difficulty and make your experience better[/i]. [b]New features, data and functionality will be added as the app progress[/b]. Feel free to drop any message related to any discrepancy or any other suggestion. Check out the contact tab for that."
                    halign: "center"
                    markup: True


            Screen:
                name: "contact-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Contact"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12

                    Widget:
                BoxLayout:
                    orientation: "vertical"
                    MDLabel:
                        text: ""
                    MDList:
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.instagram.com/kaustubhgupta1828/")
                            text: "Instagram"
                            IconLeftWidget:
                                icon: "instagram"

                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.facebook.com/kaustubh.gupta.1828/")
                            text: "Facebook"
                            IconLeftWidget:
                                icon: 'facebook'


                        OneLineAvatarListItem:
                            on_press: root.openweb("https://twitter.com/Kaustubh1828")
                            text: "Twitter"
                            IconLeftWidget:
                                icon: "twitter"

                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.linkedin.com/in/kaustubh-gupta-612767ab/")
                            text: "Linkedin"
                            IconLeftWidget:
                                icon: "linkedin"

                        OneLineAvatarListItem:
                            on_press: root.openweb("https://github.com/kaustubhgupta")
                            text: "GitHub"
                            IconLeftWidget:
                                icon: "gitlab"

                        OneLineAvatarListItem:
                            on_press: root.openweb("https://medium.com/@kaustubhgupta1828")
                            text: "Medium"
                            IconLeftWidget:
                                icon: "medium"

                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.kaustubhgupta.xyz/")
                            text: "Personal Blogging Website"
                            IconLeftWidget:
                                icon: "web"
                    Widget:


            Screen:
                name: "result-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Result"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12

                    Widget:

                MDLabel:
                    halign: "center"
                    text: "[b]Marks Summary[/b]"
                    markup: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                    font_style: "H6"

                MDLabel:
                    id: other_info
                    halign: "center"
                    text: ""
                    markup: True

                MDRectangleFlatButton:
                    text: 'Marks'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_press: root.datatables.open()

            Screen:
                name: "input-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Result"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12

                    Widget:

                MDTextField:
                    id: number
                    hint_text: "Enter your enrollment number"
                    helper_text_mode: "on_focus"
                    icon_right: "account-search"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: None
                    width: 300
                    required: True

                MDRaisedButton:
                    id: drop_semester
                    pos_hint: {'center_x': .6, 'center_y': .4}
                    text: 'Semester'
                    on_release: root.menu_semester.open()

                MDRaisedButton:
                    id: drop_batch
                    pos_hint: {'center_x': .36, 'center_y': .4}
                    text: 'Batch'
                    on_release: root.menu_batch.open()

                MDRectangleFlatButton:
                    text: 'Submit'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_press:
                        root.btn()

                MDLabel:
                    id: loading
                    haling: 'center'
                    text: ''
                    font_style: "H4"
                    theme_text_color: 'Custom'
                    text_color: (1, 0, 0, 1)

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: '8dp'
                padding: '8dp'

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height

                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "logo.png"

                MDLabel:
                    text: "IPU Results App"
                    font_style: "H4"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "From the Creator of IPUResults Website & IPUTelegrambot"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "home-screen"
                            text: "Home"
                            IconLeftWidget:
                                icon: "home"

                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "about-screen"
                            text: "About"
                            IconLeftWidget:
                                icon: 'information'


                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "input-screen"
                            text: "Check Results"
                            IconLeftWidget:
                                icon: "account-search"

                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "contact-screen"
                            text: "Contact"
                            IconLeftWidget:
                                icon: "contacts"

                        OneLineAvatarListItem:
                            on_press: root.openweb("https://ipuresultskg.herokuapp.com/")
                            text: "Visit website"
                            IconLeftWidget:
                                icon: "web"

                        OneLineAvatarListItem:
                            on_press: root.openweb("https://t.me/ipuBOT")
                            text: "Telegram Bot"
                            IconLeftWidget:
                                icon: "telegram"

'''


class MainScreen(Screen):
    number = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog_error = MDDialog(
            text="Oops! Something seems to have gone wrong with your enrollment number or our server is not responding! Please try again after sometime :/",
            radius=[20, 7, 20, 7],
        )
        self.dialog_network = MDDialog(
            text="Oops! No internet available! Please try again after sometime :/",
            radius=[20, 7, 20, 7],
        )
        self.semester_get = ''
        self.batch_get = ''
        self.menu_items_batch = [{"text": "17"},
                                 {"text": "18"}, {"text": "19"}]
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
        self.data = ''
        self.datatables = ''

    def openweb(instance, link):
        webbrowser.open(link)

    def set_semester(self, instance):
        self.ids.drop_semester.text = instance.text
        self.semester_get = instance.text
        self.menu_semester.dismiss()

    def set_batch(self, instance):
        self.ids.drop_batch.text = instance.text
        self.batch_get = instance.text
        self.menu_batch.dismiss()

    def btn(self):
        label = self.ids.loading
        label.text = "Wait! Your result is being prepared :)"
        baseurl = "https://ipubackendapi.herokuapp.com/"
        url = baseurl + 'score?eNumber={}&batch={}&semester={}'.format(
            self.number.text, self.batch_get, self.semester_get)
        self.request = UrlRequest(url=url, on_success=self.res, ca_file=cfi.where(), verify=True)

    def network(self, *args):
        return self.dialog_network

    def res(self, *args):
        self.data = self.request.result
        sm = self.ids['screen_manager']

        if self.data is None:
            self.dialog_error.open()
            self.ids.loading.text = ''

        else:
            sm.current = "result-screen"
            self.ids.loading.text = ''
            marks = [(i, j, k, z, t) for i, j, k, z, t in zip(self.data['result']['subjects'], self.data['result']['int_marks'],
                                                              self.data['result']['ext_marks'], self.data['result']['total_marks'], self.data['result']['grade_points'])]
            info = self.ids['other_info']
            to_send = "[i]Semester-{}".format(self.semester_get) + str('\n') + "Name: " + str(self.data['result']['name']) + str(
                '\n') + "Enrollment Number: " + str(self.data['result']['enroll_num']) + str('\n') + "College: " + str(self.data['result']['college_name']) + str('\n') + str(
                "Branch: ") + str(self.data['result']['branch_name']) + str('\n') + "Percentage: " + str(self.data['result']['percentage']) + str(
                '%\n') + "SGPA: " + str(self.data['result']['sgpa']) + str('\n') + "College Overall Rank :{}/{}".format(self.data['result']['ranks']['college_rank'], self.data['result']['ranks']['college_total']) + str('\n') + "College Branch Rank :{}/{}".format(self.data['result']['ranks']['college_branch_rank'], self.data['result']['ranks']['college_branch_total']) + str('\n') + "University Rank :{}/{}".format(self.data['result']['ranks']['uni_rank'], self.data['result']['ranks']['uni_total']) + str('\n') + "University Branch Rank :{}/{}".format(self.data['result']['ranks']['uni_branch_rank'], self.data['result']['ranks']['uni_branch_total']) + str('[/i]')
            info.text = to_send
            self.datatables = MDDataTable(
                size_hint=(0.9, 0.6),
                row_data=marks,
                rows_num=20,
                column_data=[
                    ("Subject", dp(35)),
                    ("Internal", dp(20)),
                    ("External", dp(20)),
                    ("Total", dp(20)),
                    ("Grade Point", dp(20))
                ]
            )


class MainApp(MDApp):
    def build(self):
        Builder.load_string(kv)
        return MainScreen()


MainApp().run()
