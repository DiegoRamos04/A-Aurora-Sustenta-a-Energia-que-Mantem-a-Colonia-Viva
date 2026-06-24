import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from system import *


while True:

    print("\n" + "=" * 60)
    print("AURORA - SISTEMA INTELIGENTE DE GERENCIAMENTO")
    print("=" * 60)

    print("1 - Consultar módulos")
    print("2 - Modelagem matemática")
    print("3 - Ranking de criticidade")
    print("4 - Estatísticas da colônia")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:

        case "1":
            consultar_modulos()

        case "2":
            calcular_perda_energetica()

        case "3":
            ranking_criticidade()

        case "4":
            estatisticas_colonia()

        case "0":
            print("\nEncerrando sistema...")
            break

        case _:
            print("\nOpção inválida.")