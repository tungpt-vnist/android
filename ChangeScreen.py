import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
class MainWindow(GridLayout):
    pass

kv = Builder.load_file("screen.kv")
class MyMainApp(App):

    def build(self):
        return MainWindow()

if __name__ == '__main__':
    MyMainApp().run()