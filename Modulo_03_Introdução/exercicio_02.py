# O exercicio consiste em calcular o IMC baseado nos dados abaixo ===
nome   = 'Matheus Almeida'
altura = 1.65
peso   = 52.0
imc    = ...
# ===================================================================

# Calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
imc = peso / (altura ** altura)

print(nome + " possui " + str(altura) + " de altura e pesa " + str(peso) + "kg")
print(f"IMC: {imc:.3f}")