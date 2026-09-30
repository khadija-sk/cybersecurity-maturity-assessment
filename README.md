# CyberAudit

## Cybersecurity Maturity Assessment Platform

CyberAudit is a web-based platform built with **Python and Streamlit** to help Moroccan SMEs assess their cybersecurity maturity through a structured questionnaire.

The platform transforms assessment responses into an overall maturity score, domain-level analysis, targeted recommendations, and a downloadable PDF report.

Developed as part of a **PFA internship at CMRPI**.

---

## Overview

CyberAudit provides SMEs with a structured way to:

* Assess their current cybersecurity maturity
* Identify weaknesses across different cybersecurity domains
* Understand their overall and domain-level maturity
* Receive recommendations based on identified weaknesses
* Track previous assessments
* Generate a PDF report of assessment results

The assessment currently covers **25 cybersecurity controls/questions across 4 cybersecurity domains and 4 maturity levels**.

---

## Key Features

### Authentication

* User registration and login
* Password hashing with bcrypt
* User-specific assessment data

### Cybersecurity Assessment

* Structured questionnaire with 25 controls/questions
* Assessment organized by cybersecurity domain
* Automatic response evaluation
* Global maturity score
* Domain-level scoring

### Analysis & Recommendations

* Identification of cybersecurity weaknesses
* Domain-level analysis
* Personalized recommendations based on assessment results
* Clear maturity-level interpretation

### Dashboard & Reporting

* Interactive results visualization
* Assessment history
* Progress tracking
* PDF report generation

---

## Assessment Workflow

```text
Authentication
      ↓
Company Information
      ↓
Cybersecurity Questionnaire
      ↓
Response Analysis
      ↓
Maturity Scoring
      ↓
Domain Analysis
      ↓
Recommendations
      ↓
Results Dashboard
      ↓
PDF Report
      ↓
Assessment History
```

---

## Assessment Framework

The current assessment includes:

| Component                        | Coverage |
| -------------------------------- | -------: |
| Cybersecurity controls/questions |       25 |
| Cybersecurity domains            |        4 |
| Maturity levels                  |        4 |
| Global maturity score            |      Yes |
| Domain-level analysis            |      Yes |
| Personalized recommendations     |      Yes |
| Assessment history               |      Yes |
| PDF reporting                    |      Yes |

The framework is designed to provide an **indicative assessment of cybersecurity maturity**, helping SMEs identify areas that may require further attention.

---

## Technology Stack

### Application

* Python
* Streamlit

### Data & Visualization

* Pandas
* Plotly

### Authentication & Security

* bcrypt

### Reporting

* ReportLab

### Storage

* SQLite

---

## Project Structure

```text
CyberAudit/
│
├── assets/
│   └── Application assets
│
├── core/
│   ├── auth.py
│   ├── iso_mapping.py
│   ├── pdf_generator.py
│   ├── questions.py
│   ├── recommendations.py
│   ├── scoring.py
│   └── utils.py
│
├── data/
│   ├── questions.csv
│   └── recommendations.csv
│
├── pages/
│   ├── 0_Login.py
│   ├── 2_Questionnaire.py
│   ├── 3_Resultats.py
│   └── 4_historique.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/khadija-sk/cybersecurity-maturity-assessment.git
cd cybersecurity-maturity-assessment
```

### 2. Create a virtual environment

```bash
py -m venv myenv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
myenv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 5. Run the application

```bash
py -m streamlit run app.py
```

The application will then be available at:

```text
http://localhost:8501
```

---

## Application

### Login

Users authenticate to access their CyberAudit workspace.

### Questionnaire

Users provide company information and complete the cybersecurity assessment covering multiple security domains.

### Results

The platform calculates the overall maturity score and provides a detailed breakdown of the assessment results.

### Recommendations

Recommendations are generated according to identified weaknesses and assessment results.

### History

Users can review previous assessments and track their results over time.

### PDF Report

Assessment results and recommendations can be exported as a structured PDF report.

---

## Screenshots


<img width="1366" height="696" alt="image" src="https://github.com/user-attachments/assets/3a562e02-7fe6-4d00-884e-ae5e0fb48917" />
<img width="1366" height="682" alt="image" src="https://github.com/user-attachments/assets/0a038c98-7797-493d-98d2-ab655f459d05" />
<img width="1366" height="668" alt="image" src="https://github.com/user-attachments/assets/5976bb3b-1793-478c-8233-f2b2deed3376" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/7178fc26-df42-456f-94a8-1ac68d5071dc" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ebebb2cc-068d-465e-a144-7a15d0240938" />






## Project Context

CyberAudit was developed during a **PFA internship at CMRPI** as part of a project focused on assessing cybersecurity maturity among Moroccan SMEs.

The project covers the implementation of the assessment workflow, questionnaire, scoring mechanisms, cybersecurity-domain analysis, recommendations, authentication, visualization, assessment history, and PDF reporting.

---

## Objective

The objective of CyberAudit is to make cybersecurity maturity assessment more **structured, accessible, and actionable** for SMEs.

Rather than providing only a numerical score, the platform combines scoring, domain-level analysis, and recommendations to help organizations understand where further cybersecurity improvements may be needed.

---

## Disclaimer

CyberAudit provides an **indicative cybersecurity maturity assessment** and is not a substitute for a professional cybersecurity audit, penetration test, compliance assessment, or certification process.

---

## Author

**Khadija Sayoukh**

Engineering Student — Digital Transformation & Artificial Intelligence
ENSA Al Hoceïma

[LinkedIn](https://www.linkedin.com/in/khadija-sayoukh-1a1a94288)
