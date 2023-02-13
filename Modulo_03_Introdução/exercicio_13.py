"""
Gerador de CPF
"""

import random

# Gerar nove digitos aleatorios
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

# Calcular digitos do cpf
buffer    = 0
count_reg = 10
digito1 = 0
digito2 = 0

for digito in nove_digitos:
	buffer += int(digito) * count_reg

	count_reg -= 1

digito1 = (buffer * 10) % 11
digito1 = 0 if digito1 > 9 else digito1

buffer    = 0
count_reg = 11

dez_digitos = nove_digitos + str(digito1)
for digito in dez_digitos:
    buffer += int(digito) * count_reg

    count_reg -= 1

digito2 = (buffer * 10) % 11
digito2 = 0 if digito2 > 9 else digito2

print(f"CPF gerado: {nove_digitos}-{digito1}{digito2}")