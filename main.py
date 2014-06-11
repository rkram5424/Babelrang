from sys import platform as _platform
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.core.window import Window
import Babelrang

class MainScreen(Screen):
	steps = ListProperty()
	def twist_button(self, in_message):
		br = Babelrang.Babelrang(in_message)
		self.ids.out_message.text = br.get_output()[1]
		self.steps = br.get_output()[0]
		print self.steps

Builder.load_string("""
#:kivy 1.8.0
<MainScreen>:
	canvas:
		Rectangle:
			source: 'Art/bg_whole_fancy.jpg'
			size: self.size
	BoxLayout:
		orientation: 'vertical'
		Image:
			size_hint_y: 0.15
			source: 'Art/Title.png'
		BoxLayout:
			orientation: 'vertical'
			padding: 20
			spacing: 20
			BoxLayout:
				TextInput:
					id: in_message
					hint_text: 'Input'
					multiline: True
				Button:
					id: twist_button
					size_hint_x: 0.2
					text: 'Throw'
					on_press: root.twist_button(in_message.text)
			BoxLayout:
				size_hint_y: 7
				canvas:
					Color:
						rgba: 0, 0, 0, 0.9
					Rectangle:
						pos: self.pos
						size: self.size
				ListView:
					id: steps
					item_strings: [root.steps[index][0] for index in range(len(root.steps))]
			TextInput:
				id: out_message
				hint_text: 'Result'
				multiline: True
				readonly: True
""")

class BabelrangApp(App):
	def build(self):
		if _platform == "linux" or _platform == "linux2" or _platform == "darwin" or _platform == "win32":
			Window.size = (480,700)
		return MainScreen()
	
if __name__ == '__main__':
	BabelrangApp().run()