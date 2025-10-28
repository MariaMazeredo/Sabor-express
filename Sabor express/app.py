import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir__opcoes():

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def cadastrar_novo_restaurante():
   os.system('clear') # limpa a tela
   print('Cadastro de novo restaurante \n')
   nome_restaurante = input('Digite o nome do restaurante: ')
   restaurantes.append(nome_restaurante)
   print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
   input('Pressione uma tecla para voltar ao menu principal...')
   main()

def listar_restaurantes():
    os.system('clear') # limpa a tela
    print('Lista de restaurantes cadastrados:\n')
    for restaurante in restaurantes:
        print(f'-{restaurante}')
    input('Pressione uma tecla para voltar ao menu principal...')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha a opção desejada:'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar/Desativar restaurante')()
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    exibir_nome_do_programa()
    exibir__opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()
