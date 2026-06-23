# Estrutura de dados principal da Colônia Aurora Siger
# Cada chave é um módulo, contendo seus atributos técnicos e as conexões (arestas) com pesos (distâncias em metros)
# Nível de prioridade vai de 1 a 5, sendo o nível 1 o mais crítico

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
