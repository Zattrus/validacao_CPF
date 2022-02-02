# Gerando CPFs validos
from random import randint

while True:
  numero = str(randint(100000000, 999999999))

  novo_cpf = numero              # Elimina os dois últimos dígitos do CPF
  reverso = 10                      # Contador reverso                     
  total = 0
  # Loop do CPF
  for index in range(19):
      if index > 8:              # Primeiro índice de 0 a 9              
        index -= 9               # São os 9 primeiros dígitos do CPF

      total += int(novo_cpf[index]) * reverso     # Valor total da multiplicação

      reverso -= 1                  # Decrementa o contador reverso 
      if reverso < 2:
          reverso = 11
          d = 11 - (total % 11)  
        
          if d > 9:                 # caso o digito for > que 9 o valor é 0
              d = 0
          total = 0                 # zera o total
          novo_cpf += str(d)        # concatena o digito calculado ao CPF

  print(novo_cpf)

  if input('Deseja gerar outro CPF? [S/N] ').upper() == 'N':
    break