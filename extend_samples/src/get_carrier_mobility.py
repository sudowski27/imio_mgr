"""version 0.1.0"""


def get_carrier_mobility(mu_0: float, t_0: float, t: float, alpha: float) -> float:
    """
    Get carrier mobility which depends on temperature

    Parameters
    ----------
    mu_0: float
    t_0: float
    t: float
    alpha: float

    Returns
    -------
    float

    Rises
    -----
    ValueError
        devide by zero
    """
    try:
        mu = mu_0 * pow((t_0 / t), alpha)
    except ZeroDivisionError as exc:
        raise ValueError(f"The value of t cannot be {t}") from exc

    return mu
