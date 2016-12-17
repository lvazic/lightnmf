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
