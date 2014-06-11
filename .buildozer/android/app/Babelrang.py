#!/usr/bin/env python

import sys
import locale
import random as r
from translate import Translator

lang_array = [['Afrikaans','af'],['Albanian','sq'],['Arabic','ar'],['Armenian','hy'],['Azerbaijani','az'],['Basque','eu'],['Belarusian','be'],['Bulgarian','bg'],['Catalan','ca'],['Chinese','zh-CN'],['Croatian','hr'],['Czech','cs'],['Danish','da'],['Dutch','nl'],['English','en'],['Estonian','et'],['Filipino','tl'],['Finnish','fi'],['French','fr'],['Galician','gl'],['Georgian','ka'],['German','de'],['Greek','el'],['Haitian Creole','ht'],['Hebrew','iw'],['Hindi','hi'],['Hungarian','hu'],['Icelandic','is'],['Indonesian','id'],['Irish','ga'],['Italian','it'],['Japanese','ja'],['Korean','ko'],['Latvian','lv'],['Lithuanian','lt'],['Macedonian','mk'],['Malay','ms'],['Maltese','mt'],['Norwegian','no'],['Persian','fa'],['Polish','pl'],['Portuguese','pt'],['Romanian','ro'],['Russian','ru'],['Serbian','sr'],['Slovak','sk'],['Slovenian','sl'],['Spanish','es'],['Swahili','sw'],['Swedish','sv'],['Thai','th'],['Turkish','tr'],['Ukrainian','uk'],['Urdu','ur'],['Vietnamese','vi'],['Welsh','cy'],['Yiddish','yi']]

output = []

class Babelrang:
	def __init__(self, in_message):
		self.output = self.twist(in_message)

	def twist(self, in_message):
		start_lang = 'en'
		last_lang = 'en'
		sentence =  in_message
		turns = 20

		first_step = ''

		for lang in range(len(lang_array)):
			if start_lang == lang_array[lang][1]:
				first_step += (lang_array[lang][0])

		steps = []
		for turn in range(turns):
			rand_int = r.randint(0,len(lang_array)-1)
			rand_lang = lang_array[rand_int][1]
			translator = Translator(to_lang = rand_lang, from_lang = last_lang)
			sentence = translator.translate(sentence)
			if sys.version_info.major == 2:
				sentence =sentence.encode(locale.getpreferredencoding())
			steps.append([sentence, rand_lang])
			print(str(turn + 1)+ '/' + str(turns) + ' (' + lang_array[rand_int][0] + ')')
			last_lang = rand_lang
		translator = Translator(to_lang = start_lang, from_lang = last_lang)
		sentence = translator.translate(sentence)
		sentence = sentence.capitalize()
		sentence = sentence.replace(' ,', ',')
		sentence = sentence.replace(' .', '.')
		sentence = sentence.replace(' \'', '\'')
		if sentence[len(sentence) - 1] != '.':
			sentence += '.'
		# print('\n' + steps)
		# print('\n' + sentence)
		return [steps, sentence]

	def get_output(self):
		return self.output

if __name__ == '__main__':
	Babelrang()