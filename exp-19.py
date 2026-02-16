import pandas as pd
import numpy as np
print("PROGRAM STARTED")


df=pd.read_csv('bp.csv')

df["Treatment_Group"] = df["Treatment_Group"].str.strip()
df["BP_Difference"] = df["Systolic_BP"] - df["Diastolic_BP"]

drugA = df[df["Treatment_Group"] == "Drug A"]["BP_Difference"]
placebo = df[df["Treatment_Group"] == "Placebo"]["BP_Difference"]

mean_drug = drugA.mean()
mean_placebo = placebo.mean()

std_drug = drugA.std()
std_placebo = placebo.std()

n_drug = drugA.count()
n_placebo = placebo.count()

se_drug = std_drug / np.sqrt(n_drug)
se_placebo = std_placebo / np.sqrt(n_placebo)

z = 1.96

me_drug = z * se_drug
me_placebo = z * se_placebo

ci_drug = (mean_drug - me_drug, mean_drug + me_drug)
ci_placebo = (mean_placebo - me_placebo, mean_placebo + me_placebo)

print("Drug A Group")
print("Mean BP Difference:", round(mean_drug,2))
print("95% Confidence Interval:", (round(ci_drug[0],2), round(ci_drug[1],2)))

print("\nPlacebo Group")
print("Mean BP Difference:", round(mean_placebo,2))
print("95% Confidence Interval:", (round(ci_placebo[0],2), round(ci_placebo[1],2)))
