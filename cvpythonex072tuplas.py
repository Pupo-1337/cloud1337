cont = ('zero', 'um', 'dois', 'três', 'quatro',
		'cinco', 'seis', 'sete', 'oito', 'nove',
		'dez', 'onze', 'doze', 'treze', 'quatorze', 
		'quinze', 'dezesseis', 'dezessete', 'dezoito',
		'dezenove', 'vinte') #Tupla_cont

#while para não deixar o programa rodar com digito errado
while True:
	num= int(input('Digite um número entre 0 e 20'))
	if 0 <= num <= 20:
		break
	print('Tente novamente.', end='')
#limitando oque o usuário deve digitar para seguir o processo
print(f'Você digitou o número {cont[num]}')	