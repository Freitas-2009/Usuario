print("------------------🔑 SISTEMA DE USUARIOS 🔑--------------------")                                                                                                                                                                                                                                                  
print("")
print("✅ SEJA BEM VINDO ✅")

def Cadastar(usuarios):
    Novo_user = input("Digite o nome do usuario: ")
    usuarios.append(Novo_user)
    print(f"✅ Usuário {Novo_user} adicionado com sucesso ✅")

def Listar(usuarios):
    if usuarios:
        for i, usuarios in enumerate(usuarios, start=1):
            print(f"{i}. {usuarios}")
    else:
        print("⚠️   Nenhum usuário cadastrado ainda ⚠️")

def Remover(usuario):
    Remove_user = input("Digite qual usuario deseja remover: ")
    usuarios.remove(Remove_user)
    print(f"{Remove_user} removido com sucesso ❌")

usuarios = []

while True:
  
    print("----------------------------------------------")
    print("1 - Cadastrar Usuario")
    print("2 - Listar Usuarios")
    print("3 - Remover Usuario")
    print("0 - Sair do Programa")
    print("----------------------------------------------")
    
    opção = input("Digite uma das opções: ")
    
    print("----------------------------------------------")
    if opção == "1":
        Cadastar(usuarios)
   
    elif opção == "2":
        Listar(usuarios)
    
    elif opção == "3":
        Remover(usuarios)

    elif opção == "0":
        print("Fechando programa... Até logo✨")
        break