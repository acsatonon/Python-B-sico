# adição
a= 3 + 3
print (a)

# subtração
b= 5 - 2
print(b)

# multiplicação
c= 4 * 2
print(c)

# divisão inteira
d= 5 // 2
print(d)

# divisão fracionada
e= 5/2
print(e)

# módulo da divisão (resto)
f= 10%3
print(f)

# potencia
g= 2**9
print(g)



# Operadores de atribução

a = 3 #atribuição
print(a)

a += 2 #aditiva (a=a+2)
print(a)

a-= 2 # subtrativa
print(a)

a *= 2 # multiplicativa
print(a)

a /= 2 # divisiva
print(a)

a %= 2 # modular
print(a)

a **= 2 # potenciação
print(a)



#operadores relacionais

print(3 > 4)     # maior que
print(3 >= 4)    #maior ou igual 
print(3 < 4)     #menor que
print(3 <= 4)    #menor ou igual
print(3 != 4)    #diferente
print(3 == 4)    #igual
print(3 == '4')  
print(3 == '3')



# operadores lógicos

#and
#não importa a quantidade de verdadeiros se tiver um falso, o resultado é falso

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True and True and True and True and False and True)


#or
#não importa a quantidade de falso se tiver um verdadeiro, o resultado é verdadeiro

print(True or True)
print(True or False)
print(False or True)
print(False or False or False or True or False)


#Xor ( ou exclusivo)
#no ou exclusivo apenas e somente apenas um ou o outro valor pode ser verdadeiro

print(True != True)     # falso
print(True != False)    # verdadeiro
print(False != True)    # verdadeiro
print(False != False)   # falso
print(False != False != False != True != False) # verdadeiro


#negação

print(not True)
print(not False)