AGENDA = {}

AGENDA['Carla'] = {
    'tel': '99999999-99',
    'email': 'ohcarla@teste.com',
    'endereco': '123 Caçaba das aquarelas'
}


def exibir_agenda():
    for contato in AGENDA:
        print('====================================')
        print("Nome: ", contato )
        print("Tel: ", AGENDA[contato]['tel'])
        print("Email: ", AGENDA[contato]['email'])
        print("Endereço: ", AGENDA[contato]['endereco'])


exibir_agenda()