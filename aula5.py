#condicional

salario = float(input('Digite o salario para calculo do imposto: '))
base = salario
imposto = 0
if base > 3000:
     imposto =  (base - 3000)* 0.35
     base = 3000
     print(imposto)
if base > 1000 :
     imposto += ((base - 1000) * 0.20)
     print(imposto)
print(f'Salário: R${salario: 6.2f} Imposto a pagar: R${imposto: 6.2f}')

# Estruturas aninhadas

minutos= int(input('Quantos minutos vc utilizou esse mês: '))
if minutos < 200:
    preço = 0.20 
else:
     if minutos < 400:
          preço= 0.18
     else:
          preço= 0.15
print(f'Você vai pagar este mês: R${minutos * preço: 0.2f}')

categoria = int(input('categoria do produto'))
if categoria == 1:
     preco= 10
elif categoria == 2:
     preco= 18   
elif categoria == 3:
     preco= 23   
elif categoria == 4:
     preco= 26
elif categoria == 5:
     preco= 31      
else:
     print('categoria invalida') 
print(f'o preço do produto é R${preco: .2f}')