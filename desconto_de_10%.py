custo=float(input("valor final da compra em R$:"))
if custo >= 100.00:
    desconto=custo*0.10
    valor_final=custo-desconto
    print("seu custo é de:", valor_final)
else:
    print("você não ganhou desconto")
    print("o final da sua compra é de:",custo)