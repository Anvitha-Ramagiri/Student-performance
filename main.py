# -----------------------------
# STUDENT PERFORMANCE ANALYSIS
# -----------------------------

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("data/student_data.csv")

# -----------------------------
# DISPLAY DATA
# -----------------------------

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(0, inplace=True)

# -----------------------------
# BASIC ANALYSIS
# -----------------------------

# Average GPA
average_gpa = df['GPA'].mean()

print("\nAVERAGE GPA")
print(round(average_gpa, 2))

# Average Study Time
average_study = df['StudyTimeWeekly'].mean()

print("\nAVERAGE STUDY TIME")
print(round(average_study, 2))

# Average Absences
average_absence = df['Absences'].mean()

print("\nAVERAGE ABSENCES")
print(round(average_absence, 2))

# Top Students
top_students = df.sort_values(
    by='GPA',
    ascending=False
)

print("\nTOP STUDENTS")
print(
    top_students[
        ['StudentID', 'GPA']
    ].head(10)
)

# Grade Class Count
grade_count = df['GradeClass'].value_counts()

print("\nGRADE CLASS DISTRIBUTION")
print(grade_count)

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

df.to_csv(
    "output/cleaned_student_data.csv",
    index=False
)

print("\nCleaned Data Saved Successfully!")

# -----------------------------
# DASHBOARD VISUALIZATION
# -----------------------------

fig, axes = plt.subplots(2, 2, figsize=(10, 6))

# -----------------------------
# 1. GPA DISTRIBUTION
# -----------------------------

df['GPA'].plot(
    kind='hist',
    bins=10,
    ax=axes[0, 0],
    title='GPA Distribution'
)

axes[0, 0].set_xlabel("GPA")
axes[0, 0].set_ylabel("Students")

# -----------------------------
# 2. STUDY TIME VS GPA
# -----------------------------

axes[0, 1].scatter(
    df['StudyTimeWeekly'],
    df['GPA']
)

axes[0, 1].set_title(
    "Study Time vs GPA"
)

axes[0, 1].set_xlabel("Study Time Weekly")
axes[0, 1].set_ylabel("GPA")

# -----------------------------
# 3. ABSENCES VS GPA
# -----------------------------

axes[1, 0].scatter(
    df['Absences'],
    df['GPA']
)

axes[1, 0].set_title(
    "Absences vs GPA"
)

axes[1, 0].set_xlabel("Absences")
axes[1, 0].set_ylabel("GPA")

# -----------------------------
# 4. STUDENT ACTIVITIES
# -----------------------------

activity_data = df[
    ['Sports', 'Music', 'Volunteering']
].sum()

activity_data.plot(
    kind='bar',
    ax=axes[1, 1],
    title='Student Activities'
)

axes[1, 1].set_xlabel("Activities")
axes[1, 1].set_ylabel("Count")

# -----------------------------
# DASHBOARD TITLE
# -----------------------------

fig.suptitle(
    "Student Performance Dashboard",
    fontsize=14,
    fontweight='bold'
)

# -----------------------------
# ADJUST LAYOUT
# -----------------------------

plt.tight_layout()

# -----------------------------
# SAVE DASHBOARD
# -----------------------------

plt.savefig(
    "output/student_dashboard.png",
    dpi=300,
    bbox_inches='tight'
)

# -----------------------------
# SHOW DASHBOARD
# -----------------------------

plt.show()

print("\nPROJECT EXECUTED SUCCESSFULLY!")
print("Dashboard saved inside OUTPUT folder.")
