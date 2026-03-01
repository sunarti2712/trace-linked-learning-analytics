# Trace-Linked Learning Analytics (Full Reproducible Repository)

This repository provides full statistical reproducibility for:

"Modeling accountability-driven redistribution in technology-mediated classrooms"

## Reproduce Main Results

Install dependencies:
    pip install pandas numpy scipy

Run:
    python scripts/04_chi_square_analysis.py
    python scripts/05_effect_size_cramers_v.py

## Data
data/raw/aggregated_counts.csv → corresponds to Table 10

## Outputs
Scripts generate:
- Chi-square statistic
- Degrees of freedom
- p-value
- Cramér’s V

This repository follows transparent, audit-ready analytics standards.
