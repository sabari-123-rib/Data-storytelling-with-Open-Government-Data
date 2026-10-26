"""
CAPSTONE 46 chart refresh script
Usage: python refresh_charts.py udise_2023_24_national_highlights.csv
Requires: pandas, matplotlib
This script refreshes charts from a local CSV; it does not fetch web data automatically.
"""
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

REQUIRED = {"indicator", "value", "unit", "reference_period", "source_url", "notes"}

def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python refresh_charts.py <input.csv>")
    source = Path(sys.argv[1])
    df = pd.read_csv(source)
    missing_cols = REQUIRED - set(df.columns)
    if missing_cols:
        raise SystemExit(f"Missing required columns: {sorted(missing_cols)}")
    if df["indicator"].duplicated().any():
        print("WARNING: duplicate indicator names found; review before charting.")
    if df["value"].isna().any():
        print("WARNING: missing values exist. They will not be replaced with zero.")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    if df["value"].isna().any():
        print("WARNING: non-numeric or missing values found.")
    outdir = Path("refreshed_charts")
    outdir.mkdir(exist_ok=True)

    def lookup(name):
        rows = df.loc[df["indicator"] == name, "value"]
        if rows.empty or pd.isna(rows.iloc[0]):
            raise ValueError(f"Required indicator missing or invalid: {name}")
        return float(rows.iloc[0])

    # Chart: gross enrolment ratio
    ger_names = [
        "Gross enrolment ratio - Primary",
        "Gross enrolment ratio - Upper primary",
        "Gross enrolment ratio - Elementary",
        "Gross enrolment ratio - Secondary",
        "Gross enrolment ratio - Higher secondary",
    ]
    ger = [lookup(n) for n in ger_names]
    labels = ["Primary", "Upper primary", "Elementary", "Secondary", "Higher secondary"]
    plt.figure(figsize=(9, 5))
    plt.bar(labels, ger)
    plt.ylabel("Gross enrolment ratio (%)")
    plt.title("India's gross enrolment ratio by school stage")
    plt.ylim(0, max(100, max(ger) + 5))
    plt.xticks(rotation=18, ha="right")
    plt.figtext(0.01, 0.01, "Source: UDISE+; check reference_period and source_url in CSV.", fontsize=8)
    plt.tight_layout(rect=[0, .05, 1, 1])
    plt.savefig(outdir / "ger_by_stage.png", dpi=180)
    plt.close()
    print(f"Refreshed charts saved to: {outdir.resolve()}")

if __name__ == "__main__":
    main()
