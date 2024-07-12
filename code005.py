#questão 5
name = str(input('Informe seu nome: '))
idade = int(input('Informe sua idade: '))
anoAtual = int(input('Informe o ano atual: '))
anoNascimento = int(input('Informe o ano nascimento: '))

if (name != ''):
  if (len(name) == 3):
    if (anoAtual > 0):
      daysLived = idade * 365
      print(f'Você viveu: {daysLived}')
    else:
      print('Informe um ano válido!')
  else:
    print('Informe um nome menor que 3 letras!')
else:
  print('Inform um nome!')