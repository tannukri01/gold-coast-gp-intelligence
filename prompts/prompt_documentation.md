# Prompt Documentation – Gold Coast GP Intelligence Tool

This document contains all the key prompts used during the development of the project, along with the reasoning and iterations.

---

## 1. Initial Project Planning Prompt

**Prompt:**
I need to create a Web Scraping & Data Intelligence project for the Healthcare domain, focused on General Practitioners in Australia (especially Gold Coast). 
The project should demonstrate practical use of AI, good prompt engineering, and a useful final outcome. 
Suggest a clean project structure using Python + Streamlit.

**Why this prompt was used:**
To get a clear and realistic project structure before starting coding.

---

## 2. Data Cleaning Prompt (Specialty & Gender Separation)

**Prompt:**
I have a column called "specialty_gender" with values like:
"Specialist General Practitioner|Male"
"General Practitioner Registrar|Female"

Write a clean Python function that splits this into two separate columns: specialty and gender. Handle missing values properly.

**Iteration:**
First version only split on "|". Later improved to handle cases where "|" might be missing.

---

## 3. AI Summary Generation Prompt (Main Prompt)

**Final Prompt Used:**

You are a professional healthcare data assistant. 

I will give you a list of General Practitioners from Gold Coast, Australia. 
For each doctor, generate a short, professional 1-2 sentence summary.

Format the output exactly like this (CSV style):

name,summary

Rules:
- Keep the summary factual and professional
- Mention specialty and practice
- Do not invent qualifications or experience
- Keep it under 30 words per summary

Here is the data:

Dr Mayur Raniga | Male | Specialist General Practitioner | Homeworld Helensvale Medical Centre
Dr Nicholas Teo | Male | Specialist General Practitioner | Better Veins Clinic
Dr Liesbeth Matthijs | Female | General Practitioner Registrar | Bundall Medical Centre
Dr Charles Wu | Male | Specialist General Practitioner | Robina 7 Day Doctors
Dr Leela Devi Avva | Female | Specialist General Practitioner | Robina 7 Day Doctors
Dr Sachin Gupta | Male | Specialist General Practitioner | Robina 7 Day Doctors
Dr Galina Chafikova | Female | General Practitioner | Robina 7 Day Doctors
Dr Ivan Budiarto | Male | General Practitioner | Robina 7 Day Doctors
Dr Pankaj Kothari | Male | General Practitioner | Gold Coast Medical Precinct
Dr Shirlina Das Daniel | Female | General Practitioner | Gold Coast Medical Precinct

**Why this prompt worked well:**
- Clear role given to AI
- Strict output format (CSV style)
- Explicit rules to avoid hallucination
- Limited word count for consistency

**Earlier weaker version:**
"Write summaries for these doctors"
→ This gave inconsistent and longer outputs. The structured prompt above produced much better results.

---

## 4. Dashboard Improvement Prompt

**Prompt:**
I have a Streamlit dashboard showing Gold Coast GPs. 
Suggest small improvements to make it look more professional and useful without making it complex. 
Keep the code simple.

**Result:**
Added metrics (Total Doctors, Practices, Female Doctors) and sidebar filters.

---

## Summary of Prompt Engineering Approach

- Started with broad planning prompts
- Moved to specific, constrained prompts for data tasks
- Added clear rules to reduce hallucination
- Iterated when output was inconsistent
- Always verified AI output before using it in the final project