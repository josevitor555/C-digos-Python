#questão 6
quant_pFrances = int(input('Quantidades de pões francês: '))
quant_pBroas = int(input('Quantidades de pões broas: '))

preco_pFrances = 0.72
preco_pBroas = 1.50

if (quant_pFrances and quant_pBroas) > 0:
  valor_pFrances = quant_pFrances * preco_pFrances
  valor_pBroas = quant_pBroas * preco_pBroas

  valorArrecadados = valor_pFrances + valor_pBroas

  print(f'Total arrecadados em R$: {valorArrecadados}')
else:
  print('Informe os números acima de zero!')