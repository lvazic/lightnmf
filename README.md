lightnmf
===========

Simple implementation of Non-Negative Matrix Factorization relying on NumPy matrices.

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
