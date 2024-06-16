# option
A simple tool for option price related tasks

## Usage

```python
from option import OPTION
import datetime

# Create an option
opt = OPTION(K=100, t="2023-12-31", delta=0.5, gamma=0.1, theta=-0.01, vega=0.2, rho=0.05)

# Print option details
opt.print_details()

# Calculate time to maturity
current_date = "2023-06-16"
print(f"Time to maturity: {opt.time_to_maturity(current_date)} years")

# Update option Greeks
opt.update_greeks(delta=0.6, theta=-0.02)

# Calculate breakeven price
option_price = 10
print(f"Breakeven price: {opt.breakeven(option_price)}")

# Calculate intrinsic value
current_underlying_price = 110
print(f"Intrinsic value: {opt.intrinsic_value(current_underlying_price)}")

# Calculate option price change
s0 = 100
s1 = 105
time0 = "2023-06-16"
time1 = "2023-06-17"
sigma0 = 0.2
sigma1 = 0.25
r0 = 0.01
r1 = 0.02
print(f"Option price change: {opt.optionpricechange(s0, s1, time0, time1, sigma0, sigma1, r0, r1)}")
```

## Methods

`__init__(self, K, t, delta, gamma, theta, vega, rho)` <br />
Initialize the OPTION instance with given parameters.

`_check_and_convert_date(self, date)` <br />
Check and convert date inputs to datetime.datetime.

`print_details(self)` <br />
Print the details of the option.

`time_to_maturity(self, current_date)` <br />
Calculate the time to maturity from the current date.

`update_greeks(self, delta=None, gamma=None, theta=None, vega=None, rho=None)` <br />
Update the option Greeks with new values.

`breakeven(self, option_price)` <br />
Calculate the breakeven price of the option.

`intrinsic_value(self, s)` <br />
Calculate the intrinsic value of the option based on the current underlying price.

`option_price_change(self, s0, s1, time0, time1, sigma0=None, sigma1=None, r0=None, r1=None)` <br />
Calculate the change in option price based on changes in underlying price, time, volatility, and interest rates.
