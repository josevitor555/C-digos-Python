number1 = int(input('Digite um número: '))
number2 = int(input('Digite um segundo número: '))

if (number1 and number2) > 0:
  soma = number1 + number2
  divisao = number1 / number2
  multiplicacao = number1 * number2
  subtracao = number1 - number2
else:
  soma = 0
  divisao = 0
  multiplicacao = 0
  subtracao = 0
  print('Somente números inteiros!')

print(f'Soma entre {number1} e {number2}: {soma}')
print(f'Divisão entre {number1} e {number2}: {round(divisao, 2)}')
print(f'Multiplicação entre {number1} e {number2}: {multiplicacao}')
print(f'Subtração entre {number1} e {number2}: {subtracao}')