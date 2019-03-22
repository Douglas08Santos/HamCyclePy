# HamCyclePi
This is a college work for Project and Analysis of Algorithms.

Este código visa resolver o problema NP-Completo do Ciclo Hamiltoniano em um grafo não orientado.
Como foi feito para uma disciplina, Projeto e Análise de Algoritmos, por questão de didática a forma como foi implementado é a,
ou uma das, menos eficiente possível. 

Basicamente, é inserido um grafo vértice por vértice, informando para cada um deles as arestas que o ligam a outro.
Exemplo: 
O grafo abaixo:

            (0)--(1)--(2)
             |   / \   |
             |  /   \  | 
             | /     \ |
            (4)-------(3)

Inserindo suas informações diria primeiro que: Contem 5 vértices.

Logo após, o programa pergunta vertice a vertice qual ele é adjacente. Enumera automaticamente os vertices com os números de 0 ao
número de vertices digitado. 

Em seguida, ele começa pelo 0 e pergunta a quais outros vertices ele está ligado. A resposta seria: 1 e 4.
Como o proprio programa explica, deve-se informar os vértices ligados todos de uma vez, separados por espaço.

Pela definição de Ciclo Hamiltoniano, para que um grafo seja considerado Hamiltoniano e que tenha um ciclo hamiltoniano deve ser possível
percorrer todos os seus vértices e retornar ao ponto inicial sem passar duas vezes pelo mesmo vértice.

Tendo isso em vista, após receber todas as informações do grafo, o algoritmo então gera uma lista contendo todas as combinações possíveis, sem repetir dentro de cada combinação para obedecer a regra de não visitar duas vezes o mesmo vértice, cada combinação sendo outra lista. Portanto é gerada uma lista de listas.

[0-1-2-3-4] e [3-4-0-1-2] seriam exemplos de duas combinações feitas no grafo acima.

Importante ressaltar que o código não diferencia [0-1-2-3-4] de [4-3-2-1-0], sendo que são a mesma coisa do ponto de vista do grafo,
pois por ser, em teoria, um ciclo, qualquer ponto que se inicie nele retornará para o mesmo lugar. Uma possível, e futura, melhoria do
algoritmo seria excluir essa "falha" e fazer com que considere as duas como iguais.

Geradas todas as combinações, o algoritmo então passa a iterar sobre cada uma delas tentando encontrar um ciclo possível na ordem da
combinação da vez. Ele assume o primeiro elemento como o início do ciclo e parte do segundo. Então ele verifica se o vertice atual
(no caso o 1) possui uma aresta com o anterior (que no caso o 0).

Caso constate que há uma aresta entre eles, então ele passa para o próximo elemento (vertice 2) e repete o processo.

Um Ciclo hamiltoniano é detectado ao se chegar ao fim da combinação, e por consequência, ter adicionado todos os vértices anteriores ao
último. Para isso verifica-se constantemente se a quantidade de vértices no caminho feito é igual ao número total de vértices do grafo.

Acontecendo esta stiuação, o grafo é tido como um Ciclo Hamiltoniano, porém o algoritmo apenas armazena esta combinação e continua para
as próximas, caso haja alguma.

Novamente, é desnecessário tal esforço, pois um ciclo encontrado é suficiente para afimar nossa pergunta se ele é ou não hamiltoniano.
Porém, como a ideia do trabalho é fazer um código de força bruta e o menos eficiente possível, para que seja melhorado no decorrer do 
curso, isso é ignorado.

Ao chegar ao fim de todas as combinações geradas, caso tenha encontrado algum Ciclo hamiltoniano, ele é mostrado. 
Vale ressaltar que, como já foi dito anteriormente, ele não diferencia combinações iguais na ordem invertida, portanto, caso haja alguma
que seja um ciclo hamiltoniano, haverão também a quantidade de vértices do grafo em ciclos válidos. Por questão de obviedade é mostrada
apenas a primeira, começando no ponto 0, devido a aplicação real do algoritmo.

Também vale ressaltar que por questões de visualização, ao detectar um ciclo hamiltoniano, o algoritmo insere novamente o primeiro vértice
apenas para facilitar a leitura.

A aplicação real em que o algoritmo foi implementado é a seguinte:
