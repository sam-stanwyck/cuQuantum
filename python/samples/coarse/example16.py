"""
Example illustrating a batched operation.
"""
import numpy as np

from cuquantum import contract


a = np.random.rand(2,4)
b = np.random.rand(2,4)

# Batched inner product.
expr = "ij,ij->i"

r = contract(expr, a, b)
s = np.einsum(expr, a, b)
assert np.allclose(r, s), "Incorrect results."
