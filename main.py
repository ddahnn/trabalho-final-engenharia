from modules.personas.Cliente  import  Cliente
from modules.personas.Funcionario  import Funcionario
from modules.Product.ProdutoPerecivel import ProdutoPerecivel
from modules.Product.ProdutoNaoPerecivel import ProdutoNaoPerecivel
from datetime import  date

print("\n" + "*"*20 +f" Cliente "+ "*"*20 + "\n")
c1 = Cliente("Daniel", "000.000.000-00", "dkasjofds")
print(c1.exibirDados())
c1.cadastrar()
print(c1.ver_lista())



print("\n" + "*"*20  + f" Funcionario " + "*"*20 + "\n")
f1 = Funcionario("Alguem", "0000.000.0.00", "234fsdfsf")
f1.cadastrar()
print(f1.exibirDados())
print(f1.ver_lista())


print("\n" + "*"*20  + f" Perecivel " + "*"*20 + "\n")
pp = ProdutoPerecivel(date(2025,6,25), 9, "Leite", "666")
pp2 = ProdutoPerecivel(date(2025, 8, 30), 1, "Café", "777")

#define preco
pp.preco = 5.9
pp2.preco = 30.9
# Cadastra
pp.cadastrar()
pp2.cadastrar()
#lista estoque
pp.ver_estoque()

# Repoem estoque
pp.reporEstoque(5)

#lista estoque
pp.ver_estoque()

print(pp.get_preco())





print("\n" + "*"*20  + f"Não Perecivel " + "*"*20 + "\n")
pnp1 = ProdutoNaoPerecivel(3, 10, "Cafeteira", "666")
pnp2 = ProdutoNaoPerecivel(12, 1, "Computador", "777")

pnp1.preco = 250.00 
pnp2.preco = 12000.00
pnp1.cadastrar()
pnp2.cadastrar()
print("\n***   Lista do estoque   ***")
pnp1.ver_estoque()
