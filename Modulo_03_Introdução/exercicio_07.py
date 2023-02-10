"""
Calculadora com While.
"""

while True:
    number_1 = input("Digite um número: ")
    number_2 = input("Digite outro número: ")
    operador = input("Digite o operador [+, -, *, /]: ")

    fnumber_1 = 0.0
    fnumber_2 = 0.0
    try:
        fnumber_1 = float(number_1)
        fnumber_2 = float(number_2)
        num_vali  = True
    except:
        print(">> Um ou mais números digitados são invalidos.\n")
        continue

    operador_validos = '+-*/'
    if operador not in operador_validos:
        print(">> Operador invalido.\n")
        continue
    if len(operador) > 1:
        print(">> Digite um operador.\n")
        continue
    
    print(f"{fnumber_1} {operador} {fnumber_2} =")
    if operador == '+':
        print(fnumber_1 + fnumber_2)
    elif operador == '-':
        print(fnumber_1 - fnumber_2)
    elif operador == '*':
        print(fnumber_1 * fnumber_2)
    elif operador == '/':
        print(fnumber_1 / fnumber_2)

    sair = input("Deseja sair? [s]im: ").lower()
    if(sair == 's'):
        break

print("FIM!")