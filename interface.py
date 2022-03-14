from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
import API_Call

import os


class Accueil(Screen):
    pass

class UploadScreen(Screen):
    loadfile = ObjectProperty(None)
    file = ""

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Sélectionner un fichier", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.file = os.path.join(path, filename[0])
        print(self.file)
        self.dismiss_popup()
        res = API_Call.upload(self.file, filename)
        print(res.text, res.status_code)

class WindowManager(ScreenManager):
    pass

class DownloadScreen(Screen):
    def save(self):
        res = API_Call.download('upload.txt')
        print(res)

class LoadDialog(Screen):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

kv = Builder.load_file("main.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()

