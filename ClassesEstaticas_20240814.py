import json
from datetime import datetime
from Classes_20240814 import Cliente, Venda, VendaItem, Produto, Categoria

class Clientes:
    __clientes = []

    @staticmethod
    def Inserir(cliente):
        Clientes.__clientes.append(cliente)

    @staticmethod
    def Listar():
        return Clientes.__clientes

    @staticmethod
    def Listar_Id(id):
        for cliente in Clientes.__clientes:
            if cliente.get_id() == id:
                return cliente
        return None

    @staticmethod
    def Atualizar(id, **kwargs):
        cliente = Clientes.Listar_Id(id)
        if cliente:
            if "nome" in kwargs:
                cliente.set_nome(kwargs["nome"])
            if "email" in kwargs:
                cliente.set_email(kwargs["email"])
            if "fone" in kwargs:
                cliente.set_fone(kwargs["fone"])

    @staticmethod
    def Excluir(id):
        cliente = Clientes.Listar_Id(id)
        if cliente:
            Clientes.__clientes.remove(cliente)

    @staticmethod
    def Abrir(filepath):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data:
                    cliente = Cliente(item["id"], item["nome"], item["email"], item["fone"])
                    Clientes.Inserir(cliente)
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    @staticmethod
    def Salvar(filepath):
        with open(filepath, "w") as file:
            data = [{"id": c.get_id(), "nome": c.get_nome(), "email": c.get_email(), "fone": c.get_fone()} for c in Clientes.__clientes]
            json.dump(data, file)

class Vendas:
    __vendas = []

    @staticmethod
    def Inserir(venda):
        Vendas.__vendas.append(venda)

    @staticmethod
    def Listar():
        return Vendas.__vendas

    @staticmethod
    def Listar_Id(id):
        for venda in Vendas.__vendas:
            if venda.get_id() == id:
                return venda
        return None

    @staticmethod
    def Atualizar(id, **kwargs):
        venda = Vendas.Listar_Id(id)
        if venda:
            if "data" in kwargs:
                venda.set_data(kwargs["data"])
            if "carrinho" in kwargs:
                venda.set_carrinho(kwargs["carrinho"])
            if "total" in kwargs:
                venda.set_total(kwargs["total"])
            if "idCliente" in kwargs:
                venda.set_idCliente(kwargs["idCliente"])

    @staticmethod
    def Excluir(id):
        venda = Vendas.Listar_Id(id)
        if venda:
            Vendas.__vendas.remove(venda)

    @staticmethod
    def Abrir(filepath):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data:
                    venda = Venda(item["id"], datetime.strptime(item["data"], '%Y-%m-%d %H:%M:%S'), item["carrinho"], item["total"], item["idCliente"])
                    Vendas.Inserir(venda)
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    @staticmethod
    def Salvar(filepath):
        with open(filepath, "w") as file:
            data = [{"id": v.get_id(), "data": v.get_data().strftime('%Y-%m-%d %H:%M:%S'), "carrinho": v.get_carrinho(), "total": v.get_total(), "idCliente": v.get_idCliente()} for v in Vendas.__vendas]
            json.dump(data, file)

class VendaItens:
    __venda_itens = []

    @staticmethod
    def Inserir(venda_item):
        VendaItens.__venda_itens.append(venda_item)

    @staticmethod
    def Listar():
        return VendaItens.__venda_itens

    @staticmethod
    def Listar_Id(id):
        for item in VendaItens.__venda_itens:
            if item.get_id() == id:
                return item
        return None

    @staticmethod
    def Atualizar(id, **kwargs):
        item = VendaItens.Listar_Id(id)
        if item:
            if "qtd" in kwargs:
                item.set_qtd(kwargs["qtd"])
            if "preco" in kwargs:
                item.set_preco(kwargs["preco"])
            if "idVenda" in kwargs:
                item.set_idVenda(kwargs["idVenda"])
            if "idProduto" in kwargs:
                item.set_idProduto(kwargs["idProduto"])

    @staticmethod
    def Excluir(id):
        item = VendaItens.Listar_Id(id)
        if item:
            VendaItens.__venda_itens.remove(item)

    @staticmethod
    def Abrir(filepath):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data:
                    venda_item = VendaItem(item["id"], item["qtd"], item["preco"], item["idVenda"], item["idProduto"])
                    VendaItens.Inserir(venda_item)
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    @staticmethod
    def Salvar(filepath):
        with open(filepath, "w") as file:
            data = [{"id": vi.get_id(), "qtd": vi.get_qtd(), "preco": vi.get_preco(), "idVenda": vi.get_idVenda(), "idProduto": vi.get_idProduto()} for vi in VendaItens.__venda_itens]
            json.dump(data, file)

class Produtos:
    __produtos = []

    @staticmethod
    def Inserir(produto):
        Produtos.__produtos.append(produto)

    @staticmethod
    def Listar():
        return Produtos.__produtos

    @staticmethod
    def Listar_Id(id):
        for produto in Produtos.__produtos:
            if produto.get_id() == id:
                return produto
        return None

    @staticmethod
    def Atualizar(id, **kwargs):
        produto = Produtos.Listar_Id(id)
        if produto:
            if "descricao" in kwargs:
                produto.set_descricao(kwargs["descricao"])
            if "preco" in kwargs:
                produto.set_preco(kwargs["preco"])
            if "estoque" in kwargs:
                produto.set_estoque(kwargs["estoque"])
            if "idCategoria" in kwargs:
                produto.set_idCategoria(kwargs["idCategoria"])

    @staticmethod
    def Excluir(id):
        produto = Produtos.Listar_Id(id)
        if produto:
            Produtos.__produtos.remove(produto)

    @staticmethod
    def Abrir(filepath):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data:
                    produto = Produto(item["id"], item["descricao"], item["preco"], item["estoque"], item["idCategoria"])
                    Produtos.Inserir(produto)
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    @staticmethod
    def Salvar(filepath):
        with open(filepath, "w") as file:
            data = [{"id": p.get_id(), "descricao": p.get_descricao(), "preco": p.get_preco(), "estoque": p.get_estoque(), "idCategoria": p.get_idCategoria()} for p in Produtos.__produtos]
            json.dump(data, file)

class Categorias:
    __categorias = []

    @staticmethod
    def Inserir(categoria):
        Categorias.__categorias.append(categoria)

    @staticmethod
    def Listar():
        return Categorias.__categorias

    @staticmethod
    def Listar_Id(id):
        for categoria in Categorias.__categorias:
            if categoria.get_id() == id:
                return categoria
        return None

    @staticmethod
    def Atualizar(id, **kwargs):
        categoria = Categorias.Listar_Id(id)
        if categoria:
            if "descricao" in kwargs:
                categoria.set_descricao(kwargs["descricao"])

    @staticmethod
    def Excluir(id):
        categoria = Categorias.Listar_Id(id)
        if categoria:
            Categorias.__categorias.remove(categoria)

    @staticmethod
    def Abrir(filepath):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data:
                    categoria = Categoria(item["id"], item["descricao"])
                    Categorias.Inserir(categoria)
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    @staticmethod
    def Salvar(filepath):
        with open(filepath, "w") as file:
            data = [{"id": c.get_id(), "descricao": c.get_descricao()} for c in Categorias.__categorias]
            json.dump(data, file)