AGENDA = {}

def exibir_agenda():
    for contato in AGENDA:
        buscar_contato(contato)
        print('====================================\n')

def buscar_contato(contato):
    print('Nome: ', contato )
    print('Tel: ', AGENDA[contato]['telefone'])
    print('Email: ', AGENDA[contato]['email'])
    print('Endereço: ', AGENDA[contato]['endereco'])

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print(' Contato: {} adicionado ou editado com sucesso!\n'.format(contato))

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print('Contato: {} Excluído!\n'.format(contato))
    except:
        print('Contato não existe!\n')
    

def menu():
    print('1 - Exibir agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print("6 - Exportar contatos para arquivo de texto")
    print("7 - Importar contatos para arquivo de texto")
    print('0 - Sair')

def ler_detalhes_contato():
    telefone = input('Digite o telefone: ')
    email = input('Digite  o email: ')
    endereco = input('Digite o endereço: ')
    return telefone, email, endereco # retorna também em formato de tupla

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone=AGENDA[contato]['telefone']
                email=AGENDA[contato]['email']
                endereco=AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato,telefone,email,endereco))
        print('Agenda exportada com sucesso\n')
    except Exception as error:
        print('Algum erro ocorreu: {}\n'.format(error))

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes= linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('Arquivo não encontrado\n')
    except Exception as error:
        print('Algum erro ocorreu: {}\n'.format(error))

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                agenda[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco
                }
    except:
        print('Ocorreu algum erro\n')

# programa inicio   
while True:
    menu()
    opcao = input('Digite uma opção: ')
    if opcao == '1':
        exibir_agenda()
    elif opcao == '2':
        contato=input('Qual o nome do contato que deseja buscar?')
        buscar_contato(contato)
    elif opcao == '3':
        contato=input('Digite o nome do contato que deseja incluir: ')
        try:
            AGENDA[contato]
            print('contato já existente \n')
        except:
            telefone, email, endereco = ler_detalhes_contato()# leio cada variável e retorno em suas respectivas variáveis
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato=input('Digite o nome do contato')
        try:
            AGENDA[contato]
            telefone, email, endereco = ler_detalhes_contato()  # leio cada variável e retorno em suas respectivas variáveis
            incluir_editar_contato(contato, telefone, email, endereco)
        except:
            print('Contato inexistente \n')
    elif opcao == '5':
        contato=input('Qual contato que deseja excluir?')
        excluir_contato(contato)
    elif opcao == '6':
        arquivo = input("Digite o nome do arquivo a ser Exportado")
        exportar_contatos(arquivo)
    elif opcao == '7':
        arquivo=input("Digite o nome do arquivo a ser importado")
        importar_contatos(arquivo)

    elif opcao == '0':
        print('Fechando programa...')
        break
    else:
        print('Opção inválida!\n')