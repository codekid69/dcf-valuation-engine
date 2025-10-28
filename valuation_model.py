from dataclasses import dataclass
from typing import List, Dict

@dataclass
class DCFInputs:
    revenue: float                 # Base-period cash flow proxy (e.g., FCF)
    growth_rate: float             # Annual growth rate (e.g., 0.10 for 10%)
    discount_rate: float           # WACC / required return (e.g., 0.12)
    terminal_growth: float         # Long-term growth after forecast period (e.g., 0.03)
    years: int = 5                 # Explicit forecast period length

    def validate(self) -> None:
        if self.years <= 0:
            raise ValueError("years must be > 0")
        if self.discount_rate <= self.terminal_growth:
            raise ValueError("discount_rate must be greater than terminal_growth to use Gordon Growth")
        for name, val in [("revenue", self.revenue), ("growth_rate", self.growth_rate),
                          ("discount_rate", self.discount_rate), ("terminal_growth", self.terminal_growth)]:
            if not isinstance(val, (int, float)):
                raise TypeError(f"{name} must be numeric")


class DCFValuation:
    """Production-grade DCF valuation core."""

    def __init__(self, inputs: DCFInputs):
        inputs.validate()
        self.i = inputs

    def project_cash_flows(self) -> List[float]:
        """Project future cash flows using constant growth from the base revenue/cash flow."""
        return [self.i.revenue * (1 + self.i.growth_rate) ** t for t in range(1, self.i.years + 1)]

    def discount_cash_flows(self, cash_flows: List[float]) -> List[float]:
        return [cf / (1 + self.i.discount_rate) ** t for t, cf in enumerate(cash_flows, start=1)]

    def terminal_value(self, last_cash_flow: float) -> float:
        """Gordon Growth terminal value."""
        return last_cash_flow * (1 + self.i.terminal_growth) / (self.i.discount_rate - self.i.terminal_growth)

    def compute(self) -> Dict[str, float | List[float]]:
        cash_flows = self.project_cash_flows()
        discounted = self.discount_cash_flows(cash_flows)
        tv = self.terminal_value(cash_flows[-1])
        tv_discounted = tv / (1 + self.i.discount_rate) ** self.i.years
        ev = sum(discounted) + tv_discounted
        return {
            "cash_flows": cash_flows,
            "discounted_cash_flows": discounted,
            "terminal_value": tv,
            "terminal_value_discounted": tv_discounted,
            "enterprise_value": ev,
        }
