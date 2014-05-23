#!/usr/bin/env python

import sys
import random as r
from translate import Translator

lang_array = [['Afrikaans','af'],['Albanian','sq'],['Arabic','ar'],['Armenian','hy'],['Azerbaijani','az'],['Basque','eu'],['Belarusian','be'],['Bulgarian','bg'],['Catalan','ca'],['Chinese','zh-CN'],['Croatian','hr'],['Czech','cs'],['Danish','da'],['Dutch','nl'],['English','en'],['Estonian','et'],['Filipino','tl'],['Finnish','fi'],['French','fr'],['Galician','gl'],['Georgian','ka'],['German','de'],['Greek','el'],['Haitian Creole','ht'],['Hebrew','iw'],['Hindi','hi'],['Hungarian','hu'],['Icelandic','is'],['Indonesian','id'],['Irish','ga'],['Italian','it'],['Japanese','ja'],['Korean','ko'],['Latvian','lv'],['Lithuanian','lt'],['Macedonian','mk'],['Malay','ms'],['Maltese','mt'],['Norwegian','no'],['Persian','fa'],['Polish','pl'],['Portuguese','pt'],['Romanian','ro'],['Russian','ru'],['Serbian','sr'],['Slovak','sk'],['Slovenian','sl'],['Spanish','es'],['Swahili','sw'],['Swedish','sv'],['Thai','th'],['Turkish','tr'],['Ukrainian','uk'],['Urdu','ur'],['Vietnamese','vi'],['Welsh','cy'],['Yiddish','yi']]

class TongueTornado:
	def __init__(self):
		self.guify()
		self.twist()

	def twist(self):
		start_lang = 'en'# sys.argv[1]
		last_lang = 'en'# sys.argv[1]
		sentence = sys.argv[1]
		turns = 20 # r.randint(15,25) # I can't decide if I want it to run 20 times or a rand(10,20)

		first_step = ''

		for lang in range(len(lang_array)):
			if start_lang == lang_array[lang][1]:
				first_step += (lang_array[lang][0])

		steps = (first_step + ' -> ')
		for turn in range(turns):
			rand_int = r.randint(0,len(lang_array)-1)
			rand_lang = lang_array[rand_int][1]
			steps += (lang_array[rand_int][0] + ' -> ')
			translator = Translator(to_lang = rand_lang, from_lang = last_lang)
			sentence = translator.translate(sentence)
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
		steps += first_step
		print('\n' + steps)
		print('\n' + sentence)

	def guify(self):
		pass

if __name__ == '__main__':
	TongueTornado()