from data_structures.city_map import CityMap
# Uma obs: O Dijkstra não usa deque já que usa a biblioteca heapq
import heapq

def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    if start == goal:
        return [start]

    melhor_custo_gx = {start: 0.0} # Definimos o melhor caminho inicial que seria o próprio start
    # Mudamos agora de conjuntos(visitados) para dicionário porque no A* e Dijkstra não precisamos apenas
    # saber se um nó foi visitado, mas sim qual foi o menor custo g(x) para chegar até ele.

    fila = [] # a fila é uma lista de prioridades gerenciada pelo heapq.

    # A prioridade na fila passa a ser apenas o custo real inicial (0.0)
    # Mudamos a tupla para colocar o custo real acumulado na frente: (custo_gx, nó_atual, caminho_percorrido)
    heapq.heappush(fila, (0.0, start, [start]))

    while fila: # Esse while serve para verificar cada intersection e seus vizinhos até chegar no goal
        
        # Ordenamos apenas por custo_gx (g(x))
        custo_gx, intersection_atual, road_atual = heapq.heappop(fila) 
        # Remove e retorna a interseção que tem o MENOR custo acumulado real g(x) até agora (o mais a direita).

        if intersection_atual == goal:
            return road_atual

        if intersection_atual not in city_map.roads:
            continue

        for vizinho in city_map.roads[intersection_atual]:
            novo_custo_gx = custo_gx + 1.0 # como se movesse mais 1 caminho de peso 1

            if novo_custo_gx < melhor_custo_gx.get(vizinho, float('inf')): # Verifica se esse novo caminho até o vizinho é mais curto.

                melhor_custo_gx[vizinho] = novo_custo_gx # Atualiza o dicionário com o novo menor custo g(x) do vizinho

                # No Dijkstra, a própria variável 'novo_custo_gx' dita a prioridade do nó.

                # Enviamos para a fila usando o novo_custo_gx na frente para manter a ordenação correta
                heapq.heappush(fila, (novo_custo_gx, vizinho, road_atual + [vizinho]))

    return [] # Caso não houver solução retorna uma lista vazia pois não existe caminho