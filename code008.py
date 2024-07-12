#questão 8
nomeFuncionario = str(input('Informe o nome do funcionário: '))
nHorasTrabalhadas = float(input('Informe o número de horas trabalhadas: '))

horasTrabalhada = 100

if (nomeFuncionario != ''):
  if (nHorasTrabalhadas <= 100) and (nHorasTrabalhadas > 0):
    salario = nHorasTrabalhadas * horasTrabalhada
    print(f'{nomeFuncionario}: {round(salario, 2)} R$!')
  else:
    print('o número de horas trabalhadas não pode ultrapassar 100 horas.')
else:
  print('Informe o nome do funcionário novamente!')