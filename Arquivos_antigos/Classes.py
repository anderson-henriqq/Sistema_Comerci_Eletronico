import datetime

class Cliente:
    
    def __init__(self, id, n, e, f):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__fone = f
        if not isinstance(id, int): raise ValueError("\nO ID não é um valor inteiro.")
        if (id <= 0): raise ValueError("\nID inválido, informe outro número.")
        if (n == ""): raise ValueError("\nO campo nome precisa ser preenchido")
        if (e == ""): raise ValueError("\nO campo e-mail precisa ser preenchido") 
        if (f == ""): raise ValueError("\nO campo Telefone precisa ser preenchido")
    
    def __str__(self):
        return f"ID nº {self._id}\n\tNome do cliente: {self._nome}\n\tE-mail: {self._email}\n\tTelefone: {self._fone}"

    def set_id(self, id):
        if not isinstance(id, int): raise ValueError("\nID inválido, informe outro número.")
        if (id <= 0): raise ValueError("ID inválido")
        self._id = id
    
    def set_nome(self, n):
        if (n == ""): raise ValueError("O campo nome precisa ser preenchido") 
        self._nome = n

    def set_email(self, e):
        if (e == ""): raise ValueError("O campo e-mail precisa ser preenchido")
        self._email = e
    
    def set_fone(self, f):
        if (f == ""): raise ValueError("O campo fone precisa ser preenchido")
        self._fone = f
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email
    
    def get_fone(self):
        return self._fone
    
class Venda:

    def __init__(self, id):
        self._id = id
        self._data = self._data
        self._carrinho = self._carrinho
        self._total = self._total
        self._idCliente = Cliente.get_id()
    
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_carrinho(self):
        return self.__carrinho

    def get_total(self):
        return self.__total

    def get_idCliente(self):
        return self.__idCliente
    
    def set_data(self, data):
        self.__data = data

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    def set_total(self, total):
        self.__total = total

    def set_idCliente(self, cliente):
        self.__idCliente = cliente.get_id()

    def __str__(self):
        return f"Venda [ID: {self.__id}, Data: {self.__data}, Total: {self.__total}, Cliente ID: {self.__idCliente}]"

class VendaItem:

    def __init__(self, id, q, p):
        self._id = id
        self._qtd = q
        self._preco = p
        self._idVenda = Venda.get_id()
        self._idProduto = Produto.get_id() 
    
    def get_id(self):
        return self.__id

    def get_qtd(self):
        return self.__qtd

    def get_preco(self):
        return self.__preco

    def get_idVenda(self):
        return self.__idVenda
    
    def set_qtd(self, qtd):
        self.__qtd = qtd

    def set_preco(self, preco):
        self.__preco = preco

    def set_idVenda(self, venda):
        self.__idVenda = venda.get_id()

    def __str__(self):
        return f"VendaItem [ID: {self.__id}, Qtd: {self.__qtd}, Preço: {self.__preco}, ID Venda: {self.__idVenda}]"

class Produto:
    
    def __init__(self, id, d, p, e):
        self._id = id
        self._descricao = d     
        self._preco = p
        self._estoque = e
        self._idCategoria = Categoria.get_id()
    
    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque

    def get_idCategoria(self):
        return self.__idCategoria

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco

    def set_estoque(self, estoque):
        self.__estoque = estoque

    def set_idCategoria(self, categoria):
        self.__idCategoria = categoria.get_id()

    def __str__(self):
        return f"Produto [ID: {self.__id}, Descrição: {self.__descricao}, Preço: {self.__preco}, Estoque: {self.__estoque}, Categoria ID: {self.__idCategoria}]"

class Categoria:

    def __init__(self, id, d):
        self._id = id
        self._descricao = d
    
    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"Categoria [ID: {self.__id}, Descrição: {self.__descricao}]" #teste

    


