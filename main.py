from kivymd.app import MDApp
from kivy.lang import Builder
kv = """
Screen:
    MDLabel:
        text: "IPU Results Puller"
        font_style: "H3"
        halign: 'center'

"""


class ResultApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        return Builder.load_string(kv)


ResultApp().run()
