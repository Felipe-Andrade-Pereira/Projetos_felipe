dias = int(input('digite a quantidade de dias que o carro foi utilizado.'))
km = float(input('digite quantos quilomêtros o carro percorreu.'))
valor = (dias*60) + (km*0.15)
print('o valor total a ser cobrado do cliente é: R$ {:.2f}'.format(valor))
