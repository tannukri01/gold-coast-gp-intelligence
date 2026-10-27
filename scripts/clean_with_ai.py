import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/gold_coast_gps_raw.csv")
print("Raw data loaded:")
print(df)
print("\n" + "="*50)

# Function to split specialty and gender
def clean_specialty_gender(text):
    if pd.isna(text):
        return "", ""
    
    text = str(text)
    if "|" in text:
        parts = text.split("|")
        specialty = parts[0].strip()
        gender = parts[1].strip() if len(parts) > 1 else ""
    else:
        specialty = text
        gender = ""
    
    return specialty, gender

# Apply cleaning
df[["specialty", "gender"]] = df["specialty_gender"].apply(
    lambda x: pd.Series(clean_specialty_gender(x))
)

# Drop old column
df = df.drop(columns=["specialty_gender"])

# Reorder columns
df = df[["name", "gender", "specialty", "practice", "source"]]

print("\nCleaned data:")
print(df)

# Save cleaned version
df.to_csv("data/processed/gold_coast_gps_clean.csv", index=False)
print("\nCleaned data saved to data/processed/gold_coast_gps_clean.csv")