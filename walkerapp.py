from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty

from keyboard import MyKeyboardListener

from kivy.clock import Clock

class Walker(Widget):
    dx = NumericProperty(0)
    dy = NumericProperty(0)

    d = ReferenceListProperty(dx, dy)

    def __init__(self, **kwargs):
        super(Walker, self).__init__(**kwargs)

    def move(self, *args):
        self.pos = Vector(self.d) + self.pos


class WalkerGame(Widget):
    walker = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(WalkerGame, self).__init__(**kwargs)

        self.keyboard = MyKeyboardListener(listenerToDown=self.keyDownListener, listenerToUp=self.keyUpListener)

        Clock.schedule_interval(self.walker.move, 0)

    def keyDownListener(self, text):
        if text in ['up', 'down']:
            self.walker.dy = 1 if text == 'up' else -1
        elif text in ['left', 'right']:
            self.walker.dx = 1 if text == 'right' else -1

    def keyUpListener(self, text):
        if text in ['up', 'down']:
            self.walker.dy = 0
        elif text in ['left', 'right']:
            self.walker.dx = 0


class WalkerApp(App):
    def build(self):
        return WalkerGame()


if __name__ == '__main__':
    WalkerApp().run()