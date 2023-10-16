
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("PhotoEdit.kv")


class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class Question2Screen(Screen):
    def display_image(self):
        return ""
    def answer_question(self, num):
        if num == "2012":
            self.manager.current = "correct"
        else:
            self.manager.current = "wrong"
class CorrectScreen(Screen):
    def next(self):
        self.manager.current = "question2"

class WrongScreen(Screen):
    def next(self):
        self.manager.current = "question2"

QuizPageApp().run()
