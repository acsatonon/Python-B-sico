# tipo de string

nome= 'ACSA'
print(nome.lower())

nome2= 'al c a n t ara Tonon'
nome2 = nome2.split(' ')
print(nome2)

# frase= 'A vida é bela'
# print(frase.index(5))

#print(dir(str))


# Condicinal

a= int(input('primeiro valor: '))
b= int(input('Segundo valor: '))

if a > b:
     print(f'{a} é maior que {b}')
if b > a:
     print(f'{b} é maior que {a}')
if a == b:
     print(f'{a} é igual a {b}')

print('fim do programa')

idade= int(input('digite a idade do seu carro: '))
if idade <= 3 :
     print('seu carro é novo')
if idade > 3 :
     print('seu carro é velho')



