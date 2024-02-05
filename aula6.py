# Estrutura de repetição

#while <condição>:   --> enquanto
#    bloco a ser executado

# x =1
# while x <= 5: 
#      print('A')
#      print(1)
#      x +=1

# fim = int(input('Digite o fim da repetição:'))
# x= 1
# while x <= fim:
#       print (x)
#       x = x + 1

# fim = int(input('Digite o fim da repetição:'))
# x= 0
# while x <= fim:
#       if x % 2 == 0:
#          print(f'o número {x} é par')
#       else:
#          print(f'o número {x} é ímpar') 
#       x += 1
         
numero = int(input('Tabuada de: '))
contador= 1
print(f'***Tabuada de {numero}***')
while contador <= 10:
    print(numero + contador)
    contador += 1
