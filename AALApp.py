from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from numpy.f2py.crackfortran import multilinepattern


class AppScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(AppScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        grid = GridLayout()
        grid.cols = 7
        grid.add_widget(Label(text='A length'))
        grid.a_len = TextInput(multiline=False)
        grid.add_widget(grid.a_len)
        grid.add_widget(Label(text='B length'))
        grid.b_len = TextInput(multiline=False)
        grid.add_widget(grid.b_len)
        grid.add_widget(Label(text='N'))
        grid.nth_elem = TextInput(multiline=False)
        grid.add_widget(grid.nth_elem)
        grid.go_button = Button(text='GO!')
        grid.add_widget(grid.go_button)
        self.add_widget(grid)
        self.add_widget(Label(text='Label'))



class AALApp(App):
    def build(self):
        return AppScreen()


if __name__ == '__main__':
    AALApp().run()