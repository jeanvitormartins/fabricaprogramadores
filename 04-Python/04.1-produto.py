# Criando as variaveis e soliictando os valores ao usuario.
nome_produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto:' ))
desconto = float(input('Digite o percentual de desconto: '))

# Calculando o desconto e o preço final.
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

# Apresentando o preço final ao usuário.
print(f'Produto: {nome_produto} - Preço Final: R$ {preco_final}')
