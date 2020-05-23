import numpy as np
from numpy_fracdiff import fracdiff
from statsmodels.tsa.stattools import adfuller
import scipy.optimize


def loss_fn(d: float, x: np.array, tau: float, mmax: int) -> float:
    z = fracdiff(x, order=d, tau=tau, mmax=mmax)
    # compute ADF test
    stat, pval, _, _, crit, _ = adfuller(
        z[mmax:], regression='c', autolag='BIC')
    # pick the fractal order with its ADF-statistics ==< critical value
    return (stat - crit['1%'])**2 + pval**2


def fracadf2(X: np.array, tau: float = 1e-5, mmax: int = 4092,
             lb: float = 0.01, ub: float = 1.5,
             xtol: float = 1e-4, n_maxiter: int = 200) -> float:
    """variable truncation order

    Rules of thumb:
    ---------------
        tau   mmax
        ---- ------
        1e-2     11
        1e-3     73
        1e-4    527
        1e-5   4092
        1e-6  33243
    """
    # ensure that the truncation order does not exceed n_obs-30
    mmax_ = min(X.shape[0] - 30, mmax)

    # one time series
    if len(X.shape) == 1:
        return scipy.optimize.fminbound(
            loss_fn, lb, ub, args=(X, tau, mmax_),
            xtol=xtol, maxfun=n_maxiter)

    # many time series, one for each column
    n_features = X.shape[1]
    d = np.empty((n_features,))
    for j in range(n_features):
        d[j] = scipy.optimize.fminbound(
            loss_fn, lb, ub, args=(X[:, j], tau, mmax_),
            xtol=xtol, maxfun=n_maxiter)
    return d
