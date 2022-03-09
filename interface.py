from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
import API_Call

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



class FirstScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

class LoadDialog(Screen):
    pass

class SaveDialog(Screen):
    pass


class MyScreenManager(ScreenManager):
    def upload(self):
        files = API_Call.liste_fichiers()

root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    UploadScreen:
    LoadDialog:
    SaveDialog:
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
                bold: True
                background_color: "#e67507"
                on_release: 
                    app.root.upload()
                    app.root.current = 'Upload'
            Button:
                text: 'DOWNLOAD'
                font_size: 30
                bold: True
                background_color: "#3e45ff"
                on_release: app.root.download()

<UploadScreen>:
    name: 'Upload'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Upload'
            font_size: 30
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: "Fichiers déjà transmis: "
                    font_size: 20
            BoxLayout:
                orientation: 'vertical'
                Button:
                    text: 'Load'
                    on_release: root.show_load()
            Button:
                text: 'Save'
                on_release: root.show_save()

        BoxLayout:
            TextInput:
                id: text_input
                text: ''

            RstDocument:
                text: text_input.text
                show_errors: True

<LoadDialog>:
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Load"
                on_release: root.load(filechooser.path, filechooser.selection)

<SaveDialog>:
    text_input: text_input
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser
            on_selection: text_input.text = self.selection and self.selection[0] or ''

        TextInput:
            id: text_input
            size_hint_y: None
            height: 30
            multiline: False

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Save"
                on_release: root.save(filechooser.path, text_input.text)

                
            
''')


class ScreenManagerApp(App):
    def build(self):
        return root_widget


ScreenManagerApp().run()