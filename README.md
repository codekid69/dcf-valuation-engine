# Valuation Engine — DCF Module

This project implements a clean, production-ready **Discounted Cash Flow (DCF)** valuation engine.

## What it does
- Accepts structured inputs (JSON/kwargs)
- Projects cash flows, discounts them, and adds terminal value (Gordon Growth)
- Outputs valuation with **intermediate steps**
- Includes **sensitivity analysis** helper

## Files
- `valuation_model.py` — core logic (`DCFInputs`, `DCFValuation`)
- `example_run.py` — demo runner that prints results and writes `sample_output.json`
- `sensitivity.py` — generates `sensitivity.csv` for growth/discount-rate grid
- `sample_input.json` — example inputs
- `requirements.txt` — no external deps
- `README.md` — this file

## How to run (Python 3.9+)
```bash
python example_run.py
python sensitivity.py
```

## Inputs
```json
{
  "revenue": 500000.0,
  "growth_rate": 0.1,
  "discount_rate": 0.12,
  "terminal_growth": 0.03,
  "years": 5
}
```

## Output (sample)
Run `python example_run.py` to generate and print:
- Cash flows (each year)
- Discounted cash flows
- Terminal value (undiscounted & discounted)
- **Enterprise value**

It also writes `sample_output.json` for submission.

## Assumptions
- `revenue` is treated as a **cash flow proxy** for the base period. In a full system you would use Free Cash Flow (FCF).
- Constant growth during the explicit forecast.
- Gordon Growth for terminal value (`discount_rate > terminal_growth`).

## Integration notes
- Import `DCFValuation` into a service or API; inputs can come from a form/JSON.
- All logic is pure & side-effect free (easy to test).
- Raises clear validation errors for unsafe inputs.

## Sensitivity analysis
Run `python sensitivity.py` to write a grid of EV across growth and discount-rate scenarios to `sensitivity.csv`.

## License
MIT
