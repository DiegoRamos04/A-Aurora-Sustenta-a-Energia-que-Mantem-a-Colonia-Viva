import sys
import os
import time

# Configuração de diretório para importar o system.py da pasta src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from system import *

def limpar_tela():
    # Limpa o terminal no Windows ('nt') ou Linux/Mac ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    limpar_tela()
    print("\n" + "═" * 65)
    print(" 🚀 SIGIC - SISTEMA INTELIGENTE DE GERENCIAMENTO DA COLÔNIA")
    print("    BASE: AURORA SIGER | STATUS: OPERACIONAL")
    print("═" * 65)
    print("\n ⚡ [ MENU PRINCIPAL DE GOVERNANÇA ] ⚡\n")

while True:
    exibir_cabecalho()
    
    print("  [ 1 ] 📊 Consultar Módulos da Infraestrutura")
    print("  [ 2 ] 🧮 Simular Modelagem Matemática (Perda Energética)")
    print("  [ 3 ] 📍 Otimizar Rota de Transmissão (Algoritmo de Dijkstra)")
    print("  [ 4 ] 📡 Mapear Rede por Níveis (Algoritmo BFS)")
    print("  [ 5 ] 🛠️  Executar Inspeção Profunda (Algoritmo DFS)")
    print("  [ 0 ] 🛑 Desconectar e Encerrar Sistema")
    
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
            print(" 🛑 Desconectando do terminal central da Colônia Aurora Siger...")
            print("    Salvando logs de rede e fechando conexões...")
            time.sleep(1.5) # Pausa dramática para efeito de sistema encerrando
            print("    Sistema encerrado com segurança. Bom descanso, engenheiro!")
            print("═" * 65 + "\n")
            break
            
        case _:
            print("\n ⚠️  Comando inválido. Código não reconhecido pela rede.")
            time.sleep(2) # Pausa para o usuário ler o erro antes de limpar a tela
