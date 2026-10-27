import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/gold_coast_gps_clean.csv")

# Summaries from AI
summaries = {
    "Dr Mayur Raniga": "Specialist General Practitioner at Homeworld Helensvale Medical Centre in Gold Coast Australia.",
    "Dr Nicholas Teo": "Specialist General Practitioner at Better Veins Clinic in Gold Coast Australia.",
    "Dr Liesbeth Matthijs": "General Practitioner Registrar at Bundall Medical Centre in Gold Coast Australia.",
    "Dr Charles Wu": "Specialist General Practitioner at Robina 7 Day Doctors in Gold Coast Australia.",
    "Dr Leela Devi Avva": "Specialist General Practitioner at Robina 7 Day Doctors in Gold Coast Australia.",
    "Dr Sachin Gupta": "Specialist General Practitioner at Robina 7 Day Doctors in Gold Coast Australia.",
    "Dr Galina Chafikova": "General Practitioner at Robina 7 Day Doctors in Gold Coast Australia.",
    "Dr Ivan Budiarto": "General Practitioner at Robina 7 Day Doctors in Gold Coast Australia.",
    "Dr Pankaj Kothari": "General Practitioner at Gold Coast Medical Precinct in Gold Coast Australia.",
    "Dr Shirlina Das Daniel": "General Practitioner at Gold Coast Medical Precinct in Gold Coast Australia."
}

# Add summary column
df["summary"] = df["name"].map(summaries)

# Save final version
df.to_csv("data/processed/gold_coast_gps_final.csv", index=False)

print("Final data with summaries:")
print(df.to_string())
print("\nSaved to data/processed/gold_coast_gps_final.csv")