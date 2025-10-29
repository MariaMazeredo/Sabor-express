""" """ #1- Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número digitado é par")
else:
    print("O número digitado é ímpar")

#2- Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:Criança: 0 a 12 anos;Adolescente: 13 a 18 anos;Adulto: acima de 18 anos.

idade = int(input("Digite sua idade: "))
if idade  >=0 and idade <=12:
    print("Criança")
elif idade >=13 and idade <=18:
    print("Adolescente")
elif idade >18 and idade <=120:
    print("Adulto")
else:
    print("Múmia")

   # Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome
   # de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

from getpass import getpass
import re

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
senha_valida="Python123"
nome_user_valido = "Maria"

nome_user_valido= input("Digite o nome de usuário: ")
if nome_user_valido == "Maria" :
    print("Bem-vinda, Maria! insira a senha para continuar.")
else:
    print("Nome de usuário inválido.")

senha_valida = input("Digite a senha: ")
if senha_valida == "Python123":
    print("Acesso concedido.")
else:
    print("Senha incorreta. Acesso negado.")

#4
coordenadas_x = float(input("Digite a coordenada x: "))
coordenadas_y = float(input("Digite a coordenada y: "))

if coordenadas_x > 0 and coordenadas_y > 0:
    print("O ponto está no primeiro quadrante.")
elif coordenadas_x < 0 and coordenadas_y >0:
    print("O ponto está no segundo quadrante.")
elif coordenadas_x < 0 and coordenadas_y < 0:
    print("O ponto está no terceiro quadrante.")
elif coordenadas_x > 0 and coordenadas_y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está na origem ou em um dos eixos.")

#1 - Crie uma lista para cada informação a seguir:Lista de números de 1 a 10;Lista com quatro nomes;Lista com o ano que você nasceu e o ano atual.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['Regina', 'Regiane', 'Reinaldo', 'Rejane']
lista_anos = [2004, 2025]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

lista_de_compras = ['arroz', 'frango', 'requeijão', 'uvas']
for item in lista_de_compras:
    print(item)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros_impares = [1,3,5,7,9]
soma = 0
for numero in numeros_impares:
    soma += numero
print("A soma dos números ímpares de 1 a 10 é:", soma)

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
numeros= [10,9,8,7,6,5,4,3,2,1]
for numero in numeros:
    print(numero)

#outra possibilidade

for numero in range(10, 0, 1):
    print(numero)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada =int(input("Digite um número para consultar a tabuada: "))
for numero in range(1,11):
    resultado = numero_tabuada * numero
    print(f'{numero_tabuada} X {numero} = {resultado}')

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_numeros = [20, 10, 30, 60]
for numero in lista_numeros:
    try:
        soma += numero
        print(f'O resultado da soma é: {soma}')
    except TypeError:
        print(f'Erro ao somar o valor: {numero}. Certifique-se de que todos os elementos são números.')

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_valores=[50, 21, 22, 23, 49]

try:
    media = sum(lista_valores) / len(lista_valores)
    print(f'A média dos valores na lista é: {media}')
except ZeroDivisionError:
    print('Erro: A lista está vazia. Não é possível calcular a média.')
