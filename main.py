import locale
import random as r
import sys
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from sys import platform as _platform
from translate import Translator

class MainScreen(Screen):
	lang_array = [['Afrikaans','af'],['Albanian','sq'],['Arabic','ar'],['Armenian','hy'],['Azerbaijani','az'],['Basque','eu'],['Belarusian','be'],['Bulgarian','bg'],['Catalan','ca'],['Chinese','zh-CN'],['Croatian','hr'],['Czech','cs'],['Danish','da'],['Dutch','nl'],['English','en'],['Estonian','et'],['Filipino','tl'],['Finnish','fi'],['French','fr'],['Galician','gl'],['Georgian','ka'],['German','de'],['Greek','el'],['Haitian Creole','ht'],['Hebrew','iw'],['Hindi','hi'],['Hungarian','hu'],['Icelandic','is'],['Indonesian','id'],['Irish','ga'],['Italian','it'],['Japanese','ja'],['Korean','ko'],['Latvian','lv'],['Lithuanian','lt'],['Macedonian','mk'],['Malay','ms'],['Maltese','mt'],['Norwegian','no'],['Persian','fa'],['Polish','pl'],['Portuguese','pt'],['Romanian','ro'],['Russian','ru'],['Serbian','sr'],['Slovak','sk'],['Slovenian','sl'],['Spanish','es'],['Swahili','sw'],['Swedish','sv'],['Thai','th'],['Turkish','tr'],['Ukrainian','uk'],['Urdu','ur'],['Vietnamese','vi'],['Welsh','cy'],['Yiddish','yi']]

	def translate(self, in_message, to_lang, from_lang):
		translator = Translator(to_lang = to_lang, from_lang = from_lang)
		sentence = translator.translate(in_message)
		if sys.version_info.major == 2:
			sentence =sentence.encode(locale.getpreferredencoding())
		return [sentence, to_lang]

	def throw_button(self, in_message):
		self.ids.result_grid.clear_widgets()
		
		native_lang  = 'en'
		to_lang = 'en'
		from_lang = 'en'
		translation = in_message
		out_message = ''

		steps_progbar = ProgressBar(max = 20)
		steps_progbar.value = 0
		popup = Popup(content=steps_progbar, auto_dismiss=False)
		popup.open()

		for index in range(20):
			steps_progbar.value += 1 

			rand_int = r.randint(0,len(self.lang_array)-1)
			to_lang = self.lang_array[rand_int][1]
			translation = self.translate(translation, to_lang, from_lang)[0]
			from_lang = to_lang

			line_box = BoxLayout()
			line_box.add_widget(Image(source = 'Art/Flags/' + self.lang_array[rand_int][1] + '.png', size_hint_x = 0.1))
			step_text = TextInput(text = translation, readonly = True)
			line_box.add_widget(step_text)
			self.ids.result_grid.add_widget(line_box)
		out_message = self.translate(translation, native_lang, from_lang)[0]
		popup.dismiss()
		self.ids.out_message.text = out_message

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
			TextInput:
				id: in_message
				hint_text: 'Input. 120 characters max.'
				multiline: True
				on_text:
					if self.focus == True and len(self.text) > 120: self.text = self.text[:120]
			BoxLayout:
				spacing: 20
				Button
					id: clear_button
					text: 'Clear'
					on_press: in_message.text = ''
				Button:
					id: throw_button
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
                		size_hint_y: 3.5
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