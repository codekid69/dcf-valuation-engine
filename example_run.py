from valuation_model import DCFInputs, DCFValuation
import json

def main():
    # Example inputs 
    inputs = DCFInputs(
        revenue=500000.0,
        growth_rate=0.10,
        discount_rate=0.12,
        terminal_growth=0.03,
        years=5
    )
    model = DCFValuation(inputs)
    result = model.compute()

    print("\n--- Valuation Summary ---")
    for i, (cf, disc) in enumerate(zip(result["cash_flows"], result["discounted_cash_flows"]), 1):
        print(f"Year {i}: Cash Flow = {cf:,.2f}, Discounted = {disc:,.2f}")
    print(f"\nTerminal Value (undiscounted): {result['terminal_value']:,.2f}")
    print(f"Terminal Value (discounted):   {result['terminal_value_discounted']:,.2f}")
    print(f"\nEnterprise Value (DCF):      {result['enterprise_value']:,.2f}\n")

    # Save JSON output for the submission
    with open('sample_output.json', 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
