from collections import deque
import random

grafo = {
    "COM": [("CCO", 30)],
    "CCO": [("COM", 30), ("HAB", 50), ("AEN", 150), ("LAB", 120)],
    "HAB": [("CCO", 50), ("MED", 20), ("OXI", 80), ("AGR", 100)],
    "AEN": [("CCO", 150), ("AGR", 300), ("OXI", 200)],
    "LAB": [("CCO", 120), ("AGR", 60), ("MED", 90)],
    "MED": [("LAB", 90), ("HAB", 20)],
    "OXI": [("HAB", 80), ("AEN", 200)],
    "AGR": [("HAB", 100), ("AEN", 300), ("LAB", 60)],
}


# ==========================================
# BFS - Localizar módulos por níveis
# ==========================================
def bfs_niveis(grafo, inicio):
    visitados = {inicio}
    fila = deque([(inicio, 0)])
    niveis = {}

    while fila:
        atual, nivel = fila.popleft()

        if nivel not in niveis:
            niveis[nivel] = []

        niveis[nivel].append(atual)

        for vizinho, _ in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, nivel + 1))

    print("\n=== MÓDULOS POR NÍVEL ===")
    for nivel in sorted(niveis):
        print(f"Nível {nivel}: {', '.join(niveis[nivel])}")


# ==========================================
# DFS - Inspeção de infraestrutura
# ==========================================
def dfs_inspecao(grafo, inicio):
    visitados = set()
    ordem_visita = []

    def dfs(modulo):
        visitados.add(modulo)
        ordem_visita.append(modulo)

        for vizinho, _ in grafo[modulo]:
            if vizinho not in visitados:
                dfs(vizinho)

    dfs(inicio)

    print("\n=== INSPEÇÃO DE INFRAESTRUTURA ===")
    print("Ordem de inspeção:")
    print(" -> ".join(ordem_visita))

    erros = random.randint(0, 5)

    if erros == 0:
        print("\nNenhum erro encontrado durante a inspeção.")
    else:
        print(f"\nForam encontrados {erros} erro(s).")
        print("Todos os erros foram corrigidos com sucesso.")


# ==========================================
# Dijkstra - Menor caminho
# ==========================================
def dijkstra(grafo, origem, destino):
    distancias = {}
    anteriores = {}

    for vertice in grafo:
        distancias[vertice] = float("inf")
        anteriores[vertice] = None

    distancias[origem] = 0
    nao_visitados = list(grafo.keys())

    while nao_visitados:
        atual = min(nao_visitados, key=lambda v: distancias[v])
        nao_visitados.remove(atual)

        if atual == destino:
            break

        for vizinho, peso in grafo[atual]:
            nova_distancia = distancias[atual] + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = atual

    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]

    caminho.reverse()

    print("\n=== MENOR ROTA ENCONTRADA ===")
    print(" -> ".join(caminho))
    print(f"Distância total: {distancias[destino]} metros")

bfs_niveis(grafo, "AEN")

dfs_inspecao(grafo, "HAB")

dijkstra(grafo, "AEN", "MED")