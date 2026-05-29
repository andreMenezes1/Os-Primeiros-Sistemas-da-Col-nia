#!/usr/bin/env python3
# main.py
# Sistema Integrado da Colônia — ponto de entrada principal.
# Execute com: python main.py

from data_model      import criar_colonia, exibir_resumo
from decision_engine import avaliar_decisao, exibir_decisao
from regression      import exibir_previsao
from energy_analysis import analisar_energia, exibir_analise


def executar_cenario(titulo, energia_solar, energia_eolica, reserva,
                     consumo, clima, vento_novo):
    """
    Executa e exibe o resultado completo de um cenário da colônia.

    Parâmetros:
        titulo        (str)  : nome do cenário para exibição
        energia_solar (float): energia gerada pelo sistema solar (kWh)
        energia_eolica(float): energia gerada pelo sistema eólico (kWh)
        reserva       (float): energia armazenada em baterias (kWh)
        consumo       (float): consumo total atual (kWh)
        clima         (str)  : condição climática
        vento_novo    (float): velocidade do vento para previsão (m/s)
    """
    print(f"\n{'#' * 50}")
    print(f"  CENÁRIO: {titulo}")
    print(f"{'#' * 50}")

    # 1. Criar e exibir estado da colônia
    colonia = criar_colonia(
        energia_solar=energia_solar,
        energia_eolica=energia_eolica,
        reserva=reserva,
        consumo=consumo,
        clima=clima,
    )
    exibir_resumo(colonia)

    # 2. Decisão automática
    decisao = avaliar_decisao(colonia)
    exibir_decisao(decisao)

    # 3. Previsão de energia eólica por regressão linear
    exibir_previsao(colonia, vento_novo)

    # 4. Análise de geração vs consumo
    analise = analisar_energia(colonia)
    exibir_analise(analise)


def main():
    print("\n" + "=" * 50)
    print("  SISTEMA INTEGRADO DA COLÔNIA")
    print("  Organização · Decisão · Previsão · Análise")
    print("=" * 50)

    # ----------------------------------------------------------
    # Cenário 1 — Situação crítica: energia baixa, consumo alto
    # Entrada : energia_solar=20, energia_eolica=10, reserva=5,
    #           consumo=70, clima="normal"
    # Saída esperada: ALERTA — ativar modo economia
    # ----------------------------------------------------------
    executar_cenario(
        titulo="Energia Baixa + Consumo Alto (Modo Economia)",
        energia_solar=20,
        energia_eolica=10,
        reserva=5,
        consumo=70,
        clima="normal",
        vento_novo=11,
    )

    # ----------------------------------------------------------
    # Cenário 2 — Geração maior que consumo: excedente disponível
    # Entrada : energia_solar=60, energia_eolica=20, reserva=15,
    #           consumo=30, clima="normal"
    # Saída esperada: SUGESTÃO — armazenar energia excedente
    # ----------------------------------------------------------
    executar_cenario(
        titulo="Geração Alta + Consumo Baixo (Armazenar Excedente)",
        energia_solar=60,
        energia_eolica=20,
        reserva=15,
        consumo=30,
        clima="normal",
        vento_novo=14,
    )

    # ----------------------------------------------------------
    # Cenário 3 — Tempestade: geração instável
    # Entrada : energia_solar=30, energia_eolica=5, reserva=40,
    #           consumo=50, clima="tempestade"
    # Saída esperada: AVISO — preparar reservas
    # ----------------------------------------------------------
    executar_cenario(
        titulo="Tempestade (Geração Instável)",
        energia_solar=30,
        energia_eolica=5,
        reserva=40,
        consumo=50,
        clima="tempestade",
        vento_novo=6,
    )

    print("\n" + "=" * 50)
    print("  Simulação concluída.")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
