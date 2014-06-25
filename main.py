from sys import platform as _platform
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.core.window import Window
import Babelrang

class MainScreen(Screen):
	steps = ListProperty()
	def throw_button(self, in_message):
		self.ids.result_grid.clear_widgets()
		br = Babelrang.Babelrang(in_message)
		self.ids.out_message.text = br.get_output()[1]
		self.steps = br.get_output()[0]
		print self.steps
		for index in range(len(self.steps)):
			line_box = BoxLayout()
			line_box.add_widget(Image(source = 'Art/Flags/' + self.steps[index][1] + '.png', size_hint_x = 0.1))
			step_text = TextInput(text = self.steps[index][0], readonly = True)
			line_box.add_widget(step_text)
			self.ids.result_grid.add_widget(line_box)
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
					hint_text: 'Message to Translate. 250 characters max.'
					multiline: True
				Button:
					id: throw_button
					size_hint_x: 0.2
					text: 'Throw'
					on_press: root.throw_button(in_message.text)
			BoxLayout:
				size_hint_y: 7
				canvas:
					Color:
						rgba: 0, 0, 0, 0.9
					Rectangle:
						pos: self.pos
						size: self.size
				ScrollView:
					GridLayout:
						padding: 10
						spacing: 10
                		size_hint_y: 4
                		width: 500
						id: result_grid
						cols: 1
						rows: 20
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