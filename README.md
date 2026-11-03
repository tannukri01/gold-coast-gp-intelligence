# Gold Coast GP Intelligence Tool

**AI-Powered Web Scraping & Data Intelligence Project**

## Project Overview

The Gold Coast GP Intelligence Tool is a Python-based project designed to collect, clean, and organise publicly available information about General Practitioners (GPs) in the Gold Coast region of Australia.

It demonstrates practical skills in web scraping, data processing, AI-assisted summarisation, and interactive dashboard development.

## Live Demo

🔗 [Click here to view the live dashboard](https://gold-coast-gp-intelligence.streamlit.app/)

## Key Features

- **Web Scraping:** Extract publicly available GP information using Python.
- **Data Cleaning:** Standardise doctor names, specialties, and practice details using Pandas.
- **AI-Powered Summarisation:** Generate concise, professional summaries from provided doctor information.
- **Interactive Dashboard:** Explore and filter structured GP data using Streamlit.
- **Structured Data Management:** Separate raw and processed datasets for easier maintenance.

## Technology Stack

- **Language:** Python
- **Web Scraping:** BeautifulSoup, Requests
- **Data Processing:** Pandas
- **Dashboard:** Streamlit
- **AI Assistance:** ChatGPT, Claude, or Gemini for data standardisation and summarisation

## Project Structure

```text
gold-coast-gp-intelligence/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
├── app/
├── prompts/
├── requirements.txt
└── README.mdInstallation and Setup1. Clone the repositoryBashgit clone https://github.com/tannukri01/gold-coast-gp-intelligence.git
cd gold-coast-gp-intelligence2. Create and activate a virtual environmentBashpython -m venv venv
venv\Scripts\activate3. Install dependenciesBashpip install -r requirements.txt4. Launch the Streamlit dashboardBashstreamlit run app/app.pyAI ImplementationAI tools were used for:
Project planning and structure design
Cleaning and standardising specialty/gender data
Generating consistent professional summaries
Improving dashboard layout
All key prompts and iterations are documented in the prompts/ folder.Responsible Data Handling
Use publicly available information responsibly.
Respect website terms of service and access policies.
Verify generated summaries against their original sources.
Avoid presenting incomplete or unverified information as fact.
Skills DemonstratedPython Programming · Web Scraping · Data Cleaning · Data Processing · AI-Assisted Automation · Prompt Engineering · Streamlit Dashboard DevelopmentDisclaimerThis project is intended for educational and data-intelligence purposes. Information may be incomplete or outdated and should be verified with the relevant medical practice.Developed by Tannu Kumari

Python | Web Scraping | AI & Automation | Data Intelligencetext---

Isse `README.md` file mein **pura replace** kar do, save karo, aur GitHub pe push kar do:

```powershell
git add README.md
git commit -m "Added live demo link to README"
