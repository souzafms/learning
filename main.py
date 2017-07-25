
hora = 00
minuto = 00

hora = input("Insira uma hora inteira:")
while hora.isdigit() == False:
    print('Você inseriu uma hora inválida')
    hora = input("Insira a hora:")

minuto = input("Insita o minuto:")
while minuto.isdigit() == False:
    print('Você inseriu um minuto inválido.')
    minuto = input("Insita o minuto:")

hora = int(hora)
minuto = int(minuto)
if int(minuto) < 60:
    print("Horário: %d:%d" %(hora,minuto))
else:
    hora = (hora + int(minuto / 60))
    minuto = minuto % 60
    print("Horário: %d:%d" % (hora, minuto))