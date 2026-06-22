from data_structures.city_map import CityMap
from collections import deque

def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    if start == goal:
        return [start]

    visitados = {start}

    fila = deque([(start, [start])])

    while fila:
        intersection_atual, road = fila.popleft()

        if intersection_atual == goal:
            return road

        if intersection_atual not in city_map.roads:
            continue

        for vizinho in city_map.roads[intersection_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, road + [vizinho]))

    return []