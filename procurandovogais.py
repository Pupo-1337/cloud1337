palavras=('aprender','programar', 'linguagem', 'foder',
		'python', 'curso', 'bolete', 'futuro', 'paz',
		'xupabife')

for p in palavras: #cada {p} uma palavra e loop.
	print(f'\nNa palabra {p} temos ', end='')
#print formatado no ínicio e fim da linha.
	for letra in p: #cada letra em cada {p}.
		if letra.lower() in 'aeiou':
			print(letra, end='')

def vogal():
	for letra in ():
		if letra in 'aeiou':
			vogal = True
			print(vogal)
		else:
			vogal = False
			print(vogal)

import vogal
vogal()
