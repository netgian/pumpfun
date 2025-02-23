# pump.fun API Wrapper for Python

Pump Fun API Wrapper is a Python package designed to facilitate interaction with the [pump.fun frontend API](https://frontend-api.pump.fun/api). It provides a comprehensive set of functions for retrieving transaction data, managing user and coin information.

## Features

- Retrieve the latest trades and transaction history.
- Query information about available coins.
- User management and information retrieval.

TO DO: Get to work the post, put, delete methods
## Installation

You can install this package via pip using:

```bash
pip install pumpfun
```

## Usage

### Importing the Package

```python
import pumpfun
```

### Example Usage

```python
from pumpfun import get_all_trades, get_sol_price

# Retrieve the latest trades for a given mint
trades = get_all_trades(mint="7vJY...pump", limit=10)
print(trades)

# Get the current SOL price
sol_price = get_sol_price()
print(f"Current SOL Price: {sol_price}")
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Contact:** [gianlopez.cv@gmail.com](mailto\:gianlopez.cv@gmail.com)
