from data_structures.city_map import CityMap
from another_examples.funcao_heuristica import heuristica
import heapq

def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    if start == goal:
        return [start] # definimos um caso base para verificar se o goal = start

    melhor_custo_gx = {start: 0.0} # Definimos o melhor caminho inicial que seria o próprio start
    # Mudamos agora de conjuntos(visitados) para dicionário porque no A* não precisamos apenas
    # saber se um nó foi visitado, mas sim qual foi o menor custo g(x) para chegar até ele assim como em Dijkstra.

    fila = [] # a fila agora virou uma lista porque o módulo `heapq` transforma uma lista comum do Python
    # em uma Fila de Prioridades (Min-Heap), onde os elementos são ordenados automaticamente pelo menor custo.

    funcao_h_inicial = heuristica(start, goal, city_map.intersections)
    # Definimos o valor da função Heurística inicial começando pelo start

    heapq.heappush(fila, (funcao_h_inicial, 0.0, start, [start]))
    # Nós salvamos uma tupla com 4 informações: (custo_total, custo_gx, nó_atual, caminho_percorrido)
    # O heapq sempre deixará no topo quem tiver o menor custo_total (que é o primeiro item da tupla)

    while fila: # Esse while serve para verificar cada intersection e seus vizinhos
        # até chegar no goal
        custo_total, custo_gx, intersection_atual, road_atual = heapq.heappop(fila) # Remove e retorna a interseção que tem 
        # o MENOR custo total f(x) acumulado até agora.
        # Diferente da BFS que pega cegamente o primeiro da esquerda, o A* extrai o nó mais promissor geometricamente.

        if intersection_atual == goal: # se encontrarmos o goal retorna o caminho atual
            return road_atual

        if intersection_atual not in city_map.roads:
            continue # se a intersection não existir ele apenas continua verificando

        for vizinho in city_map.roads[intersection_atual]: # Esse for analisa os vizinhos
            # de cada intersection
            novo_custo_gx = custo_gx + 1.0 # é como se andasse uma aresta para o vizinho aumentando
            # o custo g(x) que é 1

            if novo_custo_gx < melhor_custo_gx.get(vizinho, float('inf')): # Verifica se esse novo caminho até o vizinho é
                # mais curto do que qualquer outro caminho que tínhamos descoberto antes.

                melhor_custo_gx[vizinho] = novo_custo_gx # Atualiza o dicionário com o novo menor custo g(x) do vizinho

                funcao_h = heuristica(vizinho, goal, city_map.intersections) #atualiza o primeiro parâmetro da função para vizinho

                novo_custo_total = novo_custo_gx + (funcao_h * 0.001)
                # f(x) = g(x) + h(x) -> Multiplicamos por 0.001 para que a distância geométrica não infle o custo unitário (1.0)
                # das ruas

                heapq.heappush(fila, (novo_custo_total, novo_custo_gx, vizinho, road_atual + [vizinho]))
                # Coloca esse vizinho atualizado na fila de prioridades para que ele seja avaliado nos próximos ciclos

    return [] # Caso não houver solução retorna uma lista vazia pois não existe caminho
