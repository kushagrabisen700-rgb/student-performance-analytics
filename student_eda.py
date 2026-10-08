import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Visual setup
os.makedirs('charts', exist_ok=True)
sns.set_theme(style='whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# Data Ingestion
mat = pd.read_csv('C:/Users/kusha/OneDrive/Desktop/AIML bleep/finalCAPSTONEproject/student+performance/student/student-mat.csv', sep=';')
por = pd.read_csv('C:/Users/kusha/OneDrive/Desktop/AIML bleep/finalCAPSTONEproject/student+performance/student/student-por.csv', sep=';')

# Add course indicators and combine
mat['subject'] = 'Math'
por['subject'] = 'Portuguese'
df = pd.concat([mat, por], ignore_index=True)

# Data Cleaning and Feature Engineering
for d in [mat, por, df]:
    d['passed'] = d['G3'] >= 10
    d['delta_G'] = d['G3'] - d['G1']
    d['parent_edu'] = (d['Medu'] + d['Fedu']) / 2.0
    d['is_zero'] = d['G3'] == 0

def save_chart(fig, filename):
    fig.tight_layout()
    fig.savefig(f'charts/{filename}.png', dpi=150)
    plt.close(fig)

# %%
# Chart 01: Final Grade Distribution (G3) - Compares grade distributions and passing rates between Math and Portuguese courses.
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(data=df, x='G3', hue='subject', discrete=True, kde=True, ax=ax)
ax.axvline(10, color='red', linestyle='--', label='Passing Mark (10)')
ax.set_title('Chart 01: Final Grade (G3) Distribution')
ax.legend()
save_chart(fig, '01_hist_final_grades')

# %%
# Chart 02: School Absences Distribution - Displays the right-skewed frequency of student absenteeism across subjects.
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(data=df, x='absences', hue='subject', bins=30, ax=ax)
ax.set_title('Chart 02: Distribution of School Absences')
save_chart(fig, '02_hist_absences')

# %%
# Chart 03: Student Age Distribution by School - Compares the age spread between Gabriel Pereira (urban) and Mousinho da Silveira (rural).
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(data=df, x='age', hue='school', discrete=True, multiple='dodge', shrink=0.8, ax=ax)
ax.set_title('Chart 03: Student Age Distribution by School')
save_chart(fig, '03_hist_age_school')

# %%
# Chart 04: Math Grade by Study Time Tier - Illustrates diminishing academic returns beyond 5 to 10 hours of weekly study.
study_map = {1: '<2h', 2: '2-5h', 3: '5-10h', 4: '>10h'}
mat['study_tier'] = mat['studytime'].map(study_map)
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=mat, x='study_tier', y='G3', order=['<2h', '2-5h', '5-10h', '>10h'], ax=ax)
ax.set_title('Chart 04: Math Final Grade by Weekly Study Time')
save_chart(fig, '04_box_studytime_g3')

# %%
# Chart 05: Prior Subject Failures vs Final Grade - Demonstrates the steep drop in grades caused by previous course failures.
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=df, x='failures', y='G3', hue='subject', ax=ax)
ax.set_title('Chart 05: Prior Failures vs Final Grade')
save_chart(fig, '05_box_failures_g3')

# %%
# Chart 06: Mother Education Level vs Final Grade - Analyzes the positive correlation between maternal educational attainment and student scores.
medu_map = {0: 'None', 1: 'Primary', 2: '5th-9th', 3: 'Secondary', 4: 'Higher'}
df['medu_label'] = df['Medu'].map(medu_map)
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=df, x='medu_label', y='G3', hue='subject', order=['None', 'Primary', '5th-9th', 'Secondary', 'Higher'], ax=ax)
ax.set_title("Chart 06: Final Grade by Mother's Education (Medu)")
save_chart(fig, '06_box_medu_g3')

# %%
# Chart 07: Mean Academic Grade by Mother's Occupation - Compares average grades based on the mother's professional field.
fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(data=df, x='Mjob', y='G3', hue='subject', errorbar=None, ax=ax)
ax.set_title("Chart 07: Mean Academic Grade by Mother's Occupation")
save_chart(fig, '07_bar_mjob_g3')

# %%
# Chart 08: Math Pass Rate by Support Type - Evaluates pass rates across remedial institutional support and private tutoring.
fig, ax = plt.subplots(figsize=(7, 4))
supp = mat.groupby(['schoolsup', 'paid'])['passed'].mean().reset_index()
supp['label'] = 'Support: ' + supp['schoolsup'] + ' | Paid: ' + supp['paid']
sns.barplot(data=supp, x='label', y='passed', ax=ax)
ax.set_title('Chart 08: Math Pass Rate (% >= 10) by Support')
save_chart(fig, '08_bar_support_pass_rate')

# %%
# Chart 09: Mean Grade by Gender Across Subjects - Highlights male performance advantage in Math versus female performance advantage in Portuguese.
fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(data=df, x='subject', y='G3', hue='sex', errorbar=None, ax=ax)
ax.set_title('Chart 09: Mean Grade by Gender Across Subjects')
save_chart(fig, '09_bar_gender_subject')

# %%
# Chart 10: Reported Quality of Family Relationships - Displays student ratings of home family relationship quality (1=Very Bad to 5=Excellent).
famrel_map = {1: 'Very Bad', 2: 'Bad', 3: 'Fair', 4: 'Good', 5: 'Excellent'}
df['famrel_label'] = df['famrel'].map(famrel_map)
fig, ax = plt.subplots(figsize=(7, 4))
sns.countplot(data=df, x='famrel_label', hue='subject', order=['Very Bad', 'Bad', 'Fair', 'Good', 'Excellent'], ax=ax)
ax.set_title('Chart 10: Reported Quality of Family Relationships')
save_chart(fig, '10_count_famrel')

# %%
# Chart 11: Higher Education Ambition vs Extracurriculars - Compares university aspirations between students with and without club activities.
fig, ax = plt.subplots(figsize=(7, 4))
sns.countplot(data=df, x='higher', hue='activities', ax=ax)
ax.set_title('Chart 11: Higher Education Ambition vs Extracurriculars')
save_chart(fig, '11_count_higher_activities')

# %%
# Chart 12: Term 1 Grade vs Final Grade in Math - Shows strong positive linear correlation (r = 0.80) anchoring year-end performance early.
fig, ax = plt.subplots(figsize=(7, 4))
sns.regplot(data=mat, x='G1', y='G3', ax=ax)
ax.set_title('Chart 12: Term 1 Grade vs Final Grade in Math')
save_chart(fig, '12_scatter_g1_g3')

# %%
# Chart 13: Absences vs Final Grade - Separates active test-takers from zero-grade dropouts to reveal the true attendance penalty.
fig, ax = plt.subplots(figsize=(7, 4))
sns.scatterplot(data=mat, x='absences', y='G3', hue='is_zero', palette=['#2b5c8f', 'crimson'], ax=ax)
ax.set_title('Chart 13: Absences vs Final Grade (Red = Zero Dropouts)')
save_chart(fig, '13_scatter_absences_g3')

# %%
# Chart 14: Correlation Matrix of Key Metrics (Math) - Presents Pearson correlation coefficients among academic, behavioral, and demographic features.
fig, ax = plt.subplots(figsize=(8, 6))
cols = ['age', 'Medu', 'Fedu', 'studytime', 'failures', 'absences', 'G1', 'G2', 'G3']
sns.heatmap(mat[cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax)
ax.set_title('Chart 14: Correlation Matrix of Key Metrics (Math)')
save_chart(fig, '14_heatmap_correlation')

# %%
# Chart 15: Longitudinal Grade Trajectory Across Terms - Tracks the trimester progression trend across Term 1, Term 2, and Final Grade.
fig, ax = plt.subplots(figsize=(7, 4))
grades_trend = mat[['G1', 'G2', 'G3']].mean()
ax.plot(grades_trend.index, grades_trend.values, marker='o', linewidth=2, color='#2b5c8f')
ax.set_title('Chart 15: Longitudinal Grade Trajectory Across Terms')
ax.set_ylabel('Mean Grade')
save_chart(fig, '15_trajectory_terms')

# %%
# Chart 16: Mean Grade Matrix: Mother's vs Father's Education - Heatmap showing combined parental education levels and their joint impact on grades.
fig, ax = plt.subplots(figsize=(7, 5))
grid = df.groupby(['Medu', 'Fedu'])['G3'].mean().unstack()
sns.heatmap(grid, annot=True, fmt='.1f', cmap='YlGnBu', ax=ax)
ax.invert_yaxis()
ax.set_title("Chart 16: Mean Grade Matrix: Mother's vs Father's Education")
save_chart(fig, '16_custom_parent_edu_grid')

# %%
# Chart 17: Grade Trajectory Shift from Term 1 to Final (Math) - Histogram showing student improvement or decline (G3 minus G1).
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(mat['delta_G'], bins=15, kde=True, ax=ax)
ax.axvline(0, color='black', linestyle='--', label='No Change')
ax.set_title('Chart 17: Grade Trajectory Shift from Term 1 to Final (Math)')
ax.legend()
save_chart(fig, '17_custom_delta_grades')

print("Execution complete: All 17 charts saved to the 'charts/' directory.")