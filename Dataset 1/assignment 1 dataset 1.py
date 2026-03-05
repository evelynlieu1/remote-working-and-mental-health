import pandas as pd

# Load dataset
df = pd.read_csv("2021_rws.csv", encoding="latin1")

# Clean column names: strip spaces, replace line breaks with space
df.columns = df.columns.str.strip().str.replace("\n", " ")

# Explore dataset
print("=== First 5 rows of the dataset ===")
print(df.head())

print("\n=== Dataset dimensions (rows, columns) ===")
print(df.shape)

print("\n=== Column names ===")
print(df.columns.tolist())

print("\n=== Missing values per column ===")
print(df.isna().sum())

print("\n=== Data types of each column ===")
print(df.dtypes)

df = df.fillna("Not answered")

if "Response ID" in df.columns:
    before = df.shape[0]
    df = df.drop_duplicates(subset=["Response ID"])
    after = df.shape[0]
    print(f"\nRemoved {before - after} duplicate responses (based on Response ID).")

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype(str).str.strip()

valid_scales = {
    "agreement": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree", "Not answered"],
    "change": ["Improved", "No change", "Worsened", "Not answered"]
}

df.to_csv("2021_rws_cleaned.csv", index=False, encoding="utf-8")
print("\n✅ Data quality check complete.")
print(f"Final dataset shape: {df.shape}")
print("Cleaned dataset saved as '2021_rws_cleaned.csv'")

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("2021_rws_cleaned.csv")


q1 = "How strongly do you agree or disagree with the following statements?   - On days when I work remotely I feel better"
q2 = "How strongly do you agree or disagree with the following statements?   - On days when I work remotely I am more active"
q3 = "How strongly do you agree or disagree with the following statements?   - I feel better on days when I see my colleagues in person"


counts_q1 = df[q1].value_counts()
counts_q2 = df[q2].value_counts()
counts_q3 = df[q3].value_counts()


summary = pd.DataFrame({
    "Feel better remote": counts_q1,
    "More active remote": counts_q2,
    "Better seeing colleagues": counts_q3
}).fillna(0)   # 缺的填0

print(summary)  # 打印表格

# draw grouped bar chart
summary.plot(kind="bar", figsize=(10,6))
plt.title("Comparison of Well-being and Activity (Remote vs In-person)")
plt.xlabel("Survey Responses")
plt.ylabel("Number of Participants")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Questions")
plt.tight_layout()
plt.show()


# === Second graph：Remote Work Barriers ===
import matplotlib.pyplot as plt
import pandas as pd


barrier_questions = [
    "Have the following barriers to remote working improved or worsened for you over the past 6 months?   - My workspace (e.g. suitable chair, lighting, noise levels, facilities)",
    "Have the following barriers to remote working improved or worsened for you over the past 6 months?   - Motivation",
    "Have the following barriers to remote working improved or worsened for you over the past 6 months?   - Difficulty collaborating remotely",
    "Have the following barriers to remote working improved or worsened for you over the past 6 months?   - Feeling left out and/or isolated"
]


labels_map = {
    barrier_questions[0]: "Workspace",
    barrier_questions[1]: "Motivation",
    barrier_questions[2]: "Collaboration",
    barrier_questions[3]: "Feeling_isolated"
}

df_barriers = df[barrier_questions]


all_options = []
for col in barrier_questions:
    for val in df_barriers[col].dropna().unique():
        if val not in all_options:
            all_options.append(val)


counts = {}
for col in barrier_questions:
    counts[col] = df_barriers[col].value_counts(normalize=True) * 100

barrier_summary = pd.DataFrame(counts).reindex(all_options).fillna(0)

print("\n=== Barrier summary (percentage) ===")
print(barrier_summary)

# draw the plot
fig, ax = plt.subplots(figsize=(10, 6))
barrier_summary.T.plot(kind="bar", stacked=True, colormap="Set2", ax=ax)

# title
plt.title("Barriers to Remote Working (Comparison across 4 questions)", fontsize=14, pad=20)
plt.ylabel("Percentage (%)", fontsize=12)
plt.xlabel("Questions", fontsize=12)


ax.set_xticklabels([labels_map.get(label, label) for label in barrier_summary.columns], rotation=0)


plt.legend(title="Response", bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=9)

plt.tight_layout()
plt.show()

