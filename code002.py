#questão 2
nome = str(input('Informe seu nome: '))
anoAtual = int(input('Informe o ano atual: '))
anoNascimento = int(input('Informe seu ano de nascimento: '))

if (anoAtual and anoNascimento) > 0:
  if (anoNascimento < anoAtual):
    idade = anoAtual - anoNascimento
    print(f'Sua idade: {idade}')
  else:
    print(f'Você veio do futuro foi {nome}?')
else:
  print('Informe uma data válida!')