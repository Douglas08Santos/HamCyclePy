import itertools

# grafo de 8 vertices abaixo. Imagem disponivel em: encurtador.com.br/diFIN
# Possui um ciclo hamiltoniano [0-1-2-3-4-5-6-7-0]
'''
          (0)-----------(1)
           | `.       ,´ |  
           |  (7)---(6)  |
           |   |     |   |
           |  (4)---(5)  |
           | ,´       `. |
          (3)-----------(2)

grafo = {0:[0, 1, 0, 1, 1, 0, 0, 0],
         1:[1, 0, 1, 0, 0, 1, 0, 0],  
         2:[0, 1, 0, 1, 0, 0, 1, 0],
         3:[1, 0, 1, 0, 0, 0, 0, 1],  
         4:[1, 0, 0, 1, 0, 1, 0, 1],
         5:[0, 1, 0, 0, 1, 0, 1, 0],
         6:[0, 0, 1, 0, 0, 1, 0, 1],
         7:[0, 0, 0, 1, 1, 0, 1, 0]} 

# grafo de 5 vertices desenhado abaixo. Possui um ciclo hamiltoniano [0-1-2-3-4-0]

            (0)--(1)--(2)
             |   / \   |
             |  /   \  | 
             | /     \ |
            (4)-------(3)


grafo = {0:[0, 1, 0, 0, 1],
         1:[1, 0, 1, 1, 1],  
         2:[0, 1, 0, 1, 0],
         3:[0, 1, 1, 0, 1],  
         4:[1, 1, 0, 1, 0] } '''

# Recebendo o grafo que representa os pontos de entregas do caminhao
print("Informe a quantidade de pontos de entrega (vértices): ")
vert = (int(input()))
print(vert)
# começando a perguntar as arestas dos vertices
print("Certo. Diga agora as vias (arestas) de cada ponto de entrega (vertices) ")
# variavel para guardar as ligações
vertices = []
lista_adjacencias = []
for i in range(vert):
    ''' esta lista contem os vertices, apenas para
        podermos utilizar a função zip mais a frente'''
    vertices.append(i)
    print(i)
    if(i == 0):
        print("As vias que saem da distribuidora (separados por espaço):")
    else:
        print("As vias que existem no ponto " + str((i)) + "(separados por espaço):")
    vias = input().split(" ")
    for s in range(len(vias)):
        vias[s] = int(vias[s])
    arestas = []
    for x in range(vert):
        arestas.append(0)
        
    # neste for preparamos a lista que contem as informações
    # se há ligação entre os vertices ou nao
    # de forma x : [1,0,...,n] significa que o vertice x
    # tem ligação com 1 e com 2 não e assim por diante
    for j in vias:
        arestas[j] = 1
    print("arestas: " + str(arestas))
    lista_adjacencias.append(arestas)
grafo = dict(zip(vertices, lista_adjacencias))

print("O grafo digitado possui as seguintes listas de adjacencias: ")
for v in range(vert):
    print(str(v) + ":[", end='')
    for l in range(vert):
        print(str(grafo[v][l]) + str(", "), end='')
    print("]")

# grafo coletado e organizado

# variavel para guardar a quantidade de vertices
vert = grafo.__len__()

''' a função permutations retorna uma lista
    com todas as combinações possíveis das CHAVES
    do dicionario que representa o grafo'''
rotas = itertools.permutations(grafo)

# guarda as variações do ciclo, começando de diferentes pontos
hamRotes = []
# persiste o ultimo vertice adicionado
last = -1
# contadores de iterações
itj = 0
itk = 0
# quantidade de combinações recebidas da função permutations() acima
rotes = 0

# cada i é uma rota(combinação)
for i in rotas:
    rotes += 1
    # cada nova iteração reinicia o caminho
    path = []
    # e coloca o persistidor de ultimo em "default"
    last = -1
    # cada j é um vertice da rota (combinação)
    for j in i:
        itj += 1
        # se o last for o default, insere-se o primeiro
        if(last == -1):
            # last se torna agora o inserido
            last = j
            path.append(j)
            # proxima iteração
            continue
        # cada k vai representar os indices da lista de adjacencia do vertice j
        for k in range(vert):
            itk += 1
            # se em k houver uma aresta com j e k for o ultimo vertice adicionado
            # então eles são adjacentes
            if(grafo[j][k] == 1 and k == last):
                # last se torna o inserido
                last = j
                # adiciona-se o vertice ao caminho da rota
                path.append(j)
                break
            
        # caso todos os vertices tenham sido inseridos
        if(len(path) == vert):
            # e o ultimo inserido for adjacente ao inicial
            # então formou-se um ciclo hamiltoniano
            if(grafo[last][path[0]] == 1):
                # adiciona-se o inicial novamente apenas para que conste na rota
                path.append(path[0])
                # e guardando a variação do ciclo,
                # que pode começar de qualquer ponto
                hamRotes.append(path)

print("Existe uma rota que forma um ciclo hamiltoniano. A rota é: ")
for i in hamRotes:
    # imprimindo apenas a versão que começa do ZERO
    # apenas por definição própria
    # pois na aplicação real, seria considerado o centro de distribuição
    if(i[0] == 0):
        print(i)
        break
print("\nCombinações possiveis: " + str(rotes))
print("Com " + str(itj) + " iterações de comparação de viabilidade do proximo ponto(j) e " + str(itk) + " de verificação de adjacência(k).")

# This code was developed by Isaias Oliveira
# Esse código foi desenvolvido por Isaias Oliveira
    









