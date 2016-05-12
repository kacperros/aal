from AppScreen import AppScreen
from kivy.app import App


class AALApp(App):
    def build(self):
        return AppScreen()


if __name__ == '__main__':
    AALApp().run()