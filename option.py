import datetime
class OPTION:
    def __init__(self, K, t, delta, gamma, theta, vega, rho):
        self.type = "Call" if delta > 0 else "Put" # Option Type (Call / Put)
        self.K = K          # Strike Price
        self.t = self._check_and_convert_date(t)    # Expiration Day
        self.delta = delta  # Option Δ
        self.gamma = gamma  # Option Γ
        self.theta = theta  # Option Θ
        self.vega = vega    # Option ν
        self.rho = rho      # Option ρ
    
    # Check Date Inputs
    def _check_and_convert_date(self, date):
        if isinstance(date, str):
            return datetime.datetime.strptime(date, "%Y-%m-%d")
        elif isinstance(date, datetime.datetime):
            return date
        else:
            raise TypeError("Date should be a datetime object or a string in '%Y-%m-%d' format")
    
    def print_details(self):
        details = f"Option Type: {self.type}\nStrike Price: {self.K}\nExpiration Day: {self.t}\n"
        details += f"Delta: {self.delta}\nGamma: {self.gamma}\nTheta: {self.theta}\nVega: {self.vega}\nRho: {self.rho}"
        print(details)

    def time_to_maturity(self, current_date):
        current_date = self._check_and_convert_date(current_date)
        time_to_maturity = (self.t - current_date).days / 365.0
        return time_to_maturity

    def update_greeks(self, delta=None, gamma=None, theta=None, vega=None, rho=None):
        if delta is not None:
            self.delta = delta
        if gamma is not None:
            self.gamma = gamma
        if theta is not None:
            self.theta = theta
        if vega is not None:
            self.vega = vega
        if rho is not None:
            self.rho = rho
    
    def breakeven(self, option_price):
        breakeven_price = self.K + option_price if self.type == "Call" else self.K - option_price
        return breakeven_price
    
    def intrinsic_value(self, s):
        return max(s - self.K, 0) if self.type == "Call" else max(self.K - s, 0)

    def optionpricechange(self, s0, s1, time0, time1, sigma0=None, sigma1=None, r0=None, r1=None):
        time0 = self._check_and_convert_date(time0)
        time1 = self._check_and_convert_date(time1)
        delta_t = (time1 - time0).days / 365.0  # Change in time (time decay)
        delta_s = s1 - s0                       # Change in underlying price
        option_price_change = (self.delta * delta_s) + \
                              (0.5 * self.gamma * delta_s**2) - \
                              (self.theta * delta_t)
        if sigma0 is not None or sigma1 is not None:    # If sigma0 or sigma1 are provided
            delta_sigma = sigma1 - sigma0               # Change in volatility
            option_price_change += (self.vega * delta_sigma)
        if r0 is not None or r1 is not None:            # If r0 and r1 are provided
            delta_r = r1 - r0                           # Change in interest rate
            option_price_change += (self.rho * delta_r)
        return option_price_change
