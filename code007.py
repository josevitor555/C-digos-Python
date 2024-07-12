#questão 7
precoLitro_gasolina = float(input('Preço do litro da gasolina: '))
valorPagamento = float(input('Valor de pagamento: '))

if (precoLitro_gasolina and valorPagamento) > 0:
  totalLitros = valorPagamento / precoLitro_gasolina

  print(f'Total de litros: {round(totalLitros, 2)} L')
else:
  print('O preço do litro da gasolina e o valor do pagamento devem ser maior que zero')