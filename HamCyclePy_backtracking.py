# Python program for solution of 
# hamiltonian cycle problem 
import time
import timeit

class Grafo():
    def __init__(self, vert):
        self.grafo = [[0 for column in range(vert)]
                            for row in range(vert)]
        self.vert = vert

    # verifica se o vertice pode ser adicionado ao caminho recebido
    def verifica(self, v, posicao, caminho):
        # se o vertice não for adjacente ao ulttimo não pode
        if self.grafo[caminho[posicao-1]][v] == 0:
            return False
        # se o vertice já estiver no caminho, não pode
        for vert in caminho:
            if vert == v:
                return False

        return True

    def findeHamCycle(self, caminho, posicao):
        # caso base: caminho contem todos os vertices
        if posicao == self.vert:
            # o ultimo e o primeiro vertice devem ser adjacentes
            if self.grafo[caminho[posicao-1]][caminho[0]]  == 1:
                # adicionando o vertice inical na rota do caminhao
                caminho.append(caminho[0])
                return True
            else:
                return False
        # testando vertices que possam ser viáveis
        for vert in range(1, self.vert):
            # se for possivel adicionar o vertice ao caminho
            if(self.verifica(vert, posicao, caminho)):
                caminho[posicao] = vert
                # e ele acrescentar à construção do ciclo, adiciona-se
                if(self.findeHamCycle(caminho, posicao+1)):
                    return True
                # caso não acrescente, descarta-se
                caminho[posicao] = -1
    
        return False

    def inicializa(self):
        # coloca todos os valores como -1
        caminho = [-1] * self.vert
        # o ponto inicial é a sede, vertice 0
        caminho[0] = 0

        # caso base: não há um ciclo hamiltoniano, mas ja salva os calculos
        # pois se houver, ja foi encontrado
        if not(self.findeHamCycle(caminho, 1)):
            print("Não existem ciclos hamiltonianos para este grafo.")
            return False

        print("O ciclo hamiltoniano para estas entregas é o seguinte:")
        for vert in caminho:
           print(str(vert) + ", ", end="")
        
        print("\n")  

  
''' Let us create the following graph 
      (0)--(1)--(2) 
       |   / \   | 
       |  /   \  | 
       | /     \ | 
      (3)-------(4)    '''
g1 = Grafo(5) 
g1.grafo = [ [0, 1, 0, 1, 0], 
             [1, 0, 1, 1, 1],  
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1],  
             [0, 1, 1, 1, 0], ] 
g1.inicializa()

g2 = Grafo(8)
g2.grafo =[[0, 1, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 0, 0, 1, 0, 0],  
           [0, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 0, 0, 0, 0, 1],  
           [1, 0, 0, 1, 0, 1, 0, 1],
           [0, 1, 0, 0, 1, 0, 1, 0],
           [0, 0, 1, 0, 0, 1, 0, 1],
           [0, 0, 0, 1, 1, 0, 1, 0]]
g2.inicializa()

g3 = Grafo(20)
            #0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19   
g3.grafo = [[0,1,0,0,1,0,0,0,0,0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1,0,1,0,0,0,0,0,0,0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0,1,0,1,0,0,0,0,0,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0,0,1,0,1,0,0,1,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1,0,0,1,0,1,0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0,0,0,0,1,0,1,0,0,0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0,0,0,0,0,1,0,1,0,0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0,0,0,1,0,0,1,0,1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0,0,0,0,0,0,0,1,0,1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0,0,1,0,0,0,0,0,1,0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0,0,0,0,0,0,0,0,0,1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0,1,0,0,0,0,0,0,0,0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0,0,0,0,0,0,0,0,0,0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [1,0,0,0,0,0,0,0,0,0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0,0,0,0,0,1,0,0,0,0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [0,0,0,0,0,0,1,0,0,0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0,0,0,0,0,0,0,0,1,0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0,0,0,0,0,0,0,0,0,0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0,0,0,0,0,0,0,0,0,0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]        
]

start = timeit.default_timer()
g3.inicializa()
end = timeit.default_timer()
print("Tempo de execução %f" % (end - start))