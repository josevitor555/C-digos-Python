#questão 4
peso_prato = float(input('Informe o peso do prato: '))
valor_prato = 12

if (peso_prato > 0):
  valorTotal = peso_prato * valor_prato
  print(f'Valor do peso do prato R$: {round(valorTotal, 2)}')
elif (peso_prato < 0):
  print('O peso do prato não pode ser negativo!')