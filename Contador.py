import time
T = input('Qual o tempo?')
contador= int(T)
while contador > 0:
    print(f'{contador}')
    contador -= 1
    time.sleep(1)
else:
 print(f'Kabooomm')






