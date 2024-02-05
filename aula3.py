esta_chovendo = True

print('Hoje estou com as roupas ' + ('secas', 'molhadas')[esta_chovendo]) 
# nesse caso o mais perto da variavel e verdadeiro

print('Hoje estou com as roupas ' + ('molhadas.'if esta_chovendo else 'secas'))

#_building_

# Operador membro
lista = [1,2,3,'Acsa', 'tonon']

print(1 in lista)
print(2 in lista)
print(3 in lista)
print(4 in lista)
print(4 not in lista)
print('a' in lista)
print('b' in lista)
print('Acsa' in lista)

#operador identidade

x = 5
y = x
z = 5

print(x is z)
print(y is not 5)
#valor literal


#salva um valor na memória, sao diferentes
lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]

print(lista_a is lista_b)
print(lista_a is lista_c)

# CONVERSÃO

print(3+3)
print(int('3')+int('3'))

print(2 + int('2'))


print(float('5')+float('8'))
print(2 + float('75'))

#print(type(3))


#Strings

tipo_de_pao = 'assado'
string = f'joao e maria comem pao {tipo_de_pao}'
print(string)
print(len(string))

string_vazia = ''
print(len(string_vazia))

a= 'abcde'
print(a[0])
print(a[4])

b= 'ABC' + 'DE'
print(b)
c = "-x-" * 9
d = "-x-" * 9
e = "-x-" * 9
print(c)
print(d)
print(e)

b= 'ac' + '58'
print(b)

m= d + '4$ = ' + e *4
print(m)


# posição

i = 'acbcdefghi'
print(i[5:7])
print(i[0:2])
print(i[4:8])
print(i[:5])
print(i[::-1])
print(i[6:4:-1])

x = input ('Digite um texto: ' )
print(f'o texto digitado foi: {x}')

numero = int(input('digite um numero: '))
print(type(numero))

reais = float(input('digite um valor em reais: '))
print(f'vc tem apenas R$ {reais: .2f}')