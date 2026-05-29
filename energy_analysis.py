# energy_analysis.py
# Análise do uso de energia: compara geração, consumo e reserva,
# gerando recomendações claras para a colônia.

def analisar_energia(colonia):
    """
    Compara a geração total, consumo e reserva de energia da colônia.

    Casos avaliados:
      - Consumo muito acima da geração (> 30 % a mais) → ALERTA grave
      - Consumo maior que geração                       → ALERTA
      - Consumo igual à geração                         → EQUILÍBRIO
      - Geração maior que consumo em até 30 %           → NORMAL
      - Geração muito maior que consumo (> 30 % extra)  → SUGESTÃO: armazenar excedente

    Parâmetros:
        colonia (dict): estado da colônia

    Retorna:
        dict com chaves:
            "status"   : str  – classificação ("ALERTA", "EQUILÍBRIO", "NORMAL", "EXCEDENTE")
            "mensagem" : str  – descrição da situação
            "acao"     : str  – ação recomendada
    """
    en = colonia["sistemas"]["energetico"]
    co = colonia["sistemas"]["consumo"]

    geracao = en["total_gerado"]
    reserva = en["reserva"]
    consumo = co["total"]

    excedente = geracao - consumo

    # --- Caso 1: consumo muito acima da geração (> 30 % além) ---
    if consumo > geracao * 1.30:
        return {
            "status": "ALERTA",
            "mensagem": (
                f"ALERTA: consumo ({consumo} kWh) muito maior que a geração "
                f"({geracao} kWh). Déficit de {abs(excedente):.1f} kWh."
            ),
            "acao": "Reduzir consumo imediatamente e utilizar reserva.",
        }

    # --- Caso 2: consumo maior que geração ---
    if consumo > geracao:
        return {
            "status": "ALERTA",
            "mensagem": (
                f"ALERTA: consumo maior que geração. "
                f"Geração: {geracao} kWh | Consumo: {consumo} kWh | "
                f"Déficit: {abs(excedente):.1f} kWh."
            ),
            "acao": "Utilizar reserva e reduzir consumo não essencial.",
        }

    # --- Caso 3: equilíbrio (consumo ≈ geração, diferença < 5 %) ---
    if abs(excedente) / max(geracao, 1) < 0.05:
        return {
            "status": "EQUILÍBRIO",
            "mensagem": (
                f"Equilíbrio energético. "
                f"Geração: {geracao} kWh | Consumo: {consumo} kWh."
            ),
            "acao": "Manter operação atual. Monitorar reservas.",
        }

    # --- Caso 4: geração moderadamente maior que consumo ---
    if excedente <= geracao * 0.30:
        return {
            "status": "NORMAL",
            "mensagem": (
                f"Geração levemente superior ao consumo. "
                f"Excedente: {excedente:.1f} kWh | Reserva atual: {reserva} kWh."
            ),
            "acao": "Armazenar parte do excedente nas baterias.",
        }

    # --- Caso 5: geração muito maior que consumo ---
    return {
        "status": "EXCEDENTE",
        "mensagem": (
            f"SUGESTÃO: armazenar energia excedente. "
            f"Geração: {geracao} kWh | Consumo: {consumo} kWh | "
            f"Excedente: {excedente:.1f} kWh."
        ),
        "acao": "Carregar baterias ao máximo com o excedente disponível.",
    }


def exibir_analise(resultado):
    """Exibe a análise de energia de forma clara e formatada."""
    print("\n>>> ANÁLISE DE ENERGIA <<<")
    print(f"  Status  : {resultado['status']}")
    print(f"  Situação: {resultado['mensagem']}")
    print(f"  Ação    : {resultado['acao']}")
