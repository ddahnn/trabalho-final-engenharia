from modules.personas.Pessoa import Pessoa

class Funcionario( Pessoa ) :

    __idFunc = 0
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf, endereco)
        Funcionario.__idFunc += 1
        self.__id = Funcionario.__idFunc 

    def cadastrar(self):
        if not all([self.nome, self._cpf, self.endereco]):
            print('Necessario todos os dados Para efetuar o cadastro.')
        elif any(func["CPF"] ==self._cpf for func in Pessoa._listapessoa):
            print(f"O cliente já esta cadastrado")
        else:
            pessoa={
                "ID Funcionario" : self.__id,
                "Nome": self.nome,
                "CPF": self._cpf,
                "Endereço": self.endereco
            }
            Pessoa._listapessoa.append(pessoa)
            print(f"O Funcionario  {pessoa['Nome']}, foi adicionado.")

    @classmethod
    def  ver_lista( self ):
       for funcionario in Pessoa._listapessoa:
           return f"""
        ***   Lista de Funcionarios   ***
        \n{funcionario}
 """
    
    def exibirDados(self):
        info= super().exibirDados()
        return info + f"ID Funcionario: {self.__id}"

