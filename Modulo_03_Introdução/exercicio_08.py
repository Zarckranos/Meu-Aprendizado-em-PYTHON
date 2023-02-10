"""
Saber qual letra mais apareceu dentro da frase.
"""

frase = "O python é uma linguagem de programação multiparadigma. "\
    "Python foi criado por Guido van Rossum."

letra_maior = 0
i = 0
while i < len(frase):
    if (frase[i] == " "):
        i += 1
        continue

    count = frase.count(frase[i])

    if (count > letra_maior):
        letra_maior = i

    i += 1

print(f"A letra com mais ocorrência na frase é: '{frase[letra_maior]}'")