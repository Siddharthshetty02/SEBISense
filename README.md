# RegAlert

**AI-powered SEBI Regulatory Alerts & Advisory Platform**

---

## Overview
**RegAlert** is an AI-driven platform that monitors SEBI regulations and circulars, summarizes updates, generates compliance alerts, and answers investor queries. It enhances transparency, investor awareness, and regulatory compliance in the Indian securities market.

---

## Features

- **Regulatory Summarization:** Automatically summarizes SEBI circulars and stock exchange updates using NLP.  
- **Compliance Alerts:** Generates alerts for critical compliance deadlines and investor actions.  
- **Investor Q&A Chatbot:** Answers queries related to SEBI regulations and compliance using AI.  
- **Multi-language Support:** Can be scaled to support multiple languages for retail investors.  
- **Dashboard:** Displays latest circulars, summaries, and alerts for easy access.

---

## Tech Stack

- **Backend:** Python, Flask, SQLite  
- **NLP & AI:** Hugging Face Transformers (summarization, Q&A), NLP preprocessing  
- **Frontend:** Streamlit, HTML/CSS for styling  
- **Database:** SQLite for storing circulars, summaries, and alerts  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/RegAlert.git
cd RegAlert/backend
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Setup the database:

bash
Copy code
python database/db_setup.py
Running the Project
Backend (Flask API)
bash
Copy code
cd backend
python app.py
Runs the backend API on http://localhost:5000

Frontend (Streamlit)
bash
Copy code
cd frontend
streamlit run app.py
Access the frontend dashboard in your browser.

NLP Prototype (optional)
bash
Copy code
python nlp_prototype.py
Test summarization and Q&A pipelines directly.

Folder Structure
kotlin
Copy code
RegAlert/
├── backend/
│   ├── app.py
│   ├── nlp_prototype.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── preprocess.py
│   ├── models/
│   │   ├── summarizer_model.py
│   │   └── chatbot_model.py
│   └── database/
│       └── regalert.db
├── frontend/
│   ├── app.py
│   ├── pages/
│   └── assets/
├── data/
│   └── sample_circulars/
└── README.md
How It Works
Ingests SEBI circulars (from CSV, JSON, or manual entry).

Preprocesses the text using utils/preprocess.py.

Summarizes circulars using Hugging Face Transformers.

Generates alerts for critical compliance deadlines.

Responds to investor queries via a Q&A chatbot.

Stores all information in SQLite for tracking and analytics.

SEBI Regulations Sample
Some important SEBI regulations used for testing:

Prohibition of Insider Trading Regulations, 2015 – Prevents trading based on unpublished price-sensitive information (UPSI).

Listing Obligations & Disclosure Requirements, 2015 – Requires timely disclosure by listed companies.

Mutual Funds Regulations, 1996 – Governs mutual fund operations and disclosure.

Prohibition of Fraudulent & Unfair Trade Practices, 2003 – Targets market manipulation and fraud.

Delisting of Equity Shares Regulations, 2021 – Provides rules for voluntary and compulsory delisting.

Investment Advisers Regulations, 2013 – Regulates investment advisors and portfolio managers.

Contribution
Fork the repository

Create a new branch for your feature

Submit a pull request

License
This project is licensed under the MIT License.