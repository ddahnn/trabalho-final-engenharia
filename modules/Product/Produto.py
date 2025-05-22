from abc import ABC, abstractmethod

class Produto( ABC ):
    _Id = 0
    lista = []
    def __init__( self,estoque=0, nome="", codigo='' ):
        Produto._Id +=1
        self._id = Produto._Id
        self.nome = nome
        self.codigo = codigo
        self._preco = 0.0
        self.estoque = estoque

    def reporEstoque(self, quantidade):
        if not all([self.nome, self.codigo]) or self._preco <= 0:
            return "Necessário todos os dados para cadastro."
        if not any(prod["Nome"] == self.nome and prod["Código"] == self.codigo for prod in Produto.lista):
            return "Produto não cadastrado."
        for prod in Produto.lista:
            if prod["Nome"] == self.nome and prod["Código"] == self.codigo:
                prod["Estoque"] += quantidade
                return f"Estoque atualizado para {prod['Estoque']} unidades do produto {prod['Nome']}."
        return "Erro ao atualizar o estoque."
    

    @abstractmethod
    def cadastrar(self):
        pass

    def ver_estoque(self):
        for produto in Produto.lista:
            print(f"produto: {produto}\n")

    def get_preco(self):
        return f"R$ {self.preco:.2f}".replace(".",",")



    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0.0:
            self._preco = novo_preco
