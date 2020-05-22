import numpy as np
from numpy_fracdiff import fracdiff
from statsmodels.tsa.stattools import adfuller
import scipy.optimize


def loss_fn(d: float, x: np.array, n_trunc: int) -> float:
    z = fracdiff(x, order=d, truncation=n_trunc)
    stat, pval, _, _, crit, _ = adfuller(
        z[n_trunc:], regression='c', autolag='BIC')
    return (stat - crit['1%'])**2 + pval**2


def fracadf(X: np.array, n_trunc: int = 100,
            lb: float = 0.01, ub: float = 1.5,
            xtol: float = 1e-4, n_maxiter: int = 200) -> float:
    if len(X.shape) == 1:
        return scipy.optimize.fminbound(
            loss_fn, lb, ub, args=(X, n_trunc),
            xtol=xtol, maxfun=n_maxiter)

    n_features = X.shape[1]
    d = np.empty((n_features,))
    for j in range(n_features):
        d[j] = scipy.optimize.fminbound(
            loss_fn, lb, ub, args=(X[:, j], n_trunc),
            xtol=xtol, maxfun=n_maxiter)
    return d
