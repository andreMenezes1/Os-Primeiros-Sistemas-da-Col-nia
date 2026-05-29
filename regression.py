# regression.py
# Regressão linear simples — sem bibliotecas externas.
# Usada para prever geração de energia eólica com base na velocidade do vento.

def calcular_regressao_linear(x, y):
    """
    Calcula os coeficientes (a, b) da reta y = a*x + b
    usando mínimos quadrados.

    Parâmetros:
        x (list[float]): variável independente (ex.: velocidade do vento)
        y (list[float]): variável dependente   (ex.: energia gerada)

    Retorna:
        tuple (a, b):
            a – coeficiente angular (inclinação da reta)
            b – intercepto (valor de y quando x = 0)
    """
    n = len(x)
    if n == 0:
        raise ValueError("As listas de dados não podem estar vazias.")
    if n != len(y):
        raise ValueError("As listas x e y devem ter o mesmo tamanho.")

    soma_x  = sum(x)
    soma_y  = sum(y)
    soma_xy = sum(xi * yi for xi, yi in zip(x, y))
    soma_x2 = sum(xi ** 2 for xi in x)

    denominador = n * soma_x2 - soma_x ** 2
    if denominador == 0:
        raise ValueError("Não é possível calcular a regressão: todos os valores de x são iguais.")

    a = (n * soma_xy - soma_x * soma_y) / denominador
    b = (soma_y - a * soma_x) / n
    return a, b


def prever(a, b, x_novo):
    """
    Usa os coeficientes calculados para prever y dado um novo valor de x.

    Parâmetros:
        a      (float): coeficiente angular
        b      (float): intercepto
        x_novo (float): novo valor da variável independente

    Retorna:
        float: valor previsto de y
    """
    return a * x_novo + b


def exibir_previsao(colonia, vento_novo):
    """
    Usa os dados históricos da colônia para ajustar a regressão e
    exibir a previsão de energia eólica para uma velocidade de vento informada.

    Parâmetros:
        colonia   (dict) : estado da colônia (deve conter historico_vento e historico_energia)
        vento_novo(float): velocidade de vento para a qual se deseja prever a geração
    """
    historico_vento  = colonia["historico_vento"]
    historico_energia = colonia["historico_energia"]

    a, b = calcular_regressao_linear(historico_vento, historico_energia)
    predicao = prever(a, b, vento_novo)

    print("\n>>> PREVISÃO DE ENERGIA EÓLICA (Regressão Linear) <<<")
    print(f"  Dados históricos — vento : {historico_vento}")
    print(f"  Dados históricos — energia: {historico_energia}")
    print(f"  Equação ajustada: energia = {a:.4f} × vento + {b:.4f}")
    print(f"  Entrada : vento = {vento_novo} m/s")
    print(f"  Previsão: energia ≈ {predicao:.2f} kWh")
