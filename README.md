# Pump Fun API Wrapper

pump.fun API Wrapper is a Python package designed to facilitate interaction with the Pump Fun API. It provides a comprehensive set of functions for retrieving transaction data, managing user and coin information.

## 📌 Features

- Retrieve the latest trades and transaction history.
- Query information about available coins.
- Search and manage coins efficiently.

## 🚀 Installation

You can install this package via pip using:

```bash
pip install pumpfun
```

## 🔧 Usage

### Importing the Package

```python
import pumpfun
```

### Example Usage

```python
from pumpfun import get_latest_trades, get_sol_price

# Retrieve the latest trades
trades = get_latest_trades()
print(trades)

# Get the current SOL price
sol_price = get_sol_price()
print(f"Current SOL Price: {sol_price}")
```

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

📧 **Contact:** [gianlopez.cv@gmail.com](mailto\:gianlopez.cv@gmail.com)
