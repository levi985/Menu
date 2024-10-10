usuarios = []
while True:
    m = input("Digite o que deseja fazer. 1-Cadastro, 2-Mostrar, 3-Login ou 4-Sair: ")
    if m == '1':
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        ex = False
        for usuario in usuarios:
            if usuario[0] == nome:
                ex = True
                break
        if ex:
            print("Usuário já cadastrado.")
        else:
            usuarios = usuarios + [(nome, senha)]
            print(f"Usuário {nome} cadastrado com sucesso!")
    elif m == '2':
        if usuarios:
            print("Usuários cadastrados:")
            for usuario in usuarios:
                print(f"- {usuario[0]}")
        else:
            print("Nenhum usuário cadastrado.")
    elif m == '3':
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        ls = False
        for usuario in usuarios:
            if usuario[0] == nome and usuario[1] == senha:
                ls = True
                break
        if ls:
            print(f"Login bem-sucedido! Bem-vindo, {nome}.")
        else:
            print("Usuário ou senha incorretos.")
    elif m == '4':
        print("Fim do programa")
        break
    else:
        print("Opção inválida. Tente novamente.")
