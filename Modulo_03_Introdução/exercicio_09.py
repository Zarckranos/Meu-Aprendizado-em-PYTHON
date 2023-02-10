"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

PALAVRA_SECRETA = 'python'

end_game    = False
tentativas  = 0
palavra_dig = ''
palavra_aux = ''
memoria     = ''

# Colocando '*' na palavra digitada para mostrar ao usuário.
tamanho_PS  = len(PALAVRA_SECRETA)
print(f"Sua palavra secreta tem {tamanho_PS} letras.")
palavra_dig = '*' * tamanho_PS
print(palavra_dig, '\n')

while not end_game:
    letra = input('Digite uma letra: ').lower()
    if (len(letra) > 1):
        print(">> Digite apenas uma letra!")
        continue

    if letra in memoria:
        print(">> Letra já digitada!")
        continue
    
    memoria += letra
    tentativas += 1

    # Verificar se a letra digitada está na PALAVRA SECRETA
    palavra_aux = ''
    for i in range(tamanho_PS):
        if palavra_dig[i] != '*':
            palavra_aux += palavra_dig[i]
            continue
        
        if (letra == PALAVRA_SECRETA[i]):
            palavra_aux += letra
        else:
            palavra_aux += '*'
    
    palavra_dig = palavra_aux
    print(palavra_dig)

    # Verificar se a palavra digitada é igual a PALAVRA SECRETA
    if(palavra_dig == PALAVRA_SECRETA):
        end_game = True

print("\nFim de jogo, parabéns!")
print("Número de tentativas: ", tentativas)