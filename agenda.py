AGENDA = {}

AGENDA['Carla'] = {
    'tel': '99999-9999',
    'email': 'ohcarla@teste.com',
    'endereco': '123 Caçaba das aquarelas'
}

AGENDA['Sheyla'] = {
    'tel': '90000-0099',
    'email': 'loiradotcham@teste.com',
    'endereco': 'Aguaraquaba, 2123'
}


def exibir_agenda():
    for contato in AGENDA:
        print('====================================')
        print('Nome: ', contato )
        print('Tel: ', AGENDA[contato]['tel'])
        print('Email: ', AGENDA[contato]['email'])
        print('Endereço: ', AGENDA[contato]['endereco'])


def buscar_contato(contato):
    print('Nome: ', contato )
    print('Tel: ', AGENDA[contato]['tel'])
    print('Email: ', AGENDA[contato]['email'])
    print('Endereço: ', AGENDA[contato]['endereco'])


# exibir_agenda()
buscar_contato('Sheyla')