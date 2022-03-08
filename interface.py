from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random


class FirstScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    def upload(self):
        print("upload")
    def download(self):
        print("download")

root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
<FirstScreen>:
    name: 'Menu'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Parachutage'
            font_size: 30
        BoxLayout:
            Button:
                text: 'UPLOAD'
                font_size: 30
                on_release: app.root.upload()
            Button:
                text: 'DOWNLOAD'
                font_size: 30
                on_release: app.root.download()
''')


class ScreenManagerApp(App):
    def build(self):
        return root_widget


ScreenManagerApp().run()