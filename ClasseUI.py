from Classes import Cliente, Categoria, Produto
from ClassesEstaticas import Clientes, Categorias, Produtos

class UI:
    @staticmethod
    def main():
        while True:
            UI.menu()

            operation = input("Selecione a opção desejada: ")

            if operation == '1':
                print("\nVocê selecionou a opção CLIENTES. O que deseja fazer?")
                print("\t1 - Listar Clientes")
                print("\t2 - Inserir Cliente")
                print("\t3 - Atualizar Cliente")
                print("\t4 - Excluir Cliente")
                
                while True:
                    op = int(input("Escolha uma opção: "))
                    
                    if op == 1:
                        UI.Cliente_Listar()
                        break
                    elif op == 2:
                        UI.Cliente_Inserir()
                        break
                    elif op == 3:
                        UI.Cliente_Atualizar()
                        break
                    elif op == 4:
                        UI.Cliente_Excluir()
                        break
                    else:
                        print("Opção inválida, tente novamente.")
            
            elif operation == '2':
                print("\nVocê selecionou a opção CATEGORIAS. O que deseja fazer?")
                print("\t1 - Listar Categorias")
                print("\t2 - Inserir Categoria")
                print("\t3 - Atualizar Categoria")
                print("\t4 - Excluir Categoria")
                
                while True:
                    op = int(input("Escolha uma opção: "))
                    
                    if op == 1:
                        UI.Categoria_Listar()
                        break
                    elif op == 2:
                        UI.Categoria_Inserir()
                        break
                    elif op == 3:
                        UI.Categoria_Atualizar()
                        break
                    elif op == 4:
                        UI.Categoria_Excluir()
                        break
                    else:
                        print("Opção inválida, tente novamente.")

            elif operation == '3':
                if not Categorias.Listar():
                            print("Nenhuma categoria cadastrada. Crie uma nova categoria primeiro.")
                else:
                    print("\nVocê selecionou a opção PRODUTOS. O que deseja fazer?")
                    print("\t1 - Listar Produtos")
                    print("\t2 - Inserir Produto")
                    print("\t3 - Atualizar Produto")
                    print("\t4 - Excluir Produto")
                    
                    while True:
                        op = int(input("Escolha uma opção: "))
                        
                        if op == 1:
                            UI.Produto_Listar()
                            break
                        elif op == 2:
                            UI.Produto_Inserir()
                            break
                        elif op == 3:
                            UI.Produto_Atualizar()
                            break
                        elif op == 4:
                            UI.Produto_Excluir()
                            break
                        else:
                            print("Opção inválida, tente novamente.")

            elif operation == '4':
                print("Finalizando o programa...")
                print(">>> SISTEMAS ENCERRADO COM SUCESSO! <<<")
                break
            
            else:
                print("Opção inválida, tente novamente.")

    @staticmethod
    def menu():
        print("\n:::::::::::::::::::::::::::::::::::::::::::\n")
        print(">>> BEM VINDO AO SISTEMA DE COMÉRCIO ELETRÔNICO <<<\n")
        print("[ [1] - CLIENTES ]\t[ [2] - CATEGORIAS ]\n")
        print("[ [3] - PRODUTOS ]\t[ [4] - ENCERRAR O SISTEMA ]")

    # Métodos para Clientes
    @staticmethod
    def Cliente_Listar():
        clientes = Clientes.Listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)

    @staticmethod
    def Cliente_Inserir():
        id = input("Digite o ID do cliente: ")
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        fone = input("Digite o telefone do cliente: ")
        cliente = Cliente(id, nome, email, fone)
        Clientes.Inserir(cliente)
        print(f"Cliente '{nome}' cadastrado com sucesso.")

    @staticmethod
    def Cliente_Atualizar():
        id = input("Digite o ID do cliente que deseja atualizar: ")
        cliente = Clientes.Listar_Id(id)
        if cliente:
            nome = input("Digite o novo nome (ou pressione Enter para manter): ")
            email = input("Digite o novo email (ou pressione Enter para manter): ")
            fone = input("Digite o novo telefone (ou pressione Enter para manter): ")
            Clientes.Atualizar(id, nome=nome, email=email, fone=fone)
            print(f"Cliente '{id}' atualizado com sucesso.")
        else:
            print("Cliente não encontrado.")

    @staticmethod
    def Cliente_Excluir():
        id = input("Digite o ID do cliente que deseja excluir: ")
        cliente = Clientes.Listar_Id(id)
        if cliente:
            Clientes.Excluir(id)
            print(f"Cliente '{id}' excluído com sucesso.")
        else:
            print("Cliente não encontrado.")

    # Métodos para Categorias
    @staticmethod
    def Categoria_Listar():
        categorias = Categorias.Listar()
        if not categorias:
            print("Nenhuma categoria cadastrada.")
        else:
            for categoria in categorias:
                print(categoria)

    @staticmethod
    def Categoria_Inserir():
        id = input("Digite o ID da categoria: ")
        descricao = input("Digite a descrição da categoria: ")
        categoria = Categoria(id, descricao)
        Categorias.Inserir(categoria)
        print(f"Categoria '{descricao}' cadastrada com sucesso.")

    @staticmethod
    def Categoria_Atualizar():
        id = input("Digite o ID da categoria que deseja atualizar: ")
        categoria = Categorias.Listar_Id(id)
        if categoria:
            descricao = input("Digite a nova descrição (ou pressione Enter para manter): ")
            Categorias.Atualizar(id, descricao=descricao)
            print(f"Categoria '{id}' atualizada com sucesso.")
        else:
            print("Categoria não encontrada.")

    @staticmethod
    def Categoria_Excluir():
        id = input("Digite o ID da categoria que deseja excluir: ")
        categoria = Categorias.Listar_Id(id)
        if categoria:
            Categorias.Excluir(id)
            print(f"Categoria '{id}' excluída com sucesso.")
        else:
            print("Categoria não encontrada.")

    # Métodos para Produtos
    @staticmethod
    def Produto_Listar():
        produtos = Produtos.Listar()
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(produto)

    @staticmethod
    def Produto_Inserir():
        id = input("Digite o ID do produto: ")
        descricao = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        Categorias.Listar()
        idCategoria = input("Digite o ID da categoria do produto: ")
        if not Categorias.Listar_Id(idCategoria):
            print("Categoria não encontrada.")
            return
        produto = Produto(id, descricao, preco, estoque, idCategoria)
        Produtos.Inserir(produto)
        print(f"Produto '{descricao}' cadastrado com sucesso.")

    @staticmethod
    def Produto_Atualizar():
        id = input("Digite o ID do produto que deseja atualizar: ")
        produto = Produtos.Listar_Id(id)
        if produto:
            descricao = input("Digite a nova descrição (ou pressione Enter para manter): ")
            preco = input("Digite o novo preço (ou pressione Enter para manter): ")
            estoque = input("Digite a nova quantidade em estoque (ou pressione Enter para manter): ")
            Categorias.Listar()
            idCategoria = input("Digite o novo ID da Categoria (ou pressione Enter para manter): ")
            if not Categorias.Listar_Id(idCategoria):
                print("Categoria não encontrada.")
                return
            Produtos.Atualizar(id, descricao=descricao, preco=preco, estoque=estoque, idCategoria=idCategoria)
            print(f"Produto '{id}' atualizado com sucesso.")
        else:
            print("Produto não encontrado.")

    @staticmethod
    def Produto_Excluir():
        id = input("Digite o ID do produto que deseja excluir: ")
        produto = Produtos.Listar_Id(id)
        if produto:
            Produtos.Excluir(id)
            print(f"Produto '{id}' excluído com sucesso.")
        else:
            print("Produto não encontrado.")


UI.main()