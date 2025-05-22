from modules.Product.Produto import Produto

class ProdutoNaoPerecivel(Produto):
    def __init__(self, garantia, estoque, nome, codigo):
        super().__init__(estoque, nome, codigo)
        self._garantia = garantia


    def cadastrar(self):
        if not all([self.nome, self.codigo]) or self._preco <= 0.0 or self.estoque <= 0 or self._garantia <= 0:
            print( f"Necessario todos os dados para cadastro" )
            return
        Produto._Id += 1
        produto = {
            "Id": Produto._Id,
            "Nome": self.nome,
            "Código": self.codigo,
            "Preço": f"{self._preco:.2f}".replace('.', ','),
            "Estoque": self.estoque,
            "Garantia": f"{self._garantia} meses"
        }
        Produto.lista.append(produto)
        print(f"O produto {produto['Nome']}, foi adicionado com sucesso.")

    def ver_estoque(self):
        return super().ver_estoque()
    

    @property
    def garantia(self):
        return f"{self._garantia} Meses"
    
    def get_preco(self):
        return super().get_preco()
