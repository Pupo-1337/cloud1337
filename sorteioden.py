def quebra():
	print('¬'*37)
quebra()

from random import randint #importando modulo
							#para randomizar
							#elementos da tupla

numeros= (randint(1, 10), randint(1, 10), 
	randint(1, 10), randint(1, 10),
	randint(1, 10),randint(1, 10),
	randint(1, 10),randint(1, 10))
quebra()	
print(f'Eu sorteei os valores{n}', end='')
quebra()
#O 'end=' aqui ao fim da linha mantém a próxima linha 
#nessa mesma linha

for n in numeros:
	print(f'{n}', end='')

print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')

