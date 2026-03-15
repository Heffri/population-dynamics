"""
Numerical ODE solvers.

Implements Forward Euler from scratch, alongside a thin wrapper
around scipy's RK45 for comparison.
"""

import numpy as np
from scipy.integrate import solve_ivp


def forward_euler(f, y0, t0, T, h, **params):
    """
    Solve a system of ODEs using the Forward Euler method.

    y_{n+1} = y_n + h * f(t_n, y_n)

    Parameters
    ----------
    f      : callable  ODE function f(t, y, **params).
    y0     : array-like  Initial state vector.
    t0     : float       Start time.
    T      : float       End time.
    h      : float       Step size.
    **params             Extra keyword arguments forwarded to f.

    Returns
    -------
    t : np.ndarray  Time points, shape (N+1,).
    y : np.ndarray  Solution array, shape (N+1, len(y0)).
    """
    y0 = np.atleast_1d(np.array(y0, dtype=float))
    N  = int(round((T - t0) / h))
    t  = np.linspace(t0, T, N + 1)
    y  = np.zeros((N + 1, len(y0)))
    y[0] = y0

    for i in range(N):
        y[i + 1] = y[i] + h * np.array(f(t[i], y[i], **params))

    return t, y


def rk45(f, y0, t0, T, **params):
    """
    Solve a system of ODEs using scipy's adaptive RK45 solver.

    Parameters
    ----------
    f      : callable    ODE function f(t, y, **params).
    y0     : array-like  Initial state vector.
    t0     : float       Start time.
    T      : float       End time.
    **params             Extra keyword arguments forwarded to f via args tuple.

    Returns
    -------
    t : np.ndarray  Time points chosen by the adaptive solver.
    y : np.ndarray  Solution array, shape (len(t), len(y0)).
    sol : OdeSolution  Dense output callable (sol(t) for arbitrary t).
    """
    result = solve_ivp(
        f,
        (t0, T),
        y0,
        method="RK45",
        args=tuple(params.values()),
        dense_output=True,
    )
    return result.t, result.y.T, result.sol
