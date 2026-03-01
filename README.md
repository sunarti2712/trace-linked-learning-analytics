
# Data and Code Availability Statement
## Modeling accountability-driven redistribution in technology-mediated classrooms

Author: Sunarti  
Affiliation: Learning Science, Education Department, Tianjin University  
Corresponding author: sunarti@tju.edu.cn  

---

## Overview

This repository provides the data structure, analytic scripts, and reproducible workflow accompanying the study:

**“Modeling accountability-driven redistribution in technology-mediated classrooms: A trace-linked multiple-case learning analytics study.”**

The study develops a trace-linked analytic infrastructure that models instructional activity as a phase-conditioned probability distribution under accountability-driven constraints. Classroom episodes were segmented, coded into mutually exclusive activity states, and linked to de-identified platform artifacts to ensure analytic auditability.

The repository enables independent reproduction of the main statistical results reported in the manuscript.

---

## Repository Contents

### Data

`data/raw/aggregated_counts.csv`  
Aggregated episode counts corresponding to Table 10 in the manuscript.  
The dataset contains phase-level counts for:

- Drill/Test  
- Task  
- Feedback  
- Admin  

All data are fully de-identified and aggregated. No personal or institutional identifiers are included.

---

### Code

`scripts/04_chi_square_analysis.py`  
Computes:
- Pearson chi-square statistic  
- Degrees of freedom  
- p-value  

`scripts/05_effect_size_cramers_v.py`  
Computes:
- Cramér’s V effect size  

`analysis_notebook/full_reproducible_analysis.ipynb`  
Jupyter notebook reproducing:
- Chi-square test  
- Effect-size calculation  
- Output matching manuscript Results section  

---

## Reproducibility Instructions

### Software Requirements

Python 3.9+

Install dependencies:

    pip install pandas numpy scipy

### Reproduce Statistical Results

Run:

    python scripts/04_chi_square_analysis.py
    python scripts/05_effect_size_cramers_v.py

Or open the Jupyter notebook and execute all cells.

---

## Data Governance and Ethics

All original classroom trace data were:

- De-identified prior to analysis  
- Stored under controlled-access governance  
- Linked using anonymized EpisodeID–ArtifactID indexing  

The shared dataset represents aggregated counts only and contains no identifiable information.

---

## Methodological Transparency

The repository reflects the following transparency principles:

- Explicit mapping between manuscript tables and shared data  
- Reproducible statistical workflow  
- Cluster-aware interpretation of effect sizes  
- Separation between descriptive redistribution modeling and causal inference  

This design ensures audit-ready learning analytics consistent with open science standards.

---

## Citation

If using this repository, please cite the associated publication.

---

## License

This repository is provided for academic and research purposes.
