num=(int(input('Digite um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite mais um numero: ')),
     int(input('Digite o ultimo numero: ')))
print('-='*25)
print(f'{num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)+1}° posição')
else:
    print('O numero 3 não apareceu')

print(f'Os numeros pares digitados foram', end=' ')
for n in num:
    if n % 2==0:
        print(n,end=' ')
        



    