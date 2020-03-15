import random
alfabeto = 'abcdefghijklmnopqrstuvwxyz.,! '
key      = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'

f = open("cifra.txt", "r")

def gerarKey(alfabeto):
   alfabeto = list(alfabeto)
   random.shuffle(alfabeto)
   return ''.join(alfabeto)

def encrypt(entrada, key, alfabeto):
    keyMap = dict(zip(alfabeto, key))
    return ''.join(keyMap.get(c.lower(), c) for c in entrada)
def decrypt(cifra, key, alfabeto):
	    keyMap = dict(zip(key, alfabeto))
	    return ''.join(keyMap.get(c.lower(), c) for c in cifra)

while(True):
	print('Bem vindo, Escolha uma das opções abaixo')
	print('-----------------------------------------')
	print('Digite 1 - Criptografar mensagem')
	print('Digite 2 - Descriptografar mensagem')
	print('Digite 0 - Para Sair do Programa')
	print('')
	menu = int(input())
	print('')
	if(menu==1):
		print('Escolha a tipo de Entrada de Dados: ')
		print('3 - para ler do arquivo')
		print('4 - para digitar por aqui mesmo')
		sub_entrada = input()
		#print(type(sub_entrada))
		if(sub_entrada=='3'):
			print('lendo arquivo')
			
			entrada = f.read()
			encrypt(entrada, key, alfabeto)
			cifra = encrypt(entrada, key, alfabeto)
			decrypt(cifra, key, alfabeto)
			print('Texto Cifrado',cifra)
			print('')
			continue
		else:
			print('Digite a mensagem a ser Cifrada')
			entrada_user = input()
			encrypt(entrada_user, key, alfabeto)
			cifra = encrypt(entrada_user, key, alfabeto)
			decrypt(cifra, key, alfabeto)
			print('Texto Cifrado',cifra)
			print('')
			continue
	elif(menu == 2):
		print('Escolha a tipo  ')
		print('3 - para descriptografar  do arquivo')
		print('4 - descriptografar do que foi digitado anteriormente')
		sub_entrada = input()
		#print(type(sub_entrada))
		if(sub_entrada =='3'):
			entrada = f.read()
			print('Descriptografando mensagem do arquivo..')
			#decrypt(cifra, key, alfabeto)
			cifra = encrypt(entrada, key, alfabeto)
			print('Texto Cifrado é',cifra)
			print('Texto Decifrado é',entrada)
			
		if(sub_entrada =='4'):
			print('Descriptografando mensagem digitada..')
			cifra = encrypt(entrada_user, key, alfabeto)
			print('Texto Cifrado é',cifra)
			print('Texto Decifrado é',entrada_user)

	elif(menu == 0):
		print('Saindo...')
		break
	else:
		print('Opção Invalida...Tente Novamente')
