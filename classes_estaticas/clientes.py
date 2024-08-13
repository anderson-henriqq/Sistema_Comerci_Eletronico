from Classes import *


class Clientes:
    def __init__(self):
        self.__objetos = {}
    def setObjetos(self, objetos):
        self.__objetos = objetos 
    def getObjetos(self):
        return self.__objetos 

    def Inserir(self, objeto):
        self.__objetos.append(objeto)
    def Listar(self):
        for objeto in self.__objetos:
            print(self.__objetos[objeto])
    def Listar_Id(self):
        ids = list(self.__objetos.keys())
        for ids in self.__objetos:
            print(ids)
    def Atualizar(self):
        op = 10
        while op != 9:
            locID = input("Digite o ID do objeto: \n")  
            InfoObjeto = input("Digite qual opção deseja alterar: \n 1 - ID\n 2 - Nome\n 3 - Email\n 4 - Fone\n 9 - Sair\n")
            match InfoObjeto:
                case 1: NovoId = self.__objetos[locID].set_id(NovoId) 
                case 2: NovoNome = self.__objetos[locID].set_nome(NovoNome)
                case 3: NovoEmail = self.__objetos[locID].set_email(NovoEmail)
                case 4: NovoFone = self.__objetos[locID].set_fone(NovoFone) 
        #desenvolver acesso a key do dicionario;
        #desenvolver escolha da informação do objeto;


        



             