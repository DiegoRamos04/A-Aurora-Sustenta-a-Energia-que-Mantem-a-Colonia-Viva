import math
import random
import os
import time
from collections import deque

# ==========================================
# ESTRUTURA DE DADOS PRINCIPAL DA COLÔNIA
# ==========================================
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

# ==========================================
# MATRIZ DE ADJACÊNCIA
# ==========================================
modulos = list(colonia_aurora_siger.keys())
matriz = [[0 for _ in modulos] for _ in modulos]

for i, origem in enumerate(modulos):
    for destino, peso in colonia_aurora_siger[origem]["conexoes"]:
        j = modulos.index(destino)
        matriz[i][j] = peso

# ==========================================
# UTILITÁRIOS DA INTERFACE
# ==========================================
def limpar_tela():
    # Limpa o terminal no Windows ('nt') ou Linux/Mac ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def selecionar_modulo(mensagem_input):
    """Garante que o usuário seleciona um módulo válido dinamicamente."""
    opcoes = list(colonia_aurora_siger.keys())
    print("\nMódulos disponíveis:")
    for i, modulo in enumerate(opcoes, 1):
        print(f"  [{i}] {modulo}")
    
    while True:
        try:
            escolha = int(input(f"\n{mensagem_input} "))
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]
            else:
                print("   Opção inválida. Escolha um número da lista.")
        except ValueError:
            print("   Entrada inválida. Digite um número.")

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

def consultar_modulos():
    while True:
        print("\n" + "=" * 50)
        print("CONSULTA DE MÓDULOS")
        print("=" * 50)
        
        opcoes = list(colonia_aurora_siger.keys())
        for i, modulo in enumerate(opcoes, 1):
            print(f"{i} - {modulo}")
        print("0 - Voltar")

        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 0:
                break
            elif 1 <= opcao <= len(opcoes):
                nome_modulo = opcoes[opcao - 1]
                exibir_modulo(nome_modulo)
                input("\nPressione ENTER para voltar...")
            else:
                print("\nOpção inválida.")
        except ValueError:
            print("\nPor favor, digite um número válido.")

# ==========================================
# ALGORITMOS DE GRAFOS COM SELEÇÃO DINÂMICA
# ==========================================

# BFS - Mapeamento por Níveis
def executar_bfs():
    print("\n" + "=" * 50)
    print("Mapeamento da Rede por Níveis (BFS)")
    print("=" * 50)
    
    inicio = selecionar_modulo(" Digite o número do módulo para iniciar a varredura:")
    
    print(f"\nIniciando varredura a partir de: {inicio}")
    
    visitados = {inicio}
    fila = deque([(inicio, 0)])
    niveis = {}

    while fila:
        atual, nivel = fila.popleft()

        if nivel not in niveis:
            niveis[nivel] = []
        niveis[nivel].append(atual)

        for vizinho, _ in colonia_aurora_siger[atual]["conexoes"]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, nivel + 1))

    for nivel in sorted(niveis):
        print(f"Nível {nivel}: {', '.join(niveis[nivel])}")
        
    input("\nENTER para continuar...")

# DFS - Inspeção Profunda de Infraestrutura
def executar_dfs():
    print("\n" + "=" * 50)
    print("Inspeção de Infraestrutura (DFS)")
    print("=" * 50)
    
    inicio = selecionar_modulo(" Digite o número do módulo para iniciar a inspeção:")
    visitados = set()
    ordem_visita = []

    def dfs_recursiva(modulo):
        visitados.add(modulo)
        ordem_visita.append(modulo)
        for vizinho, _ in colonia_aurora_siger[modulo]["conexoes"]:
            if vizinho not in visitados:
                dfs_recursiva(vizinho)

    dfs_recursiva(inicio)

    print("\nCaminho percorrido pela equipe de manutenção:")
    print(" -> ".join(ordem_visita))

    erros = random.randint(0, 3)
    if erros == 0:
        print("\n[STATUS] Nenhum erro estrutural encontrado durante a inspeção.")
    else:
        print(f"\n[ALERTA] Foram encontrados {erros} erro(s) de conexão.")
        print("[RESOLUÇÃO] Todos os erros foram corrigidos pelos sistemas automatizados.")
        
    input("\nENTER para continuar...")

# DIJKSTRA - Cálculo da Menor Rota Energética
def executar_dijkstra():
    print("\n" + "=" * 50)
    print("Otimização de Rota Energética (Dijkstra)")
    print("=" * 50)
    
    # Origem fixa no Armazenamento, o usuário escolhe apenas o destino
    origem = "Armazenamento de energia"
    destino = selecionar_modulo(f" Rota saindo de '{origem}'. Digite o número do módulo de destino:")
    
    distancias = {no: float("inf") for no in colonia_aurora_siger}
    anteriores = {no: None for no in colonia_aurora_siger}
    distancias[origem] = 0
    nao_visitados = list(colonia_aurora_siger.keys())

    while nao_visitados:
        atual = min(nao_visitados, key=lambda v: distancias[v])
        nao_visitados.remove(atual)

        if atual == destino:
            break

        for vizinho, peso in colonia_aurora_siger[atual]["conexoes"]:
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
    print(f"Distância total de transmissão: {distancias[destino]} metros")
    
    input("\nENTER para continuar...")

# ==========================================
# MODELAGEM MATEMÁTICA
# ==========================================
def perda_energetica(E0, d):
    return E0 * math.exp(-0.002 * d)

def executar_modelagem():
    print("\n" + "=" * 50)
    print("Cálculo de Decaimento Exponencial de Energia")
    print("=" * 50)
    print("Modelo: E(d) = E₀ × e^(-0.002 × d)")

    try:
        E0 = float(input("\nEnergia enviada na fonte (kWh): "))
        d = float(input("Distância do cabo de transmissão (metros): "))
        resultado = perda_energetica(E0, d)
        perda = E0 - resultado
        
        print(f"\nResultados da Transmissão:")
        print(f"Energia que chegou ao destino: {resultado:.2f} kWh")
        print(f"Perda térmica no trajeto: {perda:.2f} kWh")
    except ValueError:
        print("\nErro: Digite apenas valores numéricos.")
        
    input("\nENTER para continuar...")

# ==========================================
# MENU PRINCIPAL (LOOP DA APLICAÇÃO)
# ==========================================
def exibir_cabecalho():
    limpar_tela()
    print("\n" + "═" * 65)
    print("  SIGIC - SISTEMA INTELIGENTE DE GERENCIAMENTO DA COLÔNIA")
    print("    BASE: AURORA SIGER | STATUS: OPERACIONAL")
    print("═" * 65)
    print("\n  [ MENU PRINCIPAL DE GOVERNANÇA ] \n")

if __name__ == "__main__":
    while True:
        exibir_cabecalho()
        
        print("  [ 1 ]  Consultar Módulos da Infraestrutura")
        print("  [ 2 ]  Simular Modelagem Matemática (Perda Energética)")
        print("  [ 3 ]  Otimizar Rota de Transmissão (Algoritmo de Dijkstra)")
        print("  [ 4 ]  Mapear Rede por Níveis (Algoritmo BFS)")
        print("  [ 5 ]  Executar Inspeção Profunda (Algoritmo DFS)")
        print("  [ 0 ]  Desconectar e Encerrar Sistema")
        
        print("\n" + "═" * 65)
        opcao = input("  ➥ Digite o código de comando: ")

        match opcao:
            case "1":
                limpar_tela()
                consultar_modulos()
            case "2":
                limpar_tela()
                executar_modelagem()
            case "3":
                limpar_tela()
                executar_dijkstra()
            case "4":
                limpar_tela()
                executar_bfs()
            case "5":
                limpar_tela()
                executar_dfs()
            case "0":
                limpar_tela()
                print("\n" + "═" * 65)
                print("  Desconectando do terminal central da Colônia Aurora Siger...")
                print("    Salvando logs de rede e fechando conexões...")
                time.sleep(1.5)
                print("    Sistema encerrado com segurança. Bom descanso, engenheiro!")
                print("═" * 65 + "\n")
                break
            case _:
                print("\n   Comando inválido. Código não reconhecido pela rede.")
                time.sleep(2)
