# Estrutura de dados principal da Colônia Aurora Siger
# Cada chave é um módulo, contendo seus atributos técnicos e as conexões (arestas) com pesos (distâncias em metros)
# Nível de prioridade vai de 1 a 5, sendo o nível 1 o mais crítico
import math


colonia_aurora_siger = {
    "Habitação": {
        "consumo_energetico_kwh": 120,
        "prioridade_operacional": 2, 
        "capacidade_armazenamento": "500 kWh (Baterias de backup) / 1000L Água",
        "necessidade_comunicacao": "Média",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 50), ("Suporte médico", 20), ("Produção de oxigênio", 80), ("Agricultura", 100)]
    },
    "Centro de controle": {
        "consumo_energetico_kwh": 85,
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "Servidores de Dados (Petabytes) / 200 kWh (Nobreaks)",
        "necessidade_comunicacao": "Altíssima",
        "status_operacional": "Ativo",
        "conexoes": [("Habitação", 50), ("Comunicação", 30), ("Armazenamento de energia", 150), ("Laboratório científico", 120)]
    },
    "Armazenamento de energia": {
        "consumo_energetico_kwh": 15, 
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "50.000 kWh (BESS e Hidrogênio Verde)",
        "necessidade_comunicacao": "Média",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 150), ("Produção de oxigênio", 200), ("Agricultura", 300)]
    },
    "Agricultura": {
        "consumo_energetico_kwh": 250, 
        "prioridade_operacional": 3,
        "capacidade_armazenamento": "Estufas / 5000L Água / Biomassa",
        "necessidade_comunicacao": "Baixa",
        "status_operacional": "Ativo",
        "conexoes": [("Habitação", 100), ("Armazenamento de energia", 300), ("Laboratório científico", 60)]
    },
    "Laboratório científico": {
        "consumo_energetico_kwh": 180,
        "prioridade_operacional": 4,
        "capacidade_armazenamento": "Amostras geológicas / Câmaras criogênicas",
        "necessidade_comunicacao": "Alta",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 120), ("Agricultura", 60), ("Suporte médico", 90)]
    },
    "Comunicação": {
        "consumo_energetico_kwh": 95,
        "prioridade_operacional": 2,
        "capacidade_armazenamento": "Buffers de transmissão (Terabytes)",
        "necessidade_comunicacao": "Altíssima",
        "status_operacional": "Ativo",
        "conexoes": [("Centro de controle", 30)]
    },
    "Suporte médico": {
        "consumo_energetico_kwh": 60, 
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "Suprimentos médicos / Oxigênio de emergência",
        "necessidade_comunicacao": "Média",
        "status_operacional": "Ativo",
        "conexoes": [("Habitação", 20), ("Laboratório científico", 90)]
    },
    "Produção de oxigênio": {
        "consumo_energetico_kwh": 300, 
        "prioridade_operacional": 1,
        "capacidade_armazenamento": "Tanques de O2 pressurizado (10.000 m³)",
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





def calcular_perda_energetica():

    print("\n" + "=" * 60)
    print("MODELAGEM MATEMÁTICA - PERDA ENERGÉTICA")
    print("=" * 60)

    print("\nFórmula utilizada:")
    print("E(d) = E₀ × e^(-0,002 × d)\n")

    print("Onde:")
    print("E(d) = Energia recebida")
    print("E₀   = Energia enviada")
    print("d    = Distância entre os módulos (m)")
    print("0,002 = Coeficiente de perda energética\n")

    energia_inicial = float(input("Energia enviada (kWh): "))
    distancia = float(input("Distância da transmissão (m): "))

    energia_recebida = energia_inicial * math.exp(-0.002 * distancia)

    perda = energia_inicial - energia_recebida

    print("\n" + "=" * 60)
    print("RESULTADO DA SIMULAÇÃO")
    print("=" * 60)

    print(f"Energia enviada: {energia_inicial:.2f} kWh")
    print(f"Distância: {distancia:.2f} m")
    print(f"Energia recebida: {energia_recebida:.2f} kWh")
    print(f"Perda energética: {perda:.2f} kWh")

    input("\nPressione ENTER para continuar...")

#print(calcular_perda_energetica())

def ranking_criticidade():

    ranking = []

    for nome, dados in colonia_aurora_siger.items():

        consumo = dados["consumo_energetico_kwh"]
        prioridade = dados["prioridade_operacional"]

        indice = consumo / prioridade

        ranking.append((nome, indice))

    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\n" + "=" * 60)
    print("OTIMIZAÇÃO - RANKING DE CRITICIDADE")
    print("=" * 60)

    print("\nFórmula utilizada:")
    print("Índice de Criticidade = Consumo Energético ÷ Prioridade Operacional")

    print("\nQuanto MAIOR o índice, mais crítico é o módulo.\n")

    for posicao, (nome, indice) in enumerate(ranking, start=1):

        print(f"{posicao}º - {nome}")
        print(f"Índice de Criticidade: {indice:.2f}\n")

    input("Pressione ENTER para continuar...")    

#print(ranking_criticidade())

def estatisticas_colonia():

    total_consumo = 0

    maior_consumo = 0
    modulo_maior_consumo = ""

    for nome, dados in colonia_aurora_siger.items():

        consumo = dados["consumo_energetico_kwh"]

        total_consumo += consumo

        if consumo > maior_consumo:
            maior_consumo = consumo
            modulo_maior_consumo = nome

    media_consumo = total_consumo / len(colonia_aurora_siger)

    print("\n" + "=" * 60)
    print("ESTATÍSTICAS DA COLÔNIA")
    print("=" * 60)

    print(f"\nConsumo total da colônia: {total_consumo} kWh")
    print(f"Consumo médio dos módulos: {media_consumo:.2f} kWh")
    print(f"Módulo com maior consumo: {modulo_maior_consumo}")
    print(f"Maior consumo registrado: {maior_consumo} kWh")

    input("\nPressione ENTER para continuar...")

#print(estatisticas_colonia())