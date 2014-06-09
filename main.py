from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import Babelrang

class MainScreen(Screen):
	def twist_button(self, in_message):
		br = Babelrang.Babelrang(in_message)
		#self.ids.out_message = br.get_output()[1]

Builder.load_string("""
#:kivy 1.8.0
<MainScreen>:
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
				text: 'Twist'
				on_press: root.twist_button(in_message.text)
		ScrollView:
			id: steps
			size_hint_y: 4
		TextInput:
			id: out_message
			hint_text: 'Result'
			multiline: True
			readonly: True
""")

class KGBerryKrunchApp(App):
	def build(self):
		return MainScreen()
	
if __name__ == '__main__':
	KGBerryKrunchApp().run()