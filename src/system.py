# Estrutura de dados principal da Colônia Aurora Siger
# Cada chave é um módulo, contendo seus atributos técnicos e as conexões (arestas) com pesos (distâncias em metros)
# Nível de prioridade vai de 1 a 5, sendo o nível 1 o mais crítico
import math
from collections import deque

colonia_aurora_siger = {
    "Habitação": {
        "consumo_energetico_kwh": 120,
        "prioridade_operacional": 2,
        "capacidade_armazenamento": "500 kWh / 1000L Água",
        "necessidade_comunicacao": "Média",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 50), ("Suporte médico", 20), ("Produção de oxigênio", 80), ("Agricultura", 100)]
    },
    "Centro de controle": {
        "consumo_energetico_kwh": 85,
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "Servidores / Nobreaks",
        "necessidade_comunicacao": "Altíssima",
        "status_operacional": "Ativo",
        "conexoes": [("Habitação", 50), ("Comunicação", 30), ("Armazenamento de energia", 150), ("Laboratório científico", 120)]
    },
    "Armazenamento de energia": {
        "consumo_energetico_kwh": 15,
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "50.000 kWh",
        "necessidade_comunicacao": "Média",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 150), ("Produção de oxigênio", 200), ("Agricultura", 300)]
    },
    "Agricultura": {
        "consumo_energetico_kwh": 250,
        "prioridade_operacional": 3,
        "capacidade_armazenamento": "Estufas / Água",
        "necessidade_comunicacao": "Baixa",
        "status_operacional": "Ativo",
        "conexoes": [("Habitação", 100), ("Armazenamento de energia", 300), ("Laboratório científico", 60)]
    },
    "Laboratório científico": {
        "consumo_energetico_kwh": 180,
        "prioridade_operacional": 4,
        "capacidade_armazenamento": "Amostras / Equipamentos",
        "necessidade_comunicacao": "Alta",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 120), ("Agricultura", 60), ("Suporte médico", 90)]
    },
    "Comunicação": {
        "consumo_energetico_kwh": 95,
        "prioridade_operacional": 2,
        "capacidade_armazenamento": "Terabytes",
        "necessidade_comunicacao": "Altíssima",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 30)]
    },
    "Suporte médico": {
        "consumo_energetico_kwh": 60,
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "Suprimentos médicos",
        "necessidade_comunicacao": "Média",
        "status_operacional": "Ativo",
        "conexoes": [("Habitação", 20), ("Laboratório científico", 90)]
    },
    "Produção de oxigênio": {
        "consumo_energetico_kwh": 300,
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "Tanques O2",
        "necessidade_comunicacao": "Baixa",
        "status_operacional": "Ativo",
        "conexoes": [("Habitação", 80), ("Armazenamento de energia", 200)]
    }
}
def exibir_modulo(nome):

    modulo = colonia_aurora_siger[nome]

    print(f"\n===== {nome.upper()} =====")

    print(f"Consumo energético: {modulo['consumo_energetico_kwh']} kWh")
    print(f"Prioridade operacional: {modulo['prioridade_operacional']}")
    print(f"Capacidade de armazenamento: {modulo['capacidade_armazenamento']}")
    print(f"Necessidade de comunicação: {modulo['necessidade_comunicacao']}")
    print(f"Status operacional: {modulo['status_operacional']}")

    print("\nConexões:")

    for destino, distancia in modulo["conexoes"]:
        print(f"- {destino} ({distancia}m)")
#print(exibir_modulo("Habitação"))

def consultar_modulos():

    while True:

        print("\n" + "=" * 50)
        print("CONSULTA DE MÓDULOS")
        print("=" * 50)

        print("1 - Habitação")
        print("2 - Centro de controle")
        print("3 - Armazenamento de energia")
        print("4 - Agricultura")
        print("5 - Laboratório científico")
        print("6 - Comunicação")
        print("7 - Suporte médico")
        print("8 - Produção de oxigênio")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        match opcao:

            case "1":
                exibir_modulo("Habitação")
                input("Pressione ENTER para voltar:")

            case "2":
                exibir_modulo("Centro de controle")
                input("Pressione ENTER para voltar:")

            case "3":
                exibir_modulo("Armazenamento de energia")
                input("Pressione ENTER para voltar:")

            case "4":
                exibir_modulo("Agricultura")
                input("Pressione ENTER para voltar:")
            case "5":
                exibir_modulo("Laboratório científico")
                input("Pressione ENTER para voltar:")
            case "6":
                exibir_modulo("Comunicação")
                input("Pressione ENTER para voltar:")
            case "7":
                exibir_modulo("Suporte médico")
                input("Pressione ENTER para voltar:")
            case "8":
                exibir_modulo("Produção de oxigênio")
                input("Pressione ENTER para voltar:")
            case "0":
                break

            case _:
                print("\nOpção inválida.")


# MATRIZ DE ADJACÊNCIA

modulos = list(colonia_aurora_siger.keys())
matriz = [[0 for _ in modulos] for _ in modulos]

for i, origem in enumerate(modulos):
    for destino, peso in colonia_aurora_siger[origem]["conexoes"]:
        j = modulos.index(destino)
        matriz[i][j] = peso



# BFS
def bfs(inicio):
    visitados = set()
    fila = deque([inicio])

    print("\nBFS - Exploração da rede:")

    while fila:
        no = fila.popleft()

        if no not in visitados:
            print(no)
            visitados.add(no)

            for vizinho, _ in colonia_aurora_siger[no]["conexoes"]:
                if vizinho not in visitados:
                    fila.append(vizinho)


# DFS
def dfs(no, visitados=None):
    if visitados is None:
        visitados = set()

    print(no)
    visitados.add(no)

    for vizinho, _ in colonia_aurora_siger[no]["conexoes"]:
        if vizinho not in visitados:
            dfs(vizinho, visitados)


# DIJKSTRA
def dijkstra(inicio):
    dist = {no: float("inf") for no in colonia_aurora_siger}
    dist[inicio] = 0
    visitados = set()

    while len(visitados) < len(colonia_aurora_siger):
        atual = None
        menor = float("inf")

        for no in dist:
            if no not in visitados and dist[no] < menor:
                menor = dist[no]
                atual = no

        if atual is None:
            break

        visitados.add(atual)

        for vizinho, peso in colonia_aurora_siger[atual]["conexoes"]:
            if dist[atual] + peso < dist[vizinho]:
                dist[vizinho] = dist[atual] + peso

    return dist


# MODELAGEM MATEMÁTICA

def perda_energetica(E0, d):
    return E0 * math.exp(-0.002 * d)


# FUNÇÕES EXECUTÁVEIS (MENU)
def executar_modelagem():
    print("\nModelo: E(d) = E₀ × e^(-0.002 × d)")

    E0 = float(input("Energia inicial: "))
    d = float(input("Distância: "))

    resultado = perda_energetica(E0, d)

    print(f"Energia final: {resultado:.2f}")
    input("\nENTER para continuar...")


def executar_dijkstra():
    distancias = dijkstra("Habitação")

    print("\nDijkstra - Menores caminhos:")
    for no, valor in distancias.items():
        print(f"{no}: {valor}")

    input("\nENTER para continuar...")


def executar_bfs():
    bfs("Habitação")
    input("\nENTER para continuar...")


def executar_dfs():
    dfs("Habitação")
    input("\nENTER para continuar...")