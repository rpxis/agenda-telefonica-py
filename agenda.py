agenda = {}

while True:
    print('---- Agenda telefonica ----')
    print('1 - Adicionar contato')
    print('2 - Editar contato (telefone)')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    print('6 - Sair')

    opcao = int(input('Selecione uma opção: '))

    if opcao == 1:
        nome = input('Digite o nome do contato ')
        telefone = int(input('Digite o telefone do contato : '))
        agenda[nome] = telefone
        print('Contato adicionado com sucesso!')
    elif opcao == 2:
        nome = input('Digite o nome do contato que deseja editar: ')
        telefone = input("Digite o novo telefone do contato: ")
        if nome in agenda: 
            agenda[nome] = telefone
            print('Contato alterado com sucesso!')
        else: 
            print('Contato não encontrado!')
    elif opcao == 3:  
        nome = input('Digite o nome do contato:  ')
        if nome in agenda: 
            del agenda[nome]
            print('Contato removido com sucesso!')
        else: 
            print('Contato não encontrado!')
    elif opcao == 4:   
        nome = input('Digite o nome do contato:  ')
        if nome in agenda: 
            print(f'Nome do contato: {nome}, Número do contato: {agenda[nome]}')
        else: 
            print('Contato não encontrado!')
    elif opcao == 5:   
        print(' --- LISTA DE CONTATOS ---')
        for nome in agenda:
            print(f'Nome do contato: {nome}, Número do contato: {agenda[nome]}')
    elif opcao == 6:
        break   
    else:
        print('Opcão invalida')
