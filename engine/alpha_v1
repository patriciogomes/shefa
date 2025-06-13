
def calculate_allocation(R_t, S_t, T_t, V_t, L_t, alpha=0.5, beta=0.5, gamma=1.0, lambda_=1.0):
    """
    Calculate position size (A_t) based on Shefa Alpha Engine formula.

    Parameters:
    - R_t: Expected return
    - S_t: Sentiment score
    - T_t: Technical trend signal
    - V_t: Volatility
    - L_t: Risk
    - alpha, beta, gamma, lambda_: weight parameters

    Returns:
    - A_t: Recommended position size (normalized)
    """

    numerator = R_t + alpha * S_t + beta * T_t
    denominator = gamma * V_t + lambda_ * L_t

    if denominator == 0:
        return 0.0  # avoid division by zero

    A_t = numerator / denominator
    return A_t
