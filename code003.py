#questão 3
name = str(input('Informe seu nome: '))

kilometragem = float(input('Informe a kilometragem do seu carro: '))
tempo = int(input('Informe o valor do tempo: '))

if (kilometragem and tempo) > 0:
  vm = kilometragem / tempo
  print(f'Sua velocidade média: {round(vm, 2)} km/h!')
else:
  print('Informe valores acima de zero e positivos!')