
def is_valid_signal(R_t, L_t, S_t, T_t, confidence, volatility, threshold=0.002):
    """
    Filtro antifake-sinal: evita sinais frágeis ou incoerentes.
    """

    # 1. Confiança mínima
    if confidence < 0.6:
        return False

    # 2. Retorno esperado fraco
    if abs(R_t) < threshold:
        return False

    # 3. Divergência entre sentimento e tendência
    if S_t * T_t < 0:
        return False

    # 4. Volatilidade alta com retorno fraco
    risk_factor = L_t + volatility
    if abs(R_t) < risk_factor * 0.8:
        return False

    return True
