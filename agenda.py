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
        buscar_contato(contato)



def buscar_contato(contato):
    print('Nome: ', contato )
    print('Tel: ', AGENDA[contato]['tel'])
    print('Email: ', AGENDA[contato]['email'])
    print('Endereço: ', AGENDA[contato]['endereco'])

def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'tel': telefone,
        'email': email,
        'endereco': endereco
    }
    print(' Contato: {} adicionado com sucesso!'.format(contato))
    exibir_agenda()



# exibir_agenda()
# buscar_contato('Sheyla')
incluir_contato('Carlota', '98888-8888', 'carlotajoaq@teste.com', 'Mangueiral, 3443')