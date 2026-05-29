# decision_engine.py
# Regras de decisão automáticas para o sistema da colônia.
# Combina condições e prioriza sistemas essenciais.

def avaliar_decisao(colonia):
    """
    Avalia o estado da colônia e retorna uma decisão / recomendação de ação.

    Regras (por prioridade):
      1. Energia crítica (< 20 % do consumo disponível) → EMERGÊNCIA
      2. Energia baixa (< 50 kWh gerado + reserva) e consumo alto (> 70) → modo economia
      3. Energia baixa (< 50 kWh) → reduzir consumo
      4. Tempestade → preparar reservas
      5. Energia suficiente → operação normal

    Retorna:
        dict com chaves:
            "status"    : str  – nível geral ("EMERGÊNCIA", "ALERTA", "AVISO", "NORMAL")
            "mensagem"  : str  – descrição clara da situação
            "acao"      : str  – ação recomendada
            "desligar"  : list – sistemas não essenciais a desligar (se necessário)
    """
    en = colonia["sistemas"]["energetico"]
    co = colonia["sistemas"]["consumo"]
    clima = colonia["clima"]

    energia_disponivel = en["total_gerado"] + en["reserva"]
    consumo = co["total"]

    # --- Regra 1: situação crítica ---
    if energia_disponivel < consumo * 0.2:
        sistemas_desligar = list(co["nao_essenciais"].keys())
        return {
            "status": "EMERGÊNCIA",
            "mensagem": (
                f"Energia disponível ({energia_disponivel} kWh) é crítica "
                f"— menos de 20 % do consumo ({consumo} kWh)."
            ),
            "acao": "Desligar todos os sistemas não essenciais imediatamente.",
            "desligar": sistemas_desligar,
        }

    # --- Regra 2: energia baixa + consumo alto → modo economia ---
    if energia_disponivel < 50 and consumo > 70:
        sistemas_desligar = list(co["nao_essenciais"].keys())
        return {
            "status": "ALERTA",
            "mensagem": (
                f"Energia baixa ({energia_disponivel} kWh) e consumo alto "
                f"({consumo} kWh). Ativar modo economia."
            ),
            "acao": "Ativar modo economia: desligar sistemas não essenciais.",
            "desligar": sistemas_desligar,
        }

    # --- Regra 3: energia baixa ---
    if energia_disponivel < 50:
        return {
            "status": "ALERTA",
            "mensagem": f"Energia disponível baixa: {energia_disponivel} kWh.",
            "acao": "Reduzir consumo nos sistemas não essenciais.",
            "desligar": [],
        }

    # --- Regra 4: clima adverso ---
    if clima == "tempestade":
        return {
            "status": "AVISO",
            "mensagem": "Tempestade detectada — geração eólica instável.",
            "acao": "Carregar reservas ao máximo antes da tempestade.",
            "desligar": [],
        }

    # --- Regra 5: operação normal ---
    return {
        "status": "NORMAL",
        "mensagem": (
            f"Operação normal. Energia disponível: {energia_disponivel} kWh, "
            f"consumo: {consumo} kWh."
        ),
        "acao": "Manter operação atual.",
        "desligar": [],
    }


def exibir_decisao(resultado):
    """Exibe a decisão de forma clara e formatada."""
    print("\n>>> DECISÃO DO SISTEMA <<<")
    print(f"  Status  : {resultado['status']}")
    print(f"  Situação: {resultado['mensagem']}")
    print(f"  Ação    : {resultado['acao']}")
    if resultado["desligar"]:
        print(f"  Desligar: {', '.join(resultado['desligar'])}")
