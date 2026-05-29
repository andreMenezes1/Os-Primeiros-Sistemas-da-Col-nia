# Relatório — Sistema Integrado da Colônia

**Disciplina:** Estruturas de Dados e Programação  
**Repositório:** https://github.com/andreMenezes1/Os-Primeiros-Sistemas-da-Col-nia  

---

## 1. Como os Dados Foram Organizados

Os dados da colônia foram estruturados em **dicionários aninhados** (tabelas chave-valor), formando uma hierarquia que espelha os sistemas reais da colônia:

```
colonia
├── clima
└── sistemas
    ├── energetico
    │   ├── solar
    │   ├── eolico
    │   ├── reserva
    │   └── total_gerado
    └── consumo
        ├── total
        ├── essenciais
        │   ├── suporte_vida
        │   ├── iluminacao_emergencia
        │   └── comunicacoes
        └── nao_essenciais
            ├── entretenimento
            ├── aquecimento_extra
            └── laboratorio_secundario
```

Além do estado atual, a colônia mantém **listas históricas** de velocidade do vento e energia gerada, usadas para a previsão por regressão.

Esta abordagem permite acesso direto a qualquer subsistema (`colonia["sistemas"]["energetico"]["solar"]`) e facilita a adição de novos subsistemas sem alterar a estrutura existente.

---

## 2. Regras de Decisão Utilizadas

O módulo `decision_engine.py` avalia o estado da colônia e gera uma ação objetiva com base em quatro regras, aplicadas em ordem de prioridade:

| Prioridade | Condição | Status | Ação |
|-----------|----------|--------|------|
| 1ª | Energia disponível < 20 % do consumo | EMERGÊNCIA | Desligar todos os sistemas não essenciais |
| 2ª | Energia < 50 kWh **e** consumo > 70 kWh | ALERTA | Ativar modo economia |
| 3ª | Energia disponível < 50 kWh | ALERTA | Reduzir consumo |
| 4ª | Clima = "tempestade" | AVISO | Carregar reservas |
| 5ª | Demais casos | NORMAL | Manter operação |

Os sistemas **essenciais** (suporte à vida, iluminação de emergência, comunicações) nunca são desligados. Somente os **não essenciais** (entretenimento, aquecimento extra, laboratório secundário) entram na lista de corte.

---

## 3. Modelo de Previsão Aplicado

Foi implementada uma **regressão linear simples** (`regression.py`) usando apenas operações matemáticas básicas — sem nenhuma biblioteca externa.

### Método: Mínimos Quadrados

Dados históricos:

| Vento (m/s) | Energia (kWh) |
|-------------|---------------|
| 8           | 20            |
| 10          | 25            |
| 12          | 30            |
| 9           | 22            |
| 11          | 27            |

A reta ajustada segue a fórmula `y = a·x + b`, onde:

- **a** (coeficiente angular) = `(n·Σxy − Σx·Σy) / (n·Σx² − (Σx)²)`
- **b** (intercepto) = `(Σy − a·Σx) / n`

**Resultado:** `energia = 2,50 × vento − 0,20`

**Exemplo de uso:**  
Entrada: `vento = 11 m/s`  
Saída: `energia ≈ 27,30 kWh`

---

## 4. Como o Sistema Ajuda a Melhorar o Uso de Energia

O módulo `energy_analysis.py` classifica a relação entre geração e consumo em cinco situações:

| Situação | Critério | Ação Recomendada |
|----------|----------|-----------------|
| ALERTA grave | Consumo > 130 % da geração | Reduzir consumo + usar reserva |
| ALERTA | Consumo > geração | Usar reserva |
| EQUILÍBRIO | Diferença < 5 % | Monitorar |
| NORMAL | Excedente ≤ 30 % | Armazenar parte |
| EXCEDENTE | Excedente > 30 % | Carregar baterias ao máximo |

Ao identificar o excedente, o sistema evita o **desperdício** de energia. Ao detectar déficit, aciona o **protocolo de economia**, garantindo que os sistemas essenciais continuem operando.

---

## 5. Exemplos de Entrada e Saída

### Exemplo A — Modo Economia

```
Entrada : energia_solar=20, energia_eolica=10, reserva=5, consumo=70
Saída   : ALERTA — Reduzir consumo nos sistemas não essenciais.
          ALERTA — Consumo (70 kWh) muito maior que geração (30 kWh). Déficit: 40 kWh.
```

### Exemplo B — Armazenar Excedente

```
Entrada : energia_solar=60, energia_eolica=20, reserva=15, consumo=30
Saída   : NORMAL — Manter operação atual.
          EXCEDENTE — SUGESTÃO: armazenar energia excedente (50 kWh).
```

### Exemplo C — Previsão Eólica

```
Entrada : vento = 11 m/s
Saída   : energia ≈ 27,30 kWh
```

---

## 6. Conclusão

O sistema integrado demonstra como estruturas de dados simples (dicionários e listas), lógica de decisão por regras e um modelo matemático básico (regressão linear) podem ser combinados para criar uma solução computacional capaz de:

- **Organizar** os dados de uma colônia de forma hierárquica e acessível;
- **Reagir** a situações de risco com ações objetivas e priorizadas;
- **Prever** comportamentos futuros com base em dados históricos;
- **Otimizar** o uso de energia, evitando tanto o desperdício quanto o déficit.

O código é executado com `python main.py` e não requer nenhuma biblioteca externa.
