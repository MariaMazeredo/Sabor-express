import os

restaurantes = [
    {'nome': 'Lagostine', 'categoria': 'Frutos do mar', 'ativo': 'False'},
    {'nome': 'Doce Sabor', 'categoria': 'Doces e sobremesas', 'ativo': 'True'},
    {'nome': 'Napolini', 'categoria': 'Italiana', 'ativo': 'True'},
]

def exibir_nome_do_programa():
    '''
    Exibe o nome do programa com um print
    
    '''
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir__opcoes():
    ''' Função responsável por exibir as opções do menu'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Função que finaliza o app chamando exibir_subtitulo'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    return # Retorna para a função que chamou esta função

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função limpa o terminal após a execução, exibe o subtitulo daquela seção contornado com *'''
    os.system('clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

    
def cadastrar_novo_restaurante():
   '''Essa função é responsável por cadastrar um novo restaurante
   
   Inputs:
   - Nome do restaurante
   - Categoria

   Output:
   -adiciona um novo restaurante a lista de restaurantes
   
   '''
   exibir_subtitulo('Cadastrar novo restaurante')
   nome_restaurante = input('Digite o nome do restaurante: ')
   categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
   dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': 'False'}
   restaurantes.append(dados_restaurante)
   print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')

   voltar_ao_menu_principal()

def alterar_status_restaurante():
    '''Essa função é responsável por alterar o status do restaurante para ativo ou inativo'''
    exibir_subtitulo('Alternar status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            break  # Importante: interrompe o loop assim que o restaurante é encontrado

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado na lista.\n')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por exibir uma lista com todos os restaurantes cadastrados expecificando nome, categoria e se está ativo'''
    exibir_subtitulo('Lista de restaurantes cadastrados')

    print(f'{'|Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        status = 'Ativo' if ativo else 'Inativo'  # Exibe "Ativo" ou "Inativo" corretamente
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | Status: {status}')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável pela lógica na escolha de opções do menu direcioando conforme escolha do user'''
    try:
        opcao_escolhida = int(input('Escolha a opção desejada:'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
    Função principal do programa.

    Exibe continuamente o nome do programa e o menu de opções,
    aguardando a escolha do usuário. O loop principal mantém o 
    programa em execução até que o usuário selecione a opção de saída.
    
    '''
    while True:
        exibir_nome_do_programa()
        exibir__opcoes()
        escolher_opcao()
    

if __name__ == '__main__':
    main()
