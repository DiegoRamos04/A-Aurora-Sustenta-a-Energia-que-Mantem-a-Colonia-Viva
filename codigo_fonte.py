import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from system import *

while True:

    print("\n" + "=" * 60)
    print("SIGIC - SISTEMA INTELIGENTE DE GERENCIAMENTO")
    print("=" * 60)

    print("1 - Consultar módulos")
    print("2 - Modelagem matemática")
    print("3 - Otimização (Dijkstra)")
    print("4 - Exploração da rede (BFS)")
    print("5 - Exploração da rede (DFS)")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:

        case "1":
            consultar_modulos()

        case "2":
            executar_modelagem()

        case "3":
            executar_dijkstra()

        case "4":
            executar_bfs()

        case "5":
            executar_dfs()

        case "0":
            print("\nEncerrando sistema...")
            break

        case _:
            print("\nOpção inválida.")