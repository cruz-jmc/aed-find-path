from data_structures.city_map import CityMap
from collections import deque

def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    if start == goal:
        return [start] # definimos um caso base para verificar se o goal = start

    visitados = {start} # Usamos um conjunto (ou set) para rastrear os nós já visitados 
    # com custo de busca otimizado O(1) -> tempo constante

    fila = deque([(start, [start])]) # Essa fila serve para guardar o nó atual e o caminho
    # até ele na ordem de chegada (FIFO).

    while fila: # Esse while serve para verificar cada intersection e seus vizinhos
        # até chegar no goal
        intersection_atual, road_atual = fila.popleft() # pega o último elemento da esquerda

        if intersection_atual == goal: # se encontrarmos o goal retorna o caminho atual
            return road_atual

        if intersection_atual not in city_map.roads:
            continue # se a intersection não existir ele apenas continua

        for vizinho in city_map.roads[intersection_atual]: # Esse for analisa os vizinhos
            # de cada intersection
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, road_atual + [vizinho]))
            # Esse if serve para um vizinho se tornar a próxima intersection a ser vista

    return [] # Caso não houver solução retorna uma lista vazia pois não existe caminho

    