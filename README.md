# 🪐 Sistema Integrado da Colônia

Sistema em Python que simula o funcionamento inteligente de uma colônia espacial, integrando:

- **Organização de dados** – estruturas de lista e dicionário, com hierarquia de subsistemas
- **Decisão automática** – regras de lógica que transformam dados em ações claras
- **Previsão por regressão linear** – estimativa de energia eólica com base no histórico de vento
- **Análise de energia** – comparação entre geração, consumo e reserva

---

## 📁 Estrutura do Projeto

```
.
├── main.py             # Ponto de entrada — integra todos os módulos
├── data_model.py       # Organização dos dados da colônia (listas, dicts, hierarquia)
├── decision_engine.py  # Regras de decisão automáticas
├── regression.py       # Regressão linear simples (sem bibliotecas externas)
├── energy_analysis.py  # Análise de geração × consumo × reserva
└── relatorio.md        # Base do relatório para exportação em PDF
```

---

## ▶️ Como Executar

> Requisito: Python 3.6 ou superior (sem dependências externas).

```bash
python main.py
```

---

## 💡 Exemplos de Entrada e Saída

### Cenário 1 — Energia baixa + consumo alto

**Entrada:**
```
energia_solar=20, energia_eolica=10, reserva=5, consumo=70, clima="normal"
```

**Saída:**
```
>>> DECISÃO DO SISTEMA <<<
  Status  : ALERTA
  Situação: Energia disponível baixa: 35 kWh.
  Ação    : Reduzir consumo nos sistemas não essenciais.

>>> ANÁLISE DE ENERGIA <<<
  Status  : ALERTA
  Situação: ALERTA: consumo (70 kWh) muito maior que a geração (30 kWh). Déficit de 40.0 kWh.
  Ação    : Reduzir consumo imediatamente e utilizar reserva.
```

---

### Cenário 2 — Geração alta + consumo baixo

**Entrada:**
```
energia_solar=60, energia_eolica=20, reserva=15, consumo=30, clima="normal"
```

**Saída:**
```
>>> DECISÃO DO SISTEMA <<<
  Status  : NORMAL
  Situação: Operação normal. Energia disponível: 95 kWh, consumo: 30 kWh.
  Ação    : Manter operação atual.

>>> ANÁLISE DE ENERGIA <<<
  Status  : EXCEDENTE
  Situação: SUGESTÃO: armazenar energia excedente. Geração: 80 kWh | Consumo: 30 kWh | Excedente: 50.0 kWh.
  Ação    : Carregar baterias ao máximo com o excedente disponível.
```

---

### Previsão por Regressão Linear

**Dados históricos:**
```python
vento  = [8, 10, 12, 9, 11]   # m/s
energia = [20, 25, 30, 22, 27] # kWh
```

**Entrada:** `vento = 11 m/s`

**Saída:**
```
>>> PREVISÃO DE ENERGIA EÓLICA (Regressão Linear) <<<
  Equação ajustada: energia = 2.5000 × vento + -0.2000
  Entrada : vento = 11 m/s
  Previsão: energia ≈ 27.30 kWh
```

---

## 🧩 Módulos

| Arquivo              | Responsabilidade                                           |
|---------------------|------------------------------------------------------------|
| `data_model.py`     | Cria a estrutura hierárquica de dados da colônia           |
| `decision_engine.py`| Aplica regras de lógica e retorna ação recomendada         |
| `regression.py`     | Calcula regressão linear e prevê geração eólica futura     |
| `energy_analysis.py`| Compara geração × consumo e classifica a situação          |
| `main.py`           | Orquestra os cenários e exibe todos os resultados          |

---


