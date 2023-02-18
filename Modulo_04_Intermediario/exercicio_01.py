# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.
def multiplica(*args):
    total = 1
    for number in args:
        total = total * number
    
    return total

resultado = multiplica(5, 5, 5, 5, 5)
print(resultado)

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def paridade(number):
    if (number % 2) == 0:
        return f'{number} é par!'
    
    return f'{number} é ímpar!'

print(paridade(56321))