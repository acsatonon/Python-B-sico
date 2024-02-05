# nome = input('Qual o seu nome? ')
# idade= int(input('Qual o sua idade? '))
# print(f'Seu nome é {nome}, você tem {idade} anos de idade')

# numero1 = float(input('Digite o primeiro número? '))
# numero2 = float(input('Digite o segundo número? '))
# soma= numero1 + numero2
# print(f'O resultado é: {soma}')

# soma=0
# contador= 0
# while contador <4:
#     numero = int(input('Digite um número: '))
#     soma+= numero
#     contador += 1
# media = soma/ contador
# print(f'A média é de: {media}')

contador= 0
maior= 0
menor=0
while contador <5:
      numero=   float(input('Digite um número: '))
      if contador == 1:
         maior = numero
         menor= numero
      elif numero < menor:
         menor= numero
      elif numero > maior:
         maior= numero
      contador += 1
print(f'o maior número é {maior}')
print(f'o menor número é {menor}')