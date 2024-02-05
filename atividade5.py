# x =1
# while x <= 100: 
#      print(x)
#      x +=1

# x =50
# while x <= 100: 
#      print(x)
#      x +=1

# x =10
# while x >= 0 : 
#      print(x)
#      x -=1
# print('Fogo')

# inicio = int(input('Digite o inicio da repetição:'))
# fim = int(input('Digite o fim da repetição:'))
# pulo = int(input('Digite o passo da repetição:'))
# while inicio <= fim:
#       if inicio % 2 == 0:
#          print(f'o número {inicio} é par')
#       else:
#          print(f'o número {inicio} é ímpar') 
#       inicio += pulo

# fim = int(input('Digite o fim da repetição:'))
# x= 1
# while x <= fim:
#   print(f'o número {x} é ímpar') 
#   x += 2

# fim = 30
# x =1
# while x <= fim: 
#      if x % 3 == 0:
#        print(x)
#      x +=1

# numero = int(input('Tabuada de: '))
# contador= 1
# print(f'***Tabuada de {numero}***')
# while contador <= 10:
#     print(f'{numero} * {contador} = {numero * contador}')
#     contador += 1

# numero = int(input('Tabuada de: '))
# inicio = int(input('Digite o inicio da tabuada:'))
# fim = int(input('Digite o fim da tabuada:'))
# print(f'***Tabuada de {numero}***')
# while inicio <= fim:
#     print(f'{numero} * {inicio} = {numero * inicio}')
#     inicio += 1

# primeiro= int(input('primeiro numero: '))
# segundo= int(input('segundo numero: '))
# x= 1
# r= 0
# while x <= segundo: 
#     r+= primeiro
#     x+= 1
#     print(f'{primerio} x {segundo} = {r}')

dividendo = int(input('dividendo: '))
divisor = int(input('divisor: '))
quociente = 0
while dividendo>= divisor:
    dividendo-= divisor
    quociente+=1
resto= dividendo
print(f'{dividendo} / {divisor} = {quociente} e {resto}')