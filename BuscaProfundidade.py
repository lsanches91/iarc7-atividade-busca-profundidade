grafo = {
    "A": ['C','J'],
    'B': ['C','F'],
    'C': ['A','B','F'],
    'D': ['G','M'],
    'E': ['H','I'],
    'F': ['B','C','H'],
    'G': ['D','J'],
    'H': ['E','F','J','K'],
    'I': ['E','K'],
    'J': ['A','G','H','M'],
    'K': ['H','I','L'],
    'L': ['K'],
    'M': ['D','J']
}

visitados = []
pilhaAux = []

def buscaProfundidade(raiz, procurado):
    if raiz == procurado:
        print('Valor Encontrado')
        return
    else:
        visitados.append(raiz)
        print('->' + raiz, end=" ")
        for i in grafo[raiz]:
            if i not in visitados:
                pilhaAux.append(raiz)
                return buscaProfundidade(i, procurado)
        if len(pilhaAux) != 0:
            return buscaProfundidade(pilhaAux.pop(), procurado)
        else:
            print('Valor não encontrado.')
            return



if __name__ == '__main__':
    
    busca = input('Digite o valor que quer buscar: ')
    
    buscaProfundidade('H', busca)

    print(visitados)
    
    # pilhaAux = grafo['H']
    