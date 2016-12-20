lightnmf
===========

Simple implementation of Non-Negative Matrix Factorization (NMF) using multiplicative update rules relying on NumPy matrices.
[More on NMF.](http://vazic.me/non-negative-matrix-factorization-nmf/)

# Installation
```bash
pip install lightnmf
```

# Usage
```python
import lightnmf
```

## Get weights and features matrices using L2-norm cost function

```python
w, h = lightnmf.factorize(m)
```

## Get weights and features matrices using L1-norm cost function
```python
w, h = lightnmf.factorize(m, l1=True)
```

## Set desired number of factors and number of iterations for multiplicative update rules
```python
w, h = lightnmf.factorize(m, num_of_factors=15, num_of_iterations=2000)
```
