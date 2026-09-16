# CyberAudit

## Cybersecurity Maturity Assessment Platform

CyberAudit is a web-based platform developed with **Streamlit** to assess and monitor the cybersecurity maturity of Moroccan SMEs.

The platform provides a structured cybersecurity assessment through a questionnaire, automatically calculates maturity scores, identifies areas for improvement, generates personalized recommendations, and allows users to export their results as a PDF report.

> Developed as part of a **PFA internship at CMRPI**.

---

## Features

* 🔐 User authentication
* 🏢 Company information management
* 📋 Structured cybersecurity maturity questionnaire
* 📊 Automatic maturity scoring
* 🔎 Analysis by cybersecurity domain
* 💡 Personalized security recommendations
* 📄 PDF report generation
* 📈 Assessment history and progress tracking
* 📊 Interactive data visualization

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
Recommendations
      ↓
Results & PDF Report
      ↓
Assessment History
```

---

## Assessment Framework

The platform currently includes:

* **25 cybersecurity controls/questions**
* **4 cybersecurity domains**
* **4 maturity levels**
* Automatic global and domain-level scoring
* Recommendations based on identified weaknesses

The assessment is designed to provide SMEs with a clear view of their current cybersecurity maturity and the areas requiring improvement.

---

## Technology Stack

### Frontend / Application

* Python
* Streamlit

### Data & Visualization

* Pandas
* Plotly

### Security

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
├── database/
│   └── cyberaudit.db
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

The application will be available locally at:

```text
http://localhost:8501
```

---

## Main Pages

### Login

Secure authentication system allowing users to access their CyberAudit workspace.

### Questionnaire

Users answer a structured set of cybersecurity questions covering multiple security domains.

### Results

The platform calculates the overall cybersecurity maturity score and provides a detailed analysis of the assessment results.

### History

Users can review previous assessments and track their cybersecurity maturity over time.

### PDF Report

Assessment results and recommendations can be exported into a structured PDF report.

---

## Objective

The objective of CyberAudit is to make cybersecurity maturity assessment more **structured, accessible, and actionable** for SMEs.

Instead of providing only a numerical score, the platform helps identify cybersecurity weaknesses and translates assessment results into practical areas for improvement.

---

## Project Context

This project was developed during a **PFA internship at CMRPI** as part of a project focused on the assessment of cybersecurity maturity among Moroccan SMEs.

The platform implements the assessment workflow, questionnaire, scoring mechanisms, recommendations, authentication, results visualization, and report generation.

---

## Author

**Khadija Sayoukh**

Engineering Student — Digital Transformation & Artificial Intelligence
ENSA Al Hoceïma

---

## Status

🚧 **Project under development**

The platform is continuously being improved with new features, refinements, and assessment capabilities.
