import datetime

class Cliente:
    def __init__(self, id, nome, email, fone):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe outro número.")
        if not nome:
            raise ValueError("\nO campo nome precisa ser preenchido")
        if not email:
            raise ValueError("\nO campo e-mail precisa ser preenchido")
        if not fone:
            raise ValueError("\nO campo telefone precisa ser preenchido")

        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    
    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, E-mail: {self.__email}, Telefone: {self.__fone}"

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe outro número.")
        self.__id = id

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        if not nome:
            raise ValueError("\nO campo nome precisa ser preenchido") 
        self.__nome = nome

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        if not email:
            raise ValueError("\nO campo e-mail precisa ser preenchido")
        self.__email = email
    
    def get_fone(self):
        return self.__fone
    
    def set_fone(self, fone):
        if not fone:
            raise ValueError("\nO campo telefone precisa ser preenchido")
        self.__fone = fone


class Categoria:
    def __init__(self, id, descricao):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe outro número.")
        if not descricao:
            raise ValueError("\nO campo descrição precisa ser preenchido.")
        
        self.__id = id
        self.__descricao = descricao
    
    def __str__(self):
        return f"Categoria [ID: {self.__id}, Descrição: {self.__descricao}]"
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe outro número.")
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        if not descricao:
            raise ValueError("\nO campo descrição precisa ser preenchido")
        self.__descricao = descricao


class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe outro número.")
        if not descricao:
            raise ValueError("\nO campo descrição precisa ser preenchido")
        if not isinstance(preco, float) or preco <= 0.0:
            raise ValueError("\nO campo preço precisa ser um valor positivo")
        if not isinstance(estoque, int) or estoque < 0:
            raise ValueError("\nO campo estoque precisa ser um número inteiro positivo")
        '''if not isinstance(idCategoria, int) or idCategoria <= 0:
            raise ValueError("\nID da Categoria inválido, informe outro número.")''' # Verificação já feita na inicialização da Categoria
        
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idCategoria = idCategoria
    
    def __str__(self):
        return f"Produto [ID: {self.__id}, Descrição: {self.__descricao}, Preço: R$ {self.__preco:.2f}, Estoque: {self.__estoque}, Categoria ID: {self.__idCategoria}]"
    
    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        if not descricao:
            raise ValueError("O campo descrição precisa ser preenchido")
        self.__descricao = descricao

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if not isinstance(preco, float) or preco <= 0.0:
            raise ValueError("O campo preço precisa ser um número positivo")
        self.__preco = preco

    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, estoque):
        if not isinstance(estoque, int) or estoque < 0:
            raise ValueError("O campo estoque precisa ser um número inteiro positivo")
        self.__estoque = estoque

    def get_idCategoria(self):
        return self.__idCategoria

    def set_idCategoria(self, idCategoria):
        '''if not isinstance(idCategoria, int) or idCategoria <= 0:
            raise ValueError("ID da Categoria inválido, informe outro número.")'''
        self.__idCategoria = idCategoria


class Venda:
    def __init__(self, id, idCliente, carrinho=True):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe outro número.")
        '''if not isinstance(idCliente, int) or idCliente <= 0:
            raise ValueError("\nID do Cliente inválido, informe outro número.")''' # Verificação já feita na inicialização do Cliente

        self.__id = id
        self.__data = datetime.datetime.now()
        self.__carrinho = carrinho
        self.__total = 0.0
        self.__idCliente = idCliente
        #self.__itens = []

    def __str__(self):
        return f"Venda [ID: {self.__id}, Data: {self.__data}, Total: R$ {self.__total:.2f}, Cliente ID: {self.__idCliente}]"
    
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_carrinho(self):
        return self.__carrinho

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    '''def get_total(self):
        return self.__total

    def calcular_total(self):
        self.__total = sum(item.get_preco() * item.get_qtd() for item in self.__itens)'''

    def get_idCliente(self):
        return self.__idCliente

    '''def get_itens(self):
        return self.__itens

    def adicionar_item(self, item):
        self.__itens.append(item)
        self.calcular_total()'''


class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe outro número.")
        if not isinstance(qtd, int) or qtd <= 0:
            raise ValueError("\nQuantidade inválida, informe outro número.")
        if not isinstance(preco, float) or preco <= 0.0:
            raise ValueError("\nO campo preço precisa ser um número positivo")
        '''if not isinstance(idVenda, int) or idVenda <= 0:
            raise ValueError("\nID da Venda inválido, informe outro número.")
        if not isinstance(idProduto, int) or idProduto <= 0:
            raise ValueError("\nID do Produto inválido, informe outro número.")''' # Verificação já feita na inicialização do Produto e Venda

        self.__id = id
        self.__qtd = qtd
        self.__preco = (preco*qtd)
        self.__idVenda = idVenda
        self.__idProduto = idProduto

    def __str__(self):
        return f"Venda do item [ID: {self.__id}, Qtd. vendida: {self.__qtd}, Preço da venda: R$ {self.__preco:.2f}, ID Boleto: {self.__idVenda}, ID Produto: {self.__idProduto}]"
    
    def get_id(self):
        return self.__id

    def get_qtd(self):
        return self.__qtd

    def set_qtd(self, qtd):
        if not isinstance(qtd, int) or qtd <= 0:
            raise ValueError("Quantidade inválida, informe outro número.")
        self.__qtd = qtd

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if not isinstance(preco, float) or preco <= 0.0:
            raise ValueError("O campo preço precisa ser um número positivo")
        self.__preco = preco*self.__qtd

    def get_idVenda(self):
        return self.__idVenda

    def set_idVenda(self, idVenda):
        '''if not isinstance(idVenda, int) or idVenda <= 0:
            raise ValueError("ID da Venda inválido, informe outro número.")'''
        self.__idVenda = idVenda

    def get_idProduto(self):
        return self.__idProduto

    def set_idProduto(self, idProduto):
        '''if not isinstance(idProduto, int) or idProduto <= 0:
            raise ValueError("ID do Produto inválido, informe outro número.")'''
        self.__idProduto = idProduto