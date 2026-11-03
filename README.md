# Gold Coast GP Intelligence Tool

### AI-Powered Web Scraping & Data Intelligence Platform

A Python-based data intelligence project designed to collect, clean, organise and analyse publicly available General Practitioner (GP) information across the Gold Coast region of Australia.

The project combines web scraping, data processing, AI-assisted summarisation and interactive visualisation to transform publicly available directory information into structured and accessible data.

<p align="left">
  <a href="https://gold-coast-gp-intelligence.streamlit.app/"><strong>🚀 Live Dashboard</strong></a> ·
  <a href="https://github.com/tannukri01/gold-coast-gp-intelligence"><strong>💻 GitHub Repository</strong></a>
</p>

---

## Overview

The Gold Coast GP Intelligence Tool demonstrates an end-to-end data processing workflow, from collecting publicly available information to presenting structured results through an interactive Streamlit dashboard.

It focuses on making directory information easier to explore, filter and understand through Python automation and AI-assisted text processing.

## Key Features

- **Automated Web Scraping:** Collect publicly available GP and medical practice information using Python, Requests and BeautifulSoup.
- **Data Cleaning & Standardisation:** Process inconsistent records and organise doctor names, specialties and practice information using Pandas.
- **AI-Assisted Summarisation:** Generate concise and consistent summaries using AI tools.
- **Interactive Dashboard:** Explore structured information through a Streamlit-powered interface.
- **Structured Data Management:** Maintain separate raw and processed datasets.
- **Data Exploration:** Make directory information easier to search, review and analyse.

## Live Application

**Explore the deployed dashboard:**

https://gold-coast-gp-intelligence.streamlit.app/

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Scraping | BeautifulSoup, Requests |
| Data Processing | Pandas |
| Dashboard | Streamlit |
| AI Assistance | ChatGPT, Claude, Gemini |
| Data Storage | CSV / Structured Files |
| Version Control | Git, GitHub |

## Project Architecture

```text
Gold-Coast-GP-Intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│
├── app/
│   └── app.py
│
├── prompts/
│
├── requirements.txt
└── README.md
```

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/tannukri01/gold-coast-gp-intelligence.git

cd gold-coast-gp-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app/app.py
```

The application will be available locally at:

`http://localhost:8501`

## AI Implementation

AI-assisted workflows were used to support:

- Project planning and architecture design.
- Data cleaning and standardisation.
- Consistent professional text summarisation.
- Prompt engineering and refinement.
- Dashboard layout and usability improvements.

Project-related prompts and iterations are maintained in the `prompts/` directory.

AI-generated summaries should always be reviewed against their original source information.

## Data Processing Workflow

1. Collect publicly available directory information.
2. Extract relevant fields using web scraping.
3. Clean and standardise the collected records.
4. Organise information into structured datasets.
5. Apply AI-assisted summarisation where appropriate.
6. Present the processed information through the interactive dashboard.

## Responsible Data Handling

- Respect website terms of service and access policies.
- Use publicly available information responsibly.
- Preserve source references wherever possible.
- Verify AI-generated summaries against original information.
- Avoid presenting incomplete or unverified information as fact.
- Treat directory information as potentially outdated.

## Skills Demonstrated

Python Programming · Web Scraping · Data Extraction · Data Cleaning · Data Processing · AI-Assisted Automation · Prompt Engineering · Streamlit · Dashboard Development · Data Intelligence

## Future Improvements

- Automated data refresh and monitoring.
- Enhanced search and filtering capabilities.
- Improved data validation and duplicate detection.
- Advanced analytics and visual reporting.
- Better data freshness tracking.

## Disclaimer

This project is developed for educational, research and data-intelligence purposes. It is not a medical recommendation or healthcare service. Information may be incomplete or outdated and should be independently verified with the relevant medical practice.

---

## Author

**Tannu Kumari**

Python Developer | Web Scraping | AI & Automation | Data Intelligence

[GitHub](https://github.com/tannukri01) · [LinkedIn](https://linkedin.com/in/tannukumariofficial)

