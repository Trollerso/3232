from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
import webbrowser


class WebApp(App):
    def build(self):
        # Устанавливаем размер окна (для тестирования на компьютере)
        Window.size = (300, 100)

        # Создаем кнопку
        button = Button(text='Клацни тут порнуха', on_press=self.open_website)
        return button

    def open_website(self, instance):
        # Указываем URL сайта, который нужно открыть
        webbrowser.open('http://bitly.com/98K8eH')  # Замените на нужный вам сайт


if __name__ == '__main__':
    WebApp().run()