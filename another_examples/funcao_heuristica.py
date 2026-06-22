def heuristica(intersection_atual: int, goal: int, intersections: dict):
    x1, y1 = intersections[intersection_atual]
    x2, y2 = intersections[goal]
# Utiliza-se a equação euclidiana para o cálculo de distância.
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
    