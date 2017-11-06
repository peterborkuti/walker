from kivy.core.window import Window
from kivy.uix.widget import Widget


class MyKeyboardListener(Widget):

    def __init__(self, listenerToUp=None, listenerToDown=None, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')

        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.listenerToUp = listenerToUp
        self.listenerToDown = listenerToDown

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        keyname = keycode[1]

        self.listenerToDown(keyname)

        # Return True to accept the key. Otherwise, it will be used by
        # the system.

        return True

    def _on_keyboard_up(self, keyboard, keycode):
        keyname = keycode[1]

        self.listenerToUp(keyname)

        return True