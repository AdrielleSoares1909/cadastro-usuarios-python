

print(" Cadastrar Usuarios ")

print('-' * 30)

usuarios = [] # Criar uma variavel para guardar os usuarios

def email_existe(email): # função para verificar se existe o email cadastrado 
    for usuario in usuarios: # percorre usuario por usuario
        if usuario['email'] == email: # se em usuario o email == email returna alguma coisa
             return True
    return False


def cadastrar_usuario(): # criar funcão para cadastrar usuarios
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')

    if email_existe(email): # se o email for igual ao email ja cadastrado não cadastra 
            print('Erro email ja cadastrado!\n')
            return

    usuario = {
        "nome": nome,
        "email": email
    }
    usuarios.append(usuario) # usar metodo append para adicionar usuarios
    print('Email cadastrado com sucesso!\n') 

def listar_usuarios():
    if not usuarios:
        print('Nenhum usuario cadastrado!')
        return

    print("\n📋 Usuários cadastrados:\n")

    for usuario in usuarios: # pega um usuario de cada vez da lista 
        print(f"nome: {usuario['nome']}"),# printar na tela as informações
        print(f"email: {usuario['email']}")
        print('-' * 30)
    print()


while True:
    print("MENU")
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Sair")

    opcao = input("Escola uma opcao:")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        print("Saindo do sistema.")
    else:
        print("Opacao invalida")








