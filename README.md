
# Data and Code Availability Statement  
# 数据与代码开放说明  

## Modeling accountability-driven redistribution in technology-mediated classrooms  
## 技术媒介课堂中问责驱动再分配建模研究  

Author / 作者: Sunarti  
Affiliation / 单位: Learning Science, Education Department, Tianjin University  
Corresponding author / 通讯作者: sunarti@tju.edu.cn  

---

## Overview / 项目简介

This repository provides data structure, analytic scripts, and a reproducible workflow supporting the study:

本仓库提供数据结构、分析脚本以及可复现的研究流程，用于支持以下论文：

**“Modeling accountability-driven redistribution in technology-mediated classrooms: A trace-linked multiple-case learning analytics study.”**  

The study proposes a trace-linked learning analytics framework that models instructional organization as a phase-conditioned probability distribution under accountability constraints.

本研究提出一种可追溯学习分析框架，将课堂教学组织建模为在问责约束条件下的阶段条件概率分布。

Rather than treating digital traces as isolated behavioral indicators, this study links episode-level coding with verifiable platform artifacts.

本研究并不将数字痕迹视为孤立的行为指标，而是将课堂片段编码与可验证的平台证据进行系统关联。

---

## Repository Contents / 仓库结构

### Data / 数据

`data/raw/aggregated_counts.csv`  

Aggregated episode counts corresponding to Table 10 in the manuscript.  
对应论文 Table 10 的聚合课堂片段数据。  

Variables include / 变量包括：

- Drill/Test  
- Task  
- Feedback  
- Admin  

All shared data are de-identified and aggregated.  
所有共享数据均已去标识化并进行聚合处理。  

---

### Code / 代码

`scripts/04_chi_square_analysis.py`  
Compute Pearson chi-square statistic  
计算卡方统计量  

`scripts/05_effect_size_cramers_v.py`  
Compute Cramér’s V effect size  
计算 Cramér’s V 效应量  

`analysis_notebook/full_reproducible_analysis.ipynb`  
Jupyter notebook reproducing all core statistics  
可复现全部核心统计结果的 Notebook  

---

## Reproducibility Instructions / 复现步骤

### Software Requirements / 软件要求

Python 3.9+

Install dependencies / 安装依赖：

    pip install pandas numpy scipy

Run scripts / 运行脚本：

    python scripts/04_chi_square_analysis.py
    python scripts/05_effect_size_cramers_v.py

Or execute the notebook step-by-step.  
或逐步运行 Notebook 文件。

---

## Data Governance and Ethics / 数据治理与伦理

All original classroom traces were:

- De-identified prior to analysis  
- Stored under controlled-access governance  
- Linked via anonymized EpisodeID–ArtifactID structure  

所有原始课堂数据：

- 在分析前已去标识化  
- 存储于受控访问系统  
- 通过匿名 EpisodeID–ArtifactID 结构进行关联  

No personally identifiable information is included.  
本仓库不包含任何可识别个人信息。  

---

## Methodological Transparency / 方法透明性

This repository demonstrates:

- Explicit mapping between manuscript tables and shared data  
- Reproducible statistical workflow  
- Cluster-aware effect size interpretation  
- Separation between descriptive modeling and causal inference  

本仓库体现：

- 论文表格与数据之间的明确对应关系  
- 可复现的统计流程  
- 基于聚类结构的效应量解释  
- 描述性建模与因果推断之间的严格区分  

---

## Citation / 引用方式

If you use this repository, please cite the associated publication.  
如使用本仓库，请引用对应论文。  

---

## License / 许可协议

This repository is provided for academic research use.  
本仓库仅供学术研究使用。  
