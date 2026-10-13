# Remote Working & Mental Health

**Question:** Do people who work from home more often report worse psychological distress?

DATA1002 group project, University of Sydney. Python (pandas, SciPy, seaborn).

## Data
UK *Understanding Society* COVID-19 study, individual responses (`cb_indresp_w`).
Variables kept: age, sex, weekly hours, work-from-home frequency, and the GHQ-12 distress score (0 to 12, higher = more distress).

## Method
1. Cut the raw file to the 8 relevant columns and renamed them in plain English.
2. Cleaning: 14,811 records, of which 6,187 had a missing field. Dropping those left 8,624 complete records. Duplicates and stray whitespace were also removed.
3. Kept respondents aged 14 to 70 and, following the group's filter, excluded those working 38 to 70 hours a week. This left 6,271 respondents.
4. Compared GHQ-12 scores across four work-from-home groups (Always / Often / Sometimes / Never) with a one-way ANOVA.

## Result
| WFH frequency | n | Mean GHQ-12 | Median |
|---|---|---|---|
| Always | 2,073 | 2.77 | 1 |
| Often | 491 | 2.87 | 1 |
| Sometimes | 605 | 2.54 | 1 |
| Never | 3,102 | 2.64 | 1 |

**No significant difference between groups (p = 0.24).** In this sample, how often someone worked from home was not associated with their distress score.

## Limitations
- GHQ-12 scores are heavily right-skewed (median 1), so ANOVA's normality assumption is shaky. A Kruskal-Wallis test would be a useful check.
- The hours filter removes most full-time workers, so the result applies to the remaining group only.
- Dropping incomplete rows may bias the sample if missingness relates to wellbeing.
- Observational data: no causal claim.
- Survey weights are in the data but were not applied.

## Repository
- `Dataset 3/`: the analysis above (`main (2).ipynb`)
- `Dataset 1/`, `Dataset 2/`: two other datasets the group assessed for the same question
