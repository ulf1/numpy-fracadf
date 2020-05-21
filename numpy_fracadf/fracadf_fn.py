import numpy as np
from numpy_fracdiff import fracdiff
from statsmodels.tsa.stattools import adfuller
from scipy.optimize import ridder


def loss_fn(d: float, x: np.array, alpha: float, n_trunc: int) -> float:
    z = fracdiff(x, order=d, truncation=n_trunc)
    _, pval, _, _, _, _ = adfuller(z[n_trunc:], regression='c', autolag='BIC')
    return pval - alpha  # for Bisection


def fracadf(X: np.array, alpha: float = 0.01, xtol: float = None,
            n_trunc: int = 100) -> float:
    if not xtol:
        xtol = alpha * .01

    if len(X.shape) == 1:
        return ridder(loss_fn, 0, 1, args=(X, alpha, n_trunc), xtol=xtol)

    n_features = X.shape[1]
    d = np.empty((n_features,))
    for j in range(n_features):
        d[j] = ridder(loss_fn, 0, 1, args=(X[:, j], alpha, n_trunc), xtol=xtol)
    return d
