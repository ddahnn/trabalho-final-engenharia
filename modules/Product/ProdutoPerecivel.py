from datetime import date
from modules.Product.Produto import Produto

class ProdutoPerecivel(Produto):
    def __init__(self, validade:date, estoque, nome, codigo):
        super().__init__(estoque, nome, codigo)
        self._validade = validade

    def cadastrar(self):
        if not all([self.nome, self.codigo, self._preco> 0.0, self.estoque> 0]):
            print( f"Necessario todos os dados para cadastro" )
            return
        Produto._Id +=1
        produto = {
            "Id": Produto._Id,
            "Nome": self.nome,
            "Código": self.codigo,
            "Preço": f"{self._preco:.2f}".replace('.', ','),
            "Estoque": self.estoque,
            "Validade": self._validade.strftime("%d/%m/%Y")
        }
        Produto.lista.append(produto)
        print(f"O produto{produto['Nome']}, foi adicionado com sucesso.")

    def ver_estoque(self):
        return super().ver_estoque()
