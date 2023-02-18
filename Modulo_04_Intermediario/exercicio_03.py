# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '15'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

pontos = 0
for i in perguntas:
    print('Pergunta:', i.get('Pergunta'), '\n')
    print('Opções:')
    for w, opcoes in enumerate(i['Opções']):
        print(f'{w}) {opcoes}')

    escolha = None
    try:
        escolha = int(input('Escolha uma opção: '))
    except ValueError as ve:
        print("Errou!\n")
        continue

    if(escolha > len(i['Opções'])):
        print("Errou!\n")
        continue

    if (i['Opções'][escolha] == i['Resposta']):
        print("Acertou!\n")
        pontos += 1
    else:
        print("Errou!\n")

print(f'Você acertou {pontos} de {len(perguntas)} perguntas.')