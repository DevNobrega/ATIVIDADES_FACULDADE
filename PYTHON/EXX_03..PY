nota = op = media = a = cont = 0
while True:
    nota = float(input('Informe sua nota:'))
    a += nota 
    op = str(input('Deseja continuar?').upper().strip())
    cont += 1 
    if op == 'N':
        break
media = a / cont
print(f'Sua média foi {media}')
