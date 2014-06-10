from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
import Babelrang

class MainScreen(Screen):
	def twist_button(self, in_message):
		br = Babelrang.Babelrang(in_message)
		#self.ids.out_message = br.get_output()[1]

Builder.load_string("""
#:kivy 1.8.0
<MainScreen>:
	canvas:
		Rectangle:
			source: 'Art/bg_whole_fancy.jpg'
			size: self.size
	BoxLayout:
		orientation: 'vertical'
		padding: 20
		spacing: 20
		BoxLayout:
			spacing: 20
			TextInput:
				id: in_message
				hint_text: 'Input'
				multiline: True
			BoxLayout:
				orientation: 'vertical'
				size_hint_x: 0.2
				Label:
				Button:
					id: twist_button
					size_hint_y: 2
					text: 'Twist'
					on_press: root.twist_button(in_message.text)
				Label:
		BoxLayout:
			size_hint_y: 4
			canvas:
				Color:
					rgba: 0, 0, 0, 0.9
				Rectangle:
					pos: self.pos
					size: self.size
			ListView:
				id: steps
				##size_hint_y: 4
				item_strings: [str(index) for index in range(20)]
		TextInput:
			id: out_message
			hint_text: 'Result'
			multiline: True
			readonly: True
""")

class BabelrangApp(App):
	def build(self):
		Window.size = (480,700)
		return MainScreen()
	
if __name__ == '__main__':
	BabelrangApp().run()