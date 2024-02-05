velocidade = float(input('Qual a velocidade?(km/h) '))
if velocidade <= 80 :
     print('Tudo certo!')
if velocidade > 80 :
     multa = velocidade * 5
     print(f'Você foi multado em {multa} reais')  

print('boa viagem')   