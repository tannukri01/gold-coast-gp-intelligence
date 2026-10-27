import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_gpgc_doctors():
    url = "https://gpgc.com.au/doctors/"
    print("Fetching page...")
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to fetch page. Status code:", response.status_code)
        return []
    
    soup = BeautifulSoup(response.text, "lxml")
    doctors = []

    # Get all h2 (doctor names)
    h2_tags = soup.find_all("h2")
    
    print(f"Found {len(h2_tags)} doctor names")

    for h2 in h2_tags:
        name = h2.get_text(strip=True)
        
        # Next elements after h2
        specialty = ""
        practice = ""
        
        next_elem = h2.find_next("h3")
        if next_elem:
            specialty = next_elem.get_text(strip=True)
            
            next_next = next_elem.find_next("h3")
            if next_next:
                practice = next_next.get_text(strip=True)
        
        doctor = {
            "name": name,
            "specialty_gender": specialty,
            "practice": practice,
            "source": "gpgc.com.au"
        }
        
        doctors.append(doctor)
        print(f"Extracted: {name} | {practice}")

    return doctors

if __name__ == "__main__":
    data = scrape_gpgc_doctors()
    
    print(f"\nTotal doctors extracted: {len(data)}")
    
    # Save to CSV
    if data:
        df = pd.DataFrame(data)
        df.to_csv("data/raw/gold_coast_gps_raw.csv", index=False)
        print("Data saved to data/raw/gold_coast_gps_raw.csv")
        print("\nPreview:")
        print(df.head())