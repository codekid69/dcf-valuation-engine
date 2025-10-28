from valuation_model import DCFInputs, DCFValuation
import itertools
import csv

def grid(values_growth=(0.06, 0.08, 0.10, 0.12, 0.14),
         values_discount=(0.08, 0.10, 0.12, 0.14, 0.16)):
    results = []
    for g, d in itertools.product(values_growth, values_discount):
        inputs = DCFInputs(
            revenue=500000.0,
            growth_rate=g,
            discount_rate=d,
            terminal_growth=0.03,
            years=5
        )
        ev = DCFValuation(inputs).compute()["enterprise_value"]
        results.append({"growth_rate": g, "discount_rate": d, "enterprise_value": round(ev, 2)})
    return results

def main():
    rows = grid()
    with open("sensitivity.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["growth_rate", "discount_rate", "enterprise_value"])
        writer.writeheader()
        writer.writerows(rows)
    print("Wrote sensitivity.csv")

if __name__ == "__main__":
    main()
