from tkinter import *
from tkinter import ttk
import re


class MainApp():

	def __init__(self, root):
		# ~~~~~~~~~~~~~~~~~ RESOURSES ~~~~~~~~~~~~~~~~~
		self.lang = 'ru'
		#
		# Flag icons
		self.flagEN = PhotoImage(file = 'res/uk.png').subsample(20,20)
		self.flagRU = PhotoImage(file = 'res/ru.png').subsample(20,20)

		# Portraits
		self.imageVigenere = PhotoImage(file = 'res/vigenere.png').subsample(2, 2)
		self.imageBabbage = PhotoImage(file = 'res/babbage.png').subsample(2, 2)
		self.imageKasiski = PhotoImage(file = 'res/kasiski.png').subsample(2, 2)

		# Arrays with text for labels
		self.listRU = [
		'Шифр Виженера',
		'Справка',
		'Шифрование',
		'Дешифрование',
		'Введите текст, который хотите зашифровать...',
		'Введите ключевое слово...',
		'Зашифровать',
		'Шифр Вижeнера by fathopert, 2020',
		'Введите текст, который хотите расшифровать...',
		'Расшифровать',
		'Назад',
		'Скопировать',
		'Вставить'
		]

		self.listEN = [
		'Vigenère cipher',
		'Help',
		'Encript',
		'Decript',
		'Type a text for an encryption here...',
		'Type a keyword here...',
		'Encrypt',
		'Vigenère cipher by fathopert, 2020',
		'Type a text for an decryption here...',
		'Decrypt',
		'Back',
		'Copy',
		'Paste'
		]

		self.alphabetRu = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
		self.alphabetEn = 'abcdefghijklmnopqrstuvwxyz'
		self.regexRu = re.compile(r'[а-яА-ЯёЁ0-9]')
		self.regexRuKey = re.compile(r'[а-яА-ЯёЁ]')
		self.regexEn = re.compile(r'[a-zA-Z0-9]')
		self.regexEnKey = re.compile(r'[a-zA-Z]')


		self.text = self.listRU
		

		self.main_page = ttk.Frame(root, width = 400, height = 300)
		self.help_page = ttk.Frame(root, width = 400, height = 300)

		for frame in (self.main_page, self.help_page):
			frame.grid(row=0, column=0, sticky='news')
		

		#------------------- FRONTEND -------------------
		#################### MAIN PAGE ####################
				
		# ~~~~~~~~~~~~~~~~~ HEADER ~~~~~~~~~~~~~~~~~
		#
		#
		# The title
		self.labelHeader = ttk.Label(self.main_page, text = self.text[0])
		self.labelHeader.config(font=("TkDefaultFont", 22))
		self.labelHeader.grid(row = 0, column = 0, pady = 5, padx = 5, stick = 'w')

		# A frame for button
		self.frameForButtons = ttk.Frame(self.main_page)
		self.frameForButtons.grid(row = 0, column = 3, pady = 5, stick = 'e')

		# A button for a language switching
		self.langButton = ttk.Button(self.frameForButtons, image = self.flagEN, command = self.switch_language)
		self.langButton.pack(side = 'left')		

		# A button for documentation opening
		self.helpButton = ttk.Button(self.frameForButtons, text = self.text[1], command = lambda: self.raise_frame(self.help_page))
		self.helpButton.pack(side = 'left', fill = 'y', expand = True)	


		# ~~~~~~~~~~~~~~~~~ BODY ~~~~~~~~~~~~~~~~~
		#
		#
		# A notebook with 2 tabs (encrypt and decrypt)
		self.notebook = ttk.Notebook(self.main_page)
		self.notebook.grid(row = 1, columnspan = 4)

		frame1 = ttk.Frame(self.notebook, width = 400, height = 30)

		frame2 = ttk.Frame(self.notebook, width = 400, height = 30)

		self.notebook.add(frame1, text = self.text[2])
		self.notebook.add(frame2, text = self.text[3])


		# ~~~~~~~~~ ENCRYPT TAB ~~~~~~~~~
		self.encryptText = Text(frame1, width = 50, height = 10)
		self.encryptText.insert('1.0', self.text[4])
		self.encryptText.grid(row = 0, columnspan = 3, stick = 'nwes', pady = 5)


		self.encryptKeyWord = Entry(frame1)
		self.encryptKeyWord.insert(0, self.text[5])
		self.encryptKeyWord.grid(row = 1, columnspan = 2, stick = 'we', pady = 5)

		self.encryptButtonsFrame = ttk.Frame(frame1)
		self.encryptButtonsFrame.grid(row = 1, column = 2, pady = 5, stick = 'e')

		self.cipherButton = ttk.Button(self.encryptButtonsFrame, text = self.text[6], command = lambda: self.encrypt(root, self.encryptText, self.encryptKeyWord, self.lang))
		self.cipherButton.pack(side = 'left')

		self.copyButton = ttk.Button(self.encryptButtonsFrame, text = self.text[11], command = lambda: self.copy_text(root, self.encryptText))
		self.copyButton.pack(side = 'left')

		# ~~~~~~~~~ DECRYPT TAB ~~~~~~~~~
		self.decryptText = Text(frame2, width = 50, height = 10)
		self.decryptText.insert('1.0', self.text[8])
		self.decryptText.grid(row = 0, columnspan = 3, stick = 'nwes', pady = 5)

		self.decryptKeyWord = Entry(frame2)
		self.decryptKeyWord.insert(0, self.text[5])
		self.decryptKeyWord.grid(row = 1, columnspan = 2, stick = 'we', pady = 5)

		self.decryptButtonsFrame = ttk.Frame(frame2)
		self.decryptButtonsFrame.grid(row = 1, column = 2, pady = 5, stick = 'e')

		self.pasteButton = ttk.Button(self.decryptButtonsFrame, text = self.text[12], command = lambda: self.paste_text(root, self.decryptText))
		self.pasteButton.pack(side = 'left')

		self.decipherButton = ttk.Button(self.decryptButtonsFrame, text = self.text[9], command = lambda: self.decrypt(root, self.decryptText, self.decryptKeyWord, self.lang))
		self.decipherButton.pack(side = 'left')


		# ~~~~~~~~~~~~~~~~~ FOOTER ~~~~~~~~~~~~~~~~~
		#
		#
		self.mainPageFooter = ttk.Label(self.main_page, text = self.text[7])
		self.mainPageFooter.grid(row = 2, columnspan = 4)






		#################### HELP PAGE ####################
		# ~~~~~~~~~~~~~~~~~ HEADER ~~~~~~~~~~~~~~~~~
		#
		#
		self.backButton = ttk.Button(self.help_page, text = self.text[10], command = lambda: self.raise_frame(self.main_page) )
		self.backButton.grid(row = 0, column = 3, stick = 'e')

		# ~~~~~~~~~~~~~~~~~ BODY ~~~~~~~~~~~~~~~~~
		#
		#
		self.helpTextFrame = ttk.Frame(self.help_page)
		self.helpTextFrame.grid(row = 1, columnspan = 4, stick = 'nwes')

		self.helpPageText = Text(self.helpTextFrame, width = 48, height = 15)
		self.helpPageText.config(wrap = 'word')
		self.print_text(self.helpPageText, self.lang)

		self.helpPageText.config(state = 'disabled')
		self.helpPageText.grid(row = 0, column = 0, stick = 'nwes')

		self.textScrollbar = ttk.Scrollbar(self.helpTextFrame, orient = 'vertical', command = self.helpPageText.yview)
		self.textScrollbar.grid(row = 0, column = 1, stick = 'ns')

		self.helpPageText.config(yscrollcommand = self.textScrollbar.set)

		# ~~~~~~~~~~~~~~~~~ FOOTER ~~~~~~~~~~~~~~~~~
		#
		#
		self.helpPageFooter = ttk.Label(self.help_page, text = self.text[7])
		self.helpPageFooter.grid(row = 2, columnspan = 4)


	
	#------------------- BACKEND -------------------
	# ~~~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~~~
	#
	#
	def switch_language(self):
		if self.text == self.listRU:
			self.text = self.listEN
			self.lang = 'en'
			self.langButton.config(image = self.flagRU)
		elif self.text == self.listEN:
			self.text = self.listRU
			self.lang = 'ru'
			self.langButton.config(image = self.flagEN)
		#### Translate the main page ####
		# Translate the Header
		self.labelHeader.config(text = self.text[0])
		self.helpButton.config(text = self.text[1])
		# Translate the Body
		self.notebook.tab(0, text = self.text[2])
		self.notebook.tab(1, text = self.text[3])
		# An encrypt tab
		self.encryptText.delete('1.0', 'end')
		self.encryptText.insert('1.0', self.text[4])
		self.encryptKeyWord.delete(0, 'end')
		self.encryptKeyWord.insert(0, self.text[5])
		self.cipherButton.config(text = self.text[6])
		self.copyButton.config(text = self.text[11])
		# An decrypt tab
		self.decryptText.delete('1.0', 'end')
		self.decryptText.insert('1.0', self.text[8])
		self.decryptKeyWord.delete(0, 'end')
		self.decryptKeyWord.insert(0, self.text[5])
		self.decipherButton.config(text = self.text[9])
		self.pasteButton.config(text = self.text[12])
		# Translate the Footer
		self.mainPageFooter.config(text = self.text[7])
		#### Translate the help page ####
		self.helpPageFooter.config(text = self.text[7])
		self.backButton.config(text = self.text[10])
		self.helpPageText.config(state = 'normal')
		self.helpPageText.delete('1.0', 'end')
		self.print_text(self.helpPageText, self.lang)
		self.helpPageText.config(state = 'disabled')


	def print_text(self, text, lang):
		if lang == 'ru':
			# Содержание текста
			text.insert('1.0', 'Шифр Винежера\n')

			text.image_create('insert', image = self.imageVigenere)
			text.insert('end', '\nПортрет Блеза де Виженера\n\n')

			text.insert('end', '   Данный шифр был создан французским дипломатом Блезом де Виженером в 1586 году.\n   Впервые метод дешифрования предложил английский изобретатель Чарльз Бэббидж, вероятно, в 1854 году, но он не опубликовал своих результатов.\n')
			text.image_create('insert', image = self.imageBabbage)
			text.insert('end', '\nПортрет Чарльза Бэббиджа\n\n')
			text.insert('end', '   Первым опубликовал метод дешифрования офицер прусской армии Фридрих Косиски в 1863 году, с тех пор данный метод носит его имя.\n')
			text.image_create('insert', image = self.imageKasiski)
			text.insert('end', '\nПортрет Фридриха Касиски\n\n')
			text.insert('end', 'Литература:\n')
			text.insert('end', 'Сингх С. Книга шифров. Тайная история шифров и их расшифровки //М.: Аст, Астрель. – 2006')
		elif lang == 'en':
			# Содержание текста
			text.insert('1.0', 'Vigenère cipher\n')

			text.image_create('insert', image = self.imageVigenere)
			text.insert('end', '\nPortrait of Blaise de Vigenère\n\n')

			text.insert('end', '   The cipher was developed by French diplomat Blaise de Vigenère in 1586.\n   English inventor Charles Babbage made a decypher method in 1854. But he did not publish his results.\n')
			text.image_create('insert', image = self.imageBabbage)
			text.insert('end', '\nPortrait of Charles Babbage\n\n')
			text.insert('end', '   Prussian infantry officer Friedrich Kasiski was the first who published the decypher method in 1863. This method is called his name.\n')
			text.image_create('insert', image = self.imageKasiski)
			text.insert('end', '\nPortrait of Friedrich Kasiski\n\n')
			text.insert('end', 'Literatuire:\n')
			text.insert('end', 'Singh, Simon. The code book. Vol. 7. New York: Doubleday, 1999')

		# Центрирую заголовок, рисунки и подписи
		text.tag_add('center', '1.0', '3.end')
		text.tag_add('center', '7.0', '8.end')
		text.tag_add('center', '11.0', '12.end')
		text.tag_configure('center', justify = 'center')
		# Шрифт текста:
		text.tag_add('font', '1.0', 'end')
		text.tag_configure('font', font = ("TkDefaultFont", 10))
		# italic для подписей
		text.tag_add('italic', '3.0', '3.end')
		text.tag_add('italic', '8.0', '8.end')
		text.tag_add('italic', '12.0', '12.end')
		text.tag_configure('italic', font = ("TkDefaultFont", 10, 'italic'))
		# Заголовок жирным
		text.tag_add('header', '1.0', '1.end')
		text.tag_configure('header', font = ("TkDefaultFont", 12, 'bold'))

	def raise_frame(self, frame):
		frame.tkraise()

	def encrypt(self, root, text, entry, lang):
		originalText = text.get('1.0','end').lower()
		keyWord = entry.get().lower()
		# Очистить текст от знаков, отличных от букв и цифр
		textClear = ''
		if lang == 'ru':
			for letter in originalText:
				if self.regexRu.search(letter) != None:
					textClear += letter
			if len(textClear) <= 0:
				errorWindow = Toplevel(root)
				errorWindow.title('Ошибка')
				errorWindow.resizable(False, False)
				ttk.Label(errorWindow, text ='Текст должен состоять \nиз цифр и букв русского алфавита', justify = 'center').pack()
		if lang == 'en':
			for letter in originalText:
				if self.regexEn.search(letter) != None:
					textClear += letter
			if len(textClear) <= 0:
				errorWindow = Toplevel(root)
				errorWindow.title('Error')
				errorWindow.resizable(False, False)
				ttk.Label(errorWindow, text ='The text must consist of\nnumbers and Latin letters', justify = 'center').pack()
		# Очистить ключевое от небуквенных знаков
		keywordClear = ''
		if lang == 'ru':
			for letter in keyWord:
				if self.regexRuKey.search(letter) != None:
					keywordClear += letter
			if len(keywordClear) <= 0:
				errorWindow1 = Toplevel(root)
				errorWindow1.title('Ошибка')
				errorWindow1.resizable(False, False)
				ttk.Label(errorWindow1, text ='Ключевое слово должно состоять \nиз букв русского алфавита', justify = 'center').pack()
		if lang == 'en':
			for letter in keyWord:
				if self.regexEnKey.search(letter) != None:
					keywordClear += letter
			if len(keywordClear) <= 0:
				errorWindow1 = Toplevel(root)
				errorWindow1.title('Error')
				errorWindow1.resizable(False, False)
				ttk.Label(errorWindow1, text ='Keyword must consist of\nLatin letters', justify = 'center').pack()
		# Проверка
		# entry.delete(0, 'end')
		# entry.insert(0, keywordClear)
		# text.delete('1.0', 'end')
		# text.insert('1.0', textClear)

		# Перевести ключевое слово в цифры
		# keywordLetterList = []
		# if lang == 'ru':
		# 	for letter in keywordClear:
		# 		num = self.alphabetRu.find(letter)
		# 		keywordLetterList.append(num)
		# if lang == 'en':
		# 	for letter in keywordClear:
		# 		num = self.alphabetEn.find(letter)
		# 		keywordLetterList.append(num)
		
		# Проверка
		# print(keywordLetterList)

		# Зашифровать
		cipherText = ''
		if lang == 'ru':
			for j in range(0, len(textClear)):
				currentAlphabetNum = j % len(keywordClear)
				currentAlphabet = self.alphabetRu.find(keywordClear[currentAlphabetNum])
				currentLetterNum = self.alphabetRu.find(textClear[j])
				if currentLetterNum != -1:
					newLetterNum = (currentLetterNum + currentAlphabet) % len(self.alphabetRu)
					newLetter = self.alphabetRu[newLetterNum]
				else:
					# Это для цифр
					newLetter = textClear[j]
				cipherText += newLetter
		if lang == 'en':
			for j in range(len(textClear)):
				currentAlphabetNum = j % len(keywordClear)
				currentAlphabet = self.alphabetEn.find(keywordClear[currentAlphabetNum])
				currentLetterNum = self.alphabetEn.find(textClear[j])
				if currentLetterNum != -1:
					newLetterNum = (currentLetterNum + currentAlphabet) % len(self.alphabetEn)
					newLetter = self.alphabetEn[newLetterNum]
				else:
					# Это для цифр
					newLetter = textClear[j]
				cipherText += newLetter

		# Проверка
		text.delete('1.0', 'end')
		text.insert('1.0', cipherText)


	def decrypt(self, root, text, entry, lang):
		cipherText = text.get('1.0','end').lower()
		keyWord = entry.get().lower()
		# Очистить текст от знаков, отличных от букв и цифр
		textClear = ''
		if lang == 'ru':
			for letter in cipherText:
				if self.regexRu.search(letter) != None:
					textClear += letter
			if len(textClear) <= 0:
				errorWindow = Toplevel(root)
				errorWindow.title('Ошибка')
				errorWindow.resizable(False, False)
				ttk.Label(errorWindow, text ='Зашифрованный текст должен состоять \nиз цифр и букв русского алфавита', justify = 'center').pack()
		if lang == 'en':
			for letter in cipherText:
				if self.regexEn.search(letter) != None:
					textClear += letter
			if len(textClear) <= 0:
				errorWindow = Toplevel(root)
				errorWindow.title('Error')
				errorWindow.resizable(False, False)
				ttk.Label(errorWindow, text ='An encripted text must consist of \nnumbers and Latin letters', justify = 'center').pack()			
		# Очистить ключевое от небуквенных знаков
		keywordClear = ''
		if lang == 'ru':
			for letter in keyWord:
				if self.regexRuKey.search(letter) != None:
					keywordClear += letter
			if len(keywordClear) <= 0:
				errorWindow1 = Toplevel(root)
				errorWindow1.title('Ошибка')
				errorWindow1.resizable(False, False)
				ttk.Label(errorWindow1, text ='Ключевое слово должно состоять \nиз букв русского алфавита', justify = 'center').pack()
		if lang == 'en':
			for letter in keyWord:
				if self.regexEnKey.search(letter) != None:
					keywordClear += letter
			if len(keywordClear) <= 0:
				errorWindow1 = Toplevel(root)
				errorWindow1.title('Error')
				errorWindow1.resizable(False, False)
				ttk.Label(errorWindow1, text ='Keyword must consist of\nLatin letters', justify = 'center').pack()

		# Перевести ключевое слово в цифры
		# keywordLetterList = []
		# for letter in keywordClear:
		# 	num = self.alphabetRu.find(letter)
		# 	keywordLetterList.append(num)

		# Расшифровать
		clearText = ''
		if lang == 'ru':
			for j in range(len(textClear)):
				currentAlphabetNum = j % len(keywordClear)
				currentAlphabet = self.alphabetRu.find(keywordClear[currentAlphabetNum])
				currentLetterNum = self.alphabetRu.find(textClear[j])
				if currentLetterNum != -1:
					newLetterNum = ((currentLetterNum - currentAlphabet) + len(self.alphabetRu)) % len(self.alphabetRu)
					newLetter = self.alphabetRu[newLetterNum]
				else:
					# Это для цифр
					newLetter = textClear[j]
				clearText += newLetter
		if lang == 'en':
			for j in range(len(textClear)):
				currentAlphabetNum = j % len(keywordClear)
				currentAlphabet = self.alphabetEn.find(keywordClear[currentAlphabetNum])
				currentLetterNum = self.alphabetEn.find(textClear[j])
				if currentLetterNum != -1:
					newLetterNum = ((currentLetterNum - currentAlphabet) + len(self.alphabetEn)) % len(self.alphabetEn)
					newLetter = self.alphabetEn[newLetterNum]
				else:
					# Это для цифр
					newLetter = textClear[j]
				clearText += newLetter

		# Проверка
		text.delete('1.0', 'end')
		text.insert('1.0', clearText)


	def paste_text(self, root, text):
		pasteText = root.clipboard_get()
		text.delete('1.0', 'end')
		text.insert('1.0', pasteText)

	def copy_text(self, root, text):
		copyText = text.get('1.0', 'end')
		root.clipboard_clear()
		root.clipboard_append(copyText)


def main():
	root = Tk()
	root.title('Vigenère cipher')
	root.resizable(False, False)
	app = MainApp(root)
	app.raise_frame(app.main_page)
	root.mainloop()

if __name__ == '__main__': main()