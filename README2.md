
### Empirical Exploratory Data Analysis & Educational Predictive Modeling

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-008080.svg)](https://seaborn.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)



## #########################################Resume-Ready Project Summary

> **Analyzed 1,040+ secondary academic records across Mathematics and Language curricula using Python, Pandas, Matplotlib, and Seaborn to model grade trajectories, attendance effects, and socio-demographic indicators—identifying an early 80% baseline performance lock-in ($r = 0.801$) and revealing that adjusting for exam dropouts shifts the raw attendance-grade correlation from neutral ($+0.034$) to strongly negative ($-0.213$).**


## #############################################Project Objective

An educational institution sought to uncover the root drivers of academic achievement, failure risk, and course dropout among secondary school students. Using demographic, family background, academic tracking, and lifestyle surveys, this project conducts an end-to-end Exploratory Data Analysis (EDA) across two core subjects to:
1. Examine final grade ($G3$) distributions and passing rates ($G3 \ge 10$) in Mathematics and Portuguese Language.
2. Investigate the elasticity of weekly study hours and identify potential diminishing returns.
3. Resolve the statistical paradox between raw absenteeism logs and actual exam outcomes.
4. Assess the impact of parental education levels and occupational fields on student attainment.
5. Model longitudinal academic trajectories across Term 1 ($G1$), Term 2 ($G2$), and Final Grade ($G3$).
6. Provide actionable institutional recommendations to enable early-warning interventions before failure lock-in occurs.



## ######################################## Dataset Overview

- Dataset Source: [UCI Machine Learning Repository - Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student+performance) (Cortez & Silva, 2008)
- Scope: 
  - Mathematics (`student-mat.csv`): 395 student records, 33 attributes
  - Portuguese Language (`student-por.csv`): 649 student records, 33 attributes
  - Dual-Enrolled Cohort: 382 students identified across 13 demographic anchor keys
  - Unified Evaluations: 1,044 records
- **Data Completeness:** Semicolon-delimited (`sep=\x27;\x27`) | 0 missing values | 0 duplicate records

#####################################Core Data Dictionary###################
| Variable | Type | Scale / Range | Description |
| :--- | :--- | :--- | :--- |
| `school` | Binary | `\"GP\"`, `\"MS\"` | Gabriel Pereira (urban) or Mousinho da Silveira (rural) |
| `sex` | Binary | `\"F\"`, `\"M\"` | Biological sex of student |
| `age` | Discrete | 15 to 22 | Student age in years |
| `Medu` / `Fedu` | Ordinal | 0 to 4 | Mother\x27s / Father\x27s education level (0: None, 4: Higher Ed) |
| `Mjob` / `Fjob` | Nominal | Teacher, Health, Services, At Home, Other | Parental occupational sector |
| `studytime` | Ordinal | 1 to 4 | Weekly study hours (1: <2h, 2: 2–5h, 3: 5–10h, 4: >10h) |
| `failures` | Discrete | 0 to 3 | Count of prior subject course failures |
| `schoolsup` | Binary | `\"yes\"`, `\"no\"` | Extra institutional remedial academic support |
| `paid` | Binary | `\"yes\"`, `\"no\"` | Extra paid private tutoring within subject |
| `higher` | Binary | `\"yes\"`, `\"no\"` | Aspiration to pursue higher education |
| `absences` | Continuous | 0 to 93 | Cumulative school absences across the academic year |
| `G1` / `G2` | Continuous | 0 to 20 | First period (Term 1) and Second period (Term 2) grades |
| `G3` | Continuous | 0 to 20 | Final year-end outcome grade (primary target) |



## Data Cleaning & Feature Engineering
1. **Delimiter Handling & Cohort Tagging:** Loaded raw files with `sep=\x27;\x27` and appended subject tags (`Math`, `Portuguese`) prior to unified concatenation.
2. **Dual-Cohort Merging:** Merged on 13 static demographic features (`school`, `sex`, `age`, `address`, `famsize`, `Pstatus`, `Medu`, `Fedu`, `Mjob`, `Fjob`, `reason`, `nursery`, `internet`) to track the 382 students taking both curricula concurrently.
3. **Dropout Isolation (`status` / `is_zero`):** Identified that the 38 zero-grade records in Math (9.62%) represent exam abandonment or course withdrawal rather than ordinary low mastery along a continuous bell curve. Segmented these records to avoid biasing linear regressions.
4. **Engineered Metrics:**
   - `passed`: Boolean pass indicator ($G3 \ge 10$).
   - `delta_G`: Term trajectory progression ($\Delta G = G3 - G1$).
   - `parent_edu`: Composite parental education index ($(Medu + Fedu) / 2.0$).
   - `weekly_alc`: Weighted weekly alcohol index ($(Dalc \times 5.0 + Walc \times 2.0) / 7.0$).


## Key Findings & Research Questions Answered

### 1. Final Grade Distributions & Pass Rates
Mathematics displays a wider spread ($\mu = 10.42, \sigma = 4.58$) and a 67.09% pass rate, while Portuguese Language demonstrates higher mastery ($\mu = 11.91, \sigma = 3.23$) and an 84.59% pass rate. Math exhibits over 4x higher exam dropout rates (9.62% vs. 2.31%).

### 2. Study Time Elasticity & Diminishing Returns
Average Math grades rise from 10.05 for $<2$ hours/week to 11.40 for 5–10 hours/week. However, studying $>10$ hours/week yields no additional grade advantage (11.26), indicating that beyond 10 hours, study efficiency and self-regulation matter more than raw hours logged.

### 3. The Attendance Paradox
Raw Pearson correlation between absences and Math grades appears neutral ($r = +0.034$). However, this is an ecological fallacy caused by zero-grade dropouts who stopped attending school early and thus accrued zero exam-period absences. Among active exam participants, absences exhibit a clear negative penalty ($r = -0.213$).

### 4. Parental Education Gradient
Mother\x27s education ($Medu$, $r = +0.217$ in Math, $+0.240$ in Por) shows a stronger correlation with grades than Father\x27s education ($Fedu$, $r = +0.152$ in Math, $+0.212$ in Por). Households where both parents completed higher education average 12.50–12.96, compared to 9.95–10.50 where parents have primary education.

### 5. Early Baseline Lock-In
Term 1 grade ($G1$) correlates at $r = +0.801$ with final grade ($G3$), and Term 2 ($G2$) correlates at $r = +0.905$. Prior subject failures exhibit a severe negative penalty ($r = -0.360$): students with zero failures average 11.02, while students with $\ge 1$ failure average 8.83.

### 6. Subject-Specific Gender Divergence
Male students score higher on average in Mathematics (10.91 vs. 9.97 for females), whereas female students outperform males in Portuguese Language (12.25 vs. 11.41 for males).



## Complete Visualization Gallery (17 Visualizations)

| Visualization | Filename | Key Research Finding |
| :--- | :--- | :--- |
| **Hist 1** | `01_hist_final_grades.png` | Bimodal Math distribution due to dropout cluster vs. smooth Portuguese bell curve. |
| **Hist 2** | `02_hist_absences.png` | Extreme right skew in absences; 75% of students miss <8 days. |
| **Hist 3** | `03_hist_age_school.png` | Age distribution centered at 15–18; older students (19–22) skew toward repeat years. |
| **Box 1** | `04_box_studytime_g3.png` | Diminishing returns plateau beyond 5–10 weekly study hours. |
| **Box 2** | `05_box_failures_g3.png` | Steep negative grade penalty associated with prior course failures. |
| **Box 3** | `06_box_medu_g3.png` | Step-level academic increases corresponding to maternal educational attainment. |
| **Bar 1** | `07_bar_mjob_g3.png` | Highest performance in healthcare/teaching households; lowest in at-home households. |
| **Bar 2** | `08_bar_support_pass_rate.png` | Institutional remedial support (`schoolsup`) currently tracks lower pass rates (late intervention). |
| **Bar 3** | `09_bar_gender_subject.png` | Cross-subject divergence: Males lead in Math (+0.94), Females lead in Language (+0.84). |
| **Count 1** | `10_count_famrel.png` | Over 75% of students report positive family relationship quality (levels 4–5). |
| **Count 2** | `11_count_higher_activities.png` | Extracurriculars correlate strongly with higher education aspirations (>90%). |
| **Scatter 1**| `12_scatter_g1_g3.png` | Strong linear correlation ($r=0.80$) with explicit callout of the dropout cluster. |
| **Scatter 2**| `13_scatter_absences_g3.png` | True attendance penalty revealed after disaggregating zero-grade dropouts. |
| **Heatmap** | `14_heatmap_correlation.png` | Comprehensive Pearson correlation matrix across behavioral and academic attributes. |
| **Trend** | `15_trajectory_terms.png` | Longitudinal trimester progression ($G1 \\rightarrow G2 \\rightarrow G3$) showing divergence by failure history. |
| **Custom 1** | `16_custom_parent_edu_grid.png`| Joint $5\\times 5$ interaction matrix of Mother\x27s vs. Father\x27s education on final grades. |
| **Custom 2** | `17_custom_delta_grades.png` | Academic shift distribution ($\Delta G = G3 - G1$) centered near zero with negative dropout tail. |



## Strategic Institutional Recommendations
1. **Term 1 Early Warning System:** Deploy automated alerts for any student scoring $G1 \\le 9$ or with prior failures to initiate tutoring before mid-year performance locks in.
2. **Attendance Disengagement Tracking:** Monitor consecutive unexcused absences between Term 1 and Term 2 to intervene before students drop out or abandon exams.
3. **Reform Remedial School Support:** Shift `schoolsup` from late-stage corrective assignments into proactive small-group mastery workshops early in the academic year.
4. **Study Skills & Active Recall Workshops:** Coach students on active learning techniques rather than increasing unguided study hours beyond 10 hours/week.
5. **Targeted First-Generation Support:** Establish faculty-guided study halls and subsidized exam tutoring for students whose parents did not attend higher education.



##  Repository File Structure

student-performance-analytics/
├── charts/                                            # 17 High-resolution figures
│   ├── 01_hist_final_grades.png
│   ├── 02_hist_absences.png
│   ├── ...
│   └── 17_custom_delta_grades.png
├── student-mat.csv                                     # Mathematics evaluation dataset
├── student-por.csv                                     # Portuguese language evaluation dataset
├── student-merge.R                                     # Demographic merging script
├── student.txt                                         # Official UCI data dictionary
├── Project_05_Student_Performance_Analytics.ipynb     # Complete Jupyter Notebook with code & visualizations
├── EDA_Report_Project_05.pdf                           # 5-Page formal academic PDF report
├── Presentation_Project_05.md                          # 8-Slide executive presentation deck
└── README.md                                           # Project overview & summary