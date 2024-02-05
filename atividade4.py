# a = float(input('Digite o primeiro valor: '))
# b = float(input('Digite o segundo valor: '))
# c = float(input('Digite o terceiro valor: '))

# if a > b and a > c:
#      print(f'{a} é o maior número!')
# if b > a and b > c:
#      print(f'{b} é o maior número!')
# if c > b and c > a:
#      print(f'{c} é o maior número!')
# if a < b and a < c:
#      print(f'{a} é o menor número!')
# if b < a and b < c:
#      print(f'{b} é o menor número!')
# if c < b and c < a:
#      print(f'{c} é o menor número!')
# print('fim do programa')

# salario = float(input('Salário: '))
# if salario > 1250:
#      aumento = salario + salario * 0.10
#      print(f'Seu salário aumentou para R${aumento: 7.2f}')
# if salario <= 1250:
#      aumento = salario + salario * 0.15 
#      print(f'Seu salário aumentou para R${aumento: 7.2f}')

# idade= int(input('digite a idade do seu carro: '))
# if idade <= 3 :
#      print('seu carro é novo')
# else:
#      print('seu carro é velho')

# distancia = float(input('Qual a distância?(km)'))                  
# if distancia <= 200:
#      print(f'R${distancia* 0.50: .2f}')
# else:
#      print(f'R${distancia* 0.45: .2f}')

# distancia = float(input('Qual a distância?(km)'))  
# bandeira = int(input('Qual a bandeira?'))            
# if distancia <= 200:
#      valor= distancia* 2
# if distancia > 200:
#      valor= distancia* 1.75

# if bandeira== 1 :
#      valor_final= valor *1
# if bandeira== 2 :
#      valor_final= valor *2
# if bandeira!= 1 and bandeira!= 2:
#      print('Essa bandeira não existe')
# print(f'total da sua corrida foi de {valor_final: .2f}')

# dias_da_semana = int(input('Qual o dia:'))
# if dias_da_semana == 1:
#      dia= 'Domingo'
# elif dias_da_semana == 2:
#      dia= 'Segunda'   
# elif dias_da_semana == 3:
#      dia= 'Terça'   
# elif dias_da_semana == 4:
#      dia= 'Quarta'
# elif dias_da_semana == 5:
#      dia= 'Quinta'
# elif dias_da_semana == 6:
#      dia= 'Sexta'
# elif dias_da_semana == 7:
#      dia= 'Sábado'      
# else:
#      print('Dia inválido (1 até 7)') 
# print(f'o dia da semana é {dia}')

# a = float(input('Digite o primeiro valor: '))
# b = float(input('Digite o segundo valor: '))
# c = input('Qual operação deseja?(*,/,+,-)')
# if c == '*':
#      print(a*b)
# if c== '/':
#      print(a/b)
# if c== '+':
#      print(a+b)
# if c== '-':
#      print(a-b)

# casa = float(input('valor da casa: '))
# salario = float(input('Salário: '))
# anos = int(input('quantos anos: '))
# prestacao= casa/(anos*12)
# aprovacao= salario*0.3
# if prestacao< aprovacao:
#      print(f'Aprovado')
# else:
#      print(f'nao aprovado')

voltagem = float(input('quantidade de kWh: '))
tipo = input('tipo de estalação(R,I,C): ')
if tipo == 'R':
     if voltagem <= 500:
         print(f'valor a pagar {voltagem* 0.4}')
     else:
        print(f'valor a pagar{voltagem* 0.65}')   
if tipo== 'I':
     if voltagem <= 1000:
         print(f'valor a pagar{voltagem* 0.55}')
     else:
        print(f'valor a pagar{voltagem* 0.6}') 
if tipo== 'C':
     if voltagem <= 5000:
         print(f'valor a pagar{voltagem* 0.55}')
     else:
        print(f'valor a pagar{voltagem* 0.6}') 
if tipo!= 'R' and tipo!= 'I' and tipo!= 'C':
     print('tipo não encontrado')