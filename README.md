# Sistema de Cadastro, Login e Exibição de Usuários

Este é um projeto simples em Python que implementa um sistema de menu interativo para cadastro de usuários, exibição de usuários cadastrados e login.

## Funcionalidades

O programa permite que o usuário:

1. **Cadastrar** um novo usuário com nome e senha.
2. **Mostrar** todos os usuários cadastrados.
3. **Realizar login** verificando nome e senha.
4. **Sair** do programa.

## Como Funciona

O código utiliza uma lista para armazenar os usuários, onde cada usuário é representado por uma tupla contendo seu nome e sua senha.

As opções disponíveis no menu são:

- **1: Cadastro** - Permite que um novo usuário seja cadastrado com nome e senha.
- **2: Mostrar** - Exibe todos os nomes de usuários cadastrados.
- **3: Login** - Verifica se o nome e a senha fornecidos correspondem a um usuário cadastrado.
- **4: Sair** - Encerra o programa.

## Exemplo de Execução

```bash
Digite o que deseja fazer. 1-Cadastro, 2-Mostrar, 3-Login ou 4-Sair: 1
Digite seu nome: Levi
Digite sua senha: 12345
Usuário Levi cadastrado com sucesso!

Digite o que deseja fazer. 1-Cadastro, 2-Mostrar, 3-Login ou 4-Sair: 2
Usuários cadastrados:
- Levi

Digite o que deseja fazer. 1-Cadastro, 2-Mostrar, 3-Login ou 4-Sair: 3
Digite seu nome: Levi
Digite sua senha: 12345
Login bem-sucedido! Bem-vindo, Levi.

Digite o que deseja fazer. 1-Cadastro, 2-Mostrar, 3-Login ou 4-Sair: 4
Fim do programa