import numpy as np
from numpy_fracdiff import fracdiff
from statsmodels.tsa.stattools import adfuller
import scipy.optimize


def loss_fn(d: float, x: np.array, n_trunc: int) -> float:
    # compute fractal diff for given order and truncation
    z = fracdiff(x, order=d, truncation=n_trunc)
    # compute ADF test
    stat, pval, _, _, crit, _ = adfuller(
        z[n_trunc:], regression='c', autolag='BIC')
    # pick the fractal order with its ADF-statistics ==< critical value
    return (stat - crit['1%'])**2 + pval**2


def fracadf1(X: np.array, n_trunc: int = 100,
             lb: float = 0.01, ub: float = 1.5,
             xtol: float = 1e-4, n_maxiter: int = 200) -> float:
    """constant truncation order"""
    if X.shape[0] <= 30:
        raise ValueError("X must contain more than 30 observations")

    # ensure that the truncation order does not exceed n_obs-30
    n_trunc_ = min(X.shape[0] - 30, n_trunc)

    # one time series
    if len(X.shape) == 1:
        return scipy.optimize.fminbound(
            loss_fn, lb, ub, args=(X, n_trunc_),
            xtol=xtol, maxfun=n_maxiter)

    # many time series, one for each column
    n_features = X.shape[1]
    d = np.empty((n_features,))
    for j in range(n_features):
        d[j] = scipy.optimize.fminbound(
            loss_fn, lb, ub, args=(X[:, j], n_trunc_),
            xtol=xtol, maxfun=n_maxiter)
    return d
