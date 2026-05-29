# data_model.py
# Organização dos dados da colônia em estruturas eficientes (listas e dicts)
# e representação hierárquica dos sistemas.

def criar_colonia(energia_solar=0, energia_eolica=0, reserva=0,
                  consumo=0, clima="normal"):
    """
    Cria e retorna o estado atual da colônia como um dicionário.

    Parâmetros:
        energia_solar  (float): energia gerada pelo sistema solar (kWh)
        energia_eolica (float): energia gerada pelo sistema eólico (kWh)
        reserva        (float): energia armazenada em baterias (kWh)
        consumo        (float): consumo total atual da colônia (kWh)
        clima          (str):   condição climática ("normal", "tempestade", "seco")

    Retorna:
        dict: estado completo da colônia
    """
    colonia = {
        "clima": clima,
        "sistemas": {
            "energetico": {
                "solar":   energia_solar,
                "eolico":  energia_eolica,
                "reserva": reserva,
                "total_gerado": energia_solar + energia_eolica,
            },
            "consumo": {
                "total": consumo,
                "essenciais": {
                    "suporte_vida": True,
                    "iluminacao_emergencia": True,
                    "comunicacoes": True,
                },
                "nao_essenciais": {
                    "entretenimento": True,
                    "aquecimento_extra": True,
                    "laboratorio_secundario": True,
                },
            },
        },
        "historico_vento":   [8, 10, 12, 9, 11],
        "historico_energia":  [20, 25, 30, 22, 27],
    }
    return colonia


def exibir_resumo(colonia):
    """Exibe um resumo formatado do estado da colônia."""
    s = colonia["sistemas"]
    en = s["energetico"]
    co = s["consumo"]

    print("=" * 45)
    print("        RESUMO DA COLÔNIA")
    print("=" * 45)
    print(f"  Clima            : {colonia['clima']}")
    print(f"  Energia Solar    : {en['solar']} kWh")
    print(f"  Energia Eólica   : {en['eolico']} kWh")
    print(f"  Total Gerado     : {en['total_gerado']} kWh")
    print(f"  Reserva          : {en['reserva']} kWh")
    print(f"  Consumo Atual    : {co['total']} kWh")
    print("=" * 45)
