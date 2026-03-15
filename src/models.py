"""
Lotka-Volterra ODE models.

Two variants are provided:
  - two_species: plants (x) and aphids (y)
  - three_species: plants (x), aphids (y), and ladybugs (w)
"""


def two_species(t, y, alpha, beta, delta, gamma):
    """
    2-species Lotka-Volterra system: plants vs. aphids.

    dx/dt =  alpha * x - beta  * x * y   (plant growth, reduced by aphid grazing)
    dy/dt =  delta * x * y - gamma * y   (aphid growth from grazing, natural death)

    Parameters
    ----------
    t : float
        Current time (required by solve_ivp, unused in autonomous system).
    y : array-like [x, y]
        State vector: x = plant population, y = aphid population.
    alpha  : float  Plant intrinsic growth rate.
    beta   : float  Aphid grazing rate on plants.
    delta  : float  Aphid reproduction rate per plant consumed.
    gamma  : float  Aphid natural death rate.

    Returns
    -------
    list [dxdt, dydt]
    """
    x, aphids = y
    dxdt  =  alpha * x - beta  * x * aphids
    dydt  =  delta * x * aphids - gamma * aphids
    return [dxdt, dydt]


def three_species(t, y, alpha, beta, delta, gamma, eta, zeta):
    """
    3-species Lotka-Volterra system: plants, aphids, and ladybugs.

    dx/dt =  alpha * x - beta * x * y            (plants)
    dy/dt =  delta * x * y - gamma * y - eta * y * w   (aphids, now also eaten by ladybugs)
    dw/dt =  eta * y * w - zeta * w               (ladybugs)

    Parameters
    ----------
    t : float
        Current time.
    y : array-like [x, y, w]
        State vector: x = plants, y = aphids, w = ladybugs.
    alpha  : float  Plant growth rate.
    beta   : float  Aphid grazing rate on plants.
    delta  : float  Aphid reproduction rate per plant consumed.
    gamma  : float  Aphid natural death rate.
    eta    : float  Ladybug predation/reproduction rate on aphids.
    zeta   : float  Ladybug natural death/migration rate.

    Returns
    -------
    list [dxdt, dydt, dwdt]
    """
    x, aphids, ladybugs = y
    dxdt  =  alpha * x - beta  * x * aphids
    dydt  =  delta * x * aphids - gamma * aphids - eta * aphids * ladybugs
    dwdt  =  eta   * aphids * ladybugs - zeta * ladybugs
    return [dxdt, dydt, dwdt]
