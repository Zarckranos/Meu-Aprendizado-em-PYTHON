"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma contagem regressiva começando do 11.

Ex.:  746.824.890-70 (746824890)
   11  10   9   8   7   6   5   4   3   2
 *  7   4   6   8   2   4   8   9   0   7
   --------------------------------------
   77  40  54  64  14  24  40  36   0  14

Somar todos os resultados:
  77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
Multiplicar os resultado anterior por 10:
  363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
  3630 % 11 = 0
Se o resultado anterior for maior que 9:
  resultado é 0
caso contrário:
  resultado é o valor da conta
"""

cpf = '74682489070'

# Para armazenar o valor do calculo
buffer    = 0
count_reg = 11
cpf_int   = None
digito2 = 0

for i in range(10):
	try:
		cpf_int = int(cpf[i])
	except ValueError:
		print("VALUE ERROR!")
		break
	
	buffer += cpf_int * count_reg

	count_reg -= 1

digito2 = (buffer * 10) % 11

digito2 = 0 if digito2 > 9 else digito2

print(f"O primeiro digito do CPF é: {digito2}")