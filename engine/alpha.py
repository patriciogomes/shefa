import math

def calculate_allocation(R_t, S_t, T_t, V_t, L_t, C_t,
                         alpha=0.5, beta=0.5, gamma=1.0, lambda_=1.0,
                         kappa=1.2, mu=1.5, delta=1e-6):
    """
    Shefa Quantum v1.0 - Adaptive Allocation Function

    Parameters:
    - R_t: Expected return
    - S_t: Sentiment score
    - T_t: Technical trend
    - V_t: Volatility
    - L_t: Risk
    - C_t: Confidence from AI
    - alpha, beta: weights for S_t and T_t
    - gamma, lambda_: weights for volatility and risk
    - kappa: confidence amplification factor
    - mu: risk penalty power
    - delta: small number to prevent division by zero

    Returns:
    - A_t: position size (normalized between -1 and +1)
    """
    numerator = (R_t + alpha * S_t + beta * T_t) * (C_t ** kappa)
    denominator = (gamma * V_t + lambda_ * L_t + delta) ** mu
    raw_allocation = numerator / denominator
    A_t = math.tanh(raw_allocation)
    return A_t