usuarios = []
while True:
    menu = input("Digite o que deseja fazer. 1-Cadastro, 2-Mostrar, 3-Login ou 4-Sair: ")
    
    if menu == '1':
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        ja_existe = False

        for usuario in usuarios:
            if usuario[0] == nome:
                ja_existe = True
                break

        if ja_existe:
            print("Usuário já cadastrado.")
        else:
            usuarios = usuarios + [(nome, senha)]
            print(f"Usuário {nome} cadastrado com sucesso!")

    elif menu == '2':
        if usuarios:
            print("Usuários cadastrados:")
            for usuario in usuarios:
                print(f"- {usuario[0]}")
        else:
            print("Nenhum usuário cadastrado.")

    elif menu == '3':
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        login_sucesso = False

        for usuario in usuarios:
            if usuario[0] == nome and usuario[1] == senha:
                login_sucesso = True
                break

        if login_sucesso:
            print(f"Login bem-sucedido! Bem-vindo, {nome}.")
        else:
            print("Usuário ou senha incorretos.")

    elif menu == '4':
        print("Fim do programa")
        break

    else:
        print("Opção inválida. Tente novamente.")
