def is_valid_signal(R_t, L_t, S_t, T_t, confidence, volatility, threshold=0.002):
    """
    Filtro antifake-sinal: evita sinais frágeis ou incoerentes.
    Retorna uma tupla: (True/False, motivo)
    """

    if confidence < 0.6:
        return False, f"🔻 Confiança baixa: {confidence:.2f}"

    if abs(R_t) < threshold:
        return False, f"📉 Retorno fraco: R_t = {R_t:.4f}"

    if S_t * T_t < 0:
        return False, f"❗ Divergência entre sentimento e tendência: S_t = {S_t}, T_t = {T_t}"

    risk_factor = L_t + volatility
    if abs(R_t) < risk_factor * 0.8:
        return False, f"⚠️ R_t ({R_t:.4f}) < 0.8 × (risk + vol = {risk_factor:.4f})"

    return True, "✅ Válido"