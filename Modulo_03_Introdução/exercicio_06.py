"""
Iterando strings com while.
Gere seu nome com '*' antes de cada letra
Ex.: Matheus -> '*M*a*t*h*e*u*s'
"""

nome    = 'Matheus do Vale'
tamanho = len(nome)

novo_nome = ''
i         = 0
while (i < tamanho):
    novo_nome += '*' + nome[i]
    i += 1

print('>> ', novo_nome)