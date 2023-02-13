"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos
valores por uma contagem regressiva começando de 10.

Ex.:  746.824.890-70 (746824890)
   10   9   8   7   6   5   4   3   2
 *  7   4   6   8   2   4   8   9   0
   -----------------------------------
   70  36  48  56  12  20  32  27   0

Somar todos os resultados:
  70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
Multiplicar os resultado anterior por 10:
  301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
  3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
caso contrário:
    resultado é o valor da conta
"""

cpf = '74682489070'

# Para armazenar o valor do calculo
buffer    = 0
count_reg = 10
cpf_int   = None
digito1 = 0

for i in range(9):
	try:
		cpf_int = int(cpf[i])
	except ValueError:
		print("VALUE ERROR!")
		break
	
	buffer += cpf_int * count_reg

	count_reg -= 1

digito1 = (buffer * 10) % 11

digito1 = 0 if digito1 > 9 else digito1

print(f"O primeiro digito do CPF é: {digito1}")
