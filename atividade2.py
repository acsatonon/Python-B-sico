cnh = True
print('vou sair porque '+ ('estou habilitada' if [cnh] else 'vou de uber'))

habilitado = True
print('Eu '+ (' não posso dirigir pq não tenho habilitação', ' posso dirigir pq tenho habilitação')[habilitado])

numero1 = int(input('Digite um número: ' ))
numero2 = int(input ('Digite um número: ' ))
print(numero1 + numero2)

metros = float(input('Digite a metragem: ' ))
print (f('metro por milimetro fuca: {metros * 1000} mm'))

dias = int(input('Digite dias: ' ))
horas = int(input('Digite horas: ' ))
minutos = int(input('Digite minutos: ' ))
segundos = int(input('Digite segundos: ' ))
print(f'{(dias*86400)+ (horas*3600)+ (minutos*60)+ segundos} segundos' )

salario= float(input('Salario: '))
aumento= float(input('Porcentagem do aumento: '))
print(salario + (salario * aumento/100))

mercadoria= float(input('preço: '))
desconto= float(input('desconto: '))
valor_do_desconto = mercadoria * desconto/100
valor_total = mercadoria - valor_do_desconto
print(valor_total)
print(valor_do_desconto)

distancia = float(input('Digite a distancia: ' ))
velocidade = float(input('Digite a velocidade média: ' ))
print(distancia / velocidade)

c= float(input('temperatura(em Celsius): '))
print((9*c/5)+32)

distancia_percorrida = float(input('distancia percorrida em km: '))
dias = int(input('Digite dias: ' ))
print((distancia_percorrida*0.15)+ (dias*60))

cigarros_por_dia= int(input('Quanto cigarros por dia: '))
anos= int(input('anos fumados: '))
perdido= anos *365 *cigarros_por_dia * 10
reducao_dias= perdido/ (24*60)
print(reducao_dias)
