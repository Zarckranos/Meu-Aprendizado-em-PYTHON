# Exercicio 01 ======================================================
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print(">> EXERCICIO 01:")
number = input('Digite um número inteiro: ')

if number.isdigit():
    number_int = int(number)

    if (number_int % 2) == 0:
        print(f"{number} é um número PAR.")
    else:
        print(f"{number} é número ÍMPAR.")
        
else:
    print(">> Você não digitou um número inteiro!")

print()

# Exercicio 02 ======================================================
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
print(">> EXERCICIO 02:")
hora = input("Digita uma hora: ")

try:
    hora_int = int(hora)

    if (hora_int >= 0 and hora_int < 12):
        print("Bom dia!")
    elif (hora_int >= 12 and hora_int < 18):
        print("Boa tarde!")
    elif (hora_int >= 18 and hora_int < 24):
        print("Boa noite!")
    else:
        print("Hora invalida")

except:
    print(">> Formato da hora invalido!")
    print(">> Tente um valor inteiro entre 0 e 23.")

print()

# Exercicio 03 ======================================================
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
print(">> EXERCICIO 03:")
nome = input("Digite seu primeiro nome: ")

nome_len = len(nome)

if (nome_len <= 4):
    print("Seu nome é curto.")
elif (nome_len >= 5 and nome_len <= 6):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")