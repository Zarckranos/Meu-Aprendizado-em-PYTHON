"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebrer com erros de índices
inexistentes na lista.
"""

import os

lista_compras = []

while True:
    print(">> Selecione uma opção")
    opcao = input("[i]nserir - [a]pagar - [l]istar: ").lower()
    os.system('cls')

    if (opcao == 'i'):
        produto = input("Produto: ")
        lista_compras.append(produto)

    elif (opcao == 'a'):
        if (len(lista_compras) < 1):
            print("Lista Vazia, nada para apagar.")
        else:
            try:
                indice = int(input("Escolha o índice para apagar: "))
                print(f"{lista_compras[indice]} foi removido da sua lista.")
                del lista_compras[indice]
            except ValueError:
                print("Digite um número inteiro.")
            except IndexError:
                print("Índice não existe na lista.")
            except Exception:
                print("Erro desconhecido.")

    elif (opcao == 'l'):
        if (len(lista_compras) < 1):
            print("Lista Vazia, nada para listar.")
        else:
            print("Lista de compras ==========")
            for i, item in enumerate(lista_compras):
                print(i, item)
            print("===========================")

    else:
        print("Digite uma operação válida!")