import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

df = pd.read_csv('../data/raw/aggregated_counts.csv')
table = df[['Drill_Test','Task','Feedback','Admin']].values

chi2, p, dof, expected = chi2_contingency(table)

n = table.sum()
k = min(table.shape) - 1
cramers_v = np.sqrt(chi2 / (n * k))

print("Cramér's V:", round(cramers_v, 4))
