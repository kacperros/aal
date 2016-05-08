from graph import Graph, MeshLinePlot
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from math import sin
import math




class AppScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(AppScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        grid = GridLayout(spacing=10, size_hint=(1, 0.05))
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
        graph = Graph(xlabel='Number of Elements', ylabel='Time taken', xlog=True, y_ticks_major=5, x_ticks_minor=10,
                      x_ticks_major=1, y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=1, xmax=100000, ymin=0, ymax=50, size_hint=(1, 0.95))
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, math.log(x, 10)) for x in range(1, 10000, 10)]
        plot2 = MeshLinePlot(color=[0, 0, 1, 1])
        plot2.points = [(x, math.log(10*x, 10)) for x in range(1, 100000, 10)]
        graph.add_plot(plot)
        graph.add_plot(plot2)
        self.add_widget(graph)


class AAL(Widget):
    pass

class AALApp(App):
    def build(self):
        return AppScreen()
        #return AAL()


if __name__ == '__main__':
    AALApp().run()