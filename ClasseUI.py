from Classes_20240814 import Cliente, Categoria, Produto
from ClassesEstaticas_20240814 import Clientes, Categorias, Produtos

class UI:
    @staticmethod
    def main():
        while True:
            UI.menu()

            operation = input("Escolha uma opção: ")

            if operation == '1':    # Listar Clientes
                UI.Cliente_Listar()
            
            elif operation == '2':  # Inserir Cliente
                UI.Cliente_Inserir()

            elif operation == '3':  # Atualizar Cliente
                UI.Cliente_Atualizar()

            elif operation == '4':  # Excluir Cliente
                UI.Cliente_Excluir()

            elif operation == '5':  # Listar Categorias
                UI.Categoria_Listar()

            elif operation == '6':  # Inserir Categoria
                UI.Categoria_Inserir()

            elif operation == '7':  # Atualizar Categoria
                UI.Categoria_Atualizar()

            elif operation == '8':  # Excluir Categoria
                UI.Categoria_Excluir()

            elif operation == '9':  # Listar Produtos
                UI.Produto_Listar()

            elif operation == '10':  # Inserir Produto
                UI.Produto_Inserir()

            elif operation == '11':  # Atualizar Produto
                UI.Produto_Atualizar()

            elif operation == '12':  # Excluir Produto
                UI.Produto_Excluir()

            elif operation == '0':  # Finalizar
                print("Finalizando o programa.")
                break
            
            else:
                print("Opção inválida.")

    @staticmethod
    def menu():
        print("\n:::::::::::::::::::::::::::::::::::::::")
        print("1 - Listar Clientes")
        print("2 - Inserir Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Listar Categorias")
        print("6 - Inserir Categoria")
        print("7 - Atualizar Categoria")
        print("8 - Excluir Categoria")
        print("9 - Listar Produtos")
        print("10 - Inserir Produto")
        print("11 - Atualizar Produto")
        print("12 - Excluir Produto")
        print("0 - Finalizar")

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
        idCategoria = input("Digite o ID da categoria do produto: ")
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
            idCategoria = input("Digite o novo ID da categoria (ou pressione Enter para manter): ")
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