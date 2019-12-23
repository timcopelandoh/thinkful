from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class LoginScreen(Widget):
	pass

class LoanApp(App):
	def build(self):
		window = LoginScreen()
		return window

if __name__ == '__main__':
	LoanApp().run()