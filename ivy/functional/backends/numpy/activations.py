"""
Collection of Numpy activation functions, wrapped to fit Ivy syntax and signature.
"""

# global
import numpy as np
try:
    from scipy.special import erf as _erf
except (ImportError, ModuleNotFoundError):
    _erf = None

relu = lambda x: np.maximum(x, 0)
leaky_relu = lambda x, alpha=0.2: np.where(x > 0, x, x * alpha)


def gelu(x, approximate=True):
    if _erf is None:
        raise Exception('scipy must be installed in order to call ivy.gelu with a numpy backend.')
    if approximate:
        return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x ** 3)))
    return 0.5 * x * (1 + _erf(x/np.sqrt(2)))


tanh = np.tanh
sigmoid = lambda x: 1 / (1 + np.exp(-x))


def softmax(x, axis=-1):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis, keepdims=True)


softplus = lambda x: np.log(np.exp(x) + 1)
