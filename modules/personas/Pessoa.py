from abc import ABC, abstractmethod

class Pessoa ( ABC ):
    _listapessoa = []
    def __init__(self, nome, cpf, endereco) :
        self.nome = nome
        self._cpf = cpf
        self.endereco = endereco

    def exibirDados(self):
        return f"""
    Nome : {self.nome},\n
    CPF: {self._cpf},\n
    Endereço: {self.endereco},\n
    """

    @abstractmethod
    def cadastrar(self):
        pass