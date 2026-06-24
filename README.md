
---

# SIGIC – Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia

## 1. Visão Geral do Projeto

O SIGIC (Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia) é um sistema desenvolvido em Python para representar e analisar a infraestrutura de uma colônia baseada em módulos interconectados.

O objetivo principal é modelar a rede da colônia como um grafo ponderado, permitindo a análise de conexões, consumo energético, criticidade dos módulos e otimização de rotas utilizando algoritmos de teoria dos grafos.

---

## 2. Organização da Infraestrutura da Colônia

A colônia é composta por diferentes módulos operacionais:

### Habitação
* Consumo Energético: 120 kWh

* Prioridade Operacional: 2 

* Capacidade de Armazenamento: 500 kWh / 1000L Água

* Necessidade de Comunicação: Média

* Status: Ativo

* Conexões: Centro de controle (50m), Suporte médico (20m), Produção de oxigênio (80m), Agricultura (100m)

### Centro de Controle
* Consumo Energético: 85 kWh

* Prioridade Operacional: 1 (Crítica)

* Capacidade de Armazenamento: Servidores / Nobreaks

* Necessidade de Comunicação: Altíssima

* Status: Ativo

* Conexões: Habitação (50m), Comunicação (30m), Armazenamento de energia (150m), Laboratório científico (120m)

### Armazenamento de Energia
* Consumo Energético: 15 kWh

* Prioridade Operacional: 1 (Crítica)

* Capacidade de Armazenamento: 50.000 kWh

* Necessidade de Comunicação: Média

* Status: Ativo

* Conexões: Centro de controle (150m), Produção de oxigênio (200m), Agricultura (300m)
  
### Agricultura
* Consumo Energético: 250 kWh

* Prioridade Operacional: 3

* Capacidade de Armazenamento: Estufas / Água

* Necessidade de Comunicação: Baixa

* Status: Ativo

* Conexões: Habitação (100m), Armazenamento de energia (300m), Laboratório científico (60m)
  
### Laboratório Científico
* Consumo Energético: 180 kWh

* Prioridade Operacional: 4

* Capacidade de Armazenamento: Amostras / Câmaras criogênicas

* Necessidade de Comunicação: Alta

* Status: Ativo

* Conexões: Centro de controle (120m), Agricultura (60m), Suporte médico (90m)

### Comunicação
* Consumo Energético: 95 kWh

* Prioridade Operacional: 2

* Capacidade de Armazenamento: Terabytes

* Necessidade de Comunicação: Altíssima

* Status: Ativo

* Conexões: Centro de controle (30m)
  
### Suporte Médico
* Consumo Energético: 60 kWh

* Prioridade Operacional: 1 (Crítica)

* Capacidade de Armazenamento: Suprimentos médicos

* Necessidade de Comunicação: Média

* Status: Ativo

* Conexões: Habitação (20m), Laboratório científico (90m)
  
### Produção de Oxigênio
* Consumo Energético: 300 kWh

* Prioridade Operacional: 1 (Crítica)

* Capacidade de Armazenamento: Tanques O2

* Necessidade de Comunicação: Baixa

* Status: Ativo

* Conexões: Habitação (80m), Armazenamento de energia (200m)

---

## 3. Estruturas de Dados Utilizadas

### 3.1 Dicionários

A estrutura principal da colônia é representada por um dicionário Python, onde cada chave representa um módulo e seus atributos.

---

### 3.2 Listas

Utilizadas para armazenar:

* conexões entre módulos
* lista de módulos da colônia

---

### 3.3 Tuplas

As conexões são representadas por tuplas no formato:

(módulo_destino, distância)

Exemplo:
("Centro de controle", 50)

---

### 3.4 Matriz de Adjacência

A rede também é representada por uma matriz de adjacência, onde:

* Linhas representam módulos de origem
* Colunas representam módulos de destino
* Valores representam a distância entre os módulos

Isso permite uma segunda forma de análise da rede.

---

## 4. Representação em Grafo

A infraestrutura da colônia é modelada como um grafo ponderado:

G = (V, E, W)

Onde:

* V = conjunto de módulos (vértices)
* E = conexões entre módulos (arestas)
* W = peso das conexões (distância em metros)

---

## 5. Algoritmos Implementados

### 5.1 BFS (Busca em Largura)

Utilizado para explorar todos os módulos da colônia de forma nivelada, analisando conectividade geral da rede.

Aplicações:

* análise de alcance da rede
* verificação de conectividade

---

### 5.2 DFS (Busca em Profundidade)

Utilizado para explorar caminhos profundos da rede, percorrendo conexões de forma recursiva.

Aplicações:

* análise estrutural da rede
* exploração de caminhos alternativos

---

### 5.3 Dijkstra (Otimização de Rotas)

Utilizado para encontrar o menor caminho entre módulos da colônia.

Aplicações:

* otimização de transmissão de energia
* redução de custo energético e de comunicação

---

## 6. Modelagem Matemática

Foi implementado um modelo matemático para simular a perda de energia na transmissão entre módulos.

### Fórmula utilizada:

E(d) = E₀ × e^(-0.002 × d)

Onde:

* E(d) = energia recebida
* E₀ = energia inicial
* d = distância entre os módulos
* 0.002 = coeficiente de perda energética

### Análise:

O modelo representa a perda exponencial de energia ao longo da distância, simulando eficiência real de transmissão em redes energéticas.

---

## 7. Otimização da Colônia

A otimização do sistema é realizada através de:

* cálculo de menor caminho (Dijkstra)
* análise de criticidade dos módulos
* avaliação de consumo energético
* exploração da rede (BFS e DFS)

Isso permite identificar rotas mais eficientes e módulos mais críticos para a operação da colônia.

---

## 8. Funcionalidades do Sistema

O sistema possui um menu interativo com as seguintes funções:

* Consultar módulos da colônia
* Executar modelagem matemática
* Calcular menor caminho (Dijkstra)
* Executar BFS (exploração da rede)
* Executar DFS (exploração profunda)

---

## 9. Arquitetura do Projeto

```

C:.
│   .gitignore
│   codigo_fonte.py
│   link_video.txt
│   README.md
│   
├───arquivos_auxiliares
│       dados_colonia.json
│       
├───docs
│       (Colocar arquivos pdf dentro desse docs)
│       
└───src
    │   funcoes_grafo.py
    │   system.py
    │   
    └───__pycache__
            system.cpython-314.pyc

```

---

## 10. Conclusão

O SIGIC integra conceitos fundamentais de estruturas de dados, grafos e otimização computacional para simular o gerenciamento inteligente de uma infraestrutura crítica.

O sistema permite análise da rede, otimização de caminhos e modelagem matemática aplicada, demonstrando a aplicação prática dos conceitos estudados na disciplina.

---
