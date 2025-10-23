import os

print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

print('1. Cadastrar restaurante')
print('2. Listar restaurantes')
print('3. Ativar/Desativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha a opção desejada:'))

def finalizar_app():
    os.system('clear') # limpa a tela
    print('Encerrando o aplicativo. Até logo!\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar/Desativar restaurante')
else:
    finalizar_app()