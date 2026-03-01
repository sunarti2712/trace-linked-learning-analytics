import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

df = pd.read_csv('../data/raw/aggregated_counts.csv')
table = df[['Drill_Test','Task','Feedback','Admin']].values

chi2, p, dof, expected = chi2_contingency(table)

print("Chi-square:", round(chi2, 4))
print("Degrees of freedom:", dof)
print("p-value:", p)
