#1- Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

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




