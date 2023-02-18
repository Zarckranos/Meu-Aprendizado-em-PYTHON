# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmentro.

def multiply(factor1):
    def product(factor2):
        return factor1 * factor2
    
    return product

duplicate     = multiply(2)
triple        = multiply(3)
quadruple     = multiply(4)
quintuple     = multiply(5)

print('duplicate:', duplicate(5))
print('triple:   ', triple(5))
print('quadruple:', quadruple(5))
print('quintuple:', quintuple(5))