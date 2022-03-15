from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

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
        print(self.file + " uploaded")
        self.dismiss_popup()
        res = API_Call.upload(self.file, filename)
        print(res.text, res.status_code)

class WindowManager(ScreenManager):
    pass

class DownloadScreen(Screen):
    def save(self, instance):
        file_chose = instance.text
        if(file_chose == "Sélectionner"):
            return
        res = API_Call.download(file_chose)
        print(res)
    def dropBut(self, instance):
        files = API_Call.liste_fichiers()
        dropdown = DropDown()
        for file in files:
            btn = Button(text=file, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        mainbutton = instance.ids.dropdown
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))



class LoadDialog(Screen):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

kv = Builder.load_file("main.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()

