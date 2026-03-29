# ATS-Resume-Analyzer
AI-powered ATS Resume Analyzer using NLP (spaCy) and Regex to extract structured data from resumes (PDF/DOCX) with ATS scoring.

## 🔹 Project Overview

Recruiters often receive hundreds of resumes per job posting. Manual screening is slow and error-prone.  
This project builds the core engine of an Applicant Tracking System (ATS), automatically extracting:

- Candidate Name  
- Contact Info (Email, Phone, Links)  
- Education  
- Skills  
- Experience  
- ATS Score  

All data is structured into a clean JSON object.

---

## 🔹 Features

- Upload **PDF** or **DOCX** resumes.  
- Extract information using **Regex** and **Named Entity Recognition (NER)**.  
- Calculate **ATS Score** based on skills match.  
- Clean, formatted JSON output.  
- Web interface with **premium UI** and structured result page.

---

## 🔹 Technologies Used

- **Python 3.11+**  
- **Flask** - Web server  
- **spaCy** - NLP & NER  
- **PyPDF2** - PDF parsing  
- **python-docx** - DOCX parsing  
- **Regex** - Email, phone, links extraction  
- **HTML/CSS** - Frontend interface  

---

## 🔹 Project Structure


Resume Analyzer/
│
├─ app.py # Flask application
├─ parser.py # Parsing engine with NLP, Regex
├─ skills.py # Skills extraction logic
├─ templates/
│ ├─ index.html # Upload form
│ └─ result.html # Extracted data display
├─ static/
│ └─ style.css # CSS styling
├─ uploads/ # Uploaded resumes
├─ screenshots/ # Screenshots (optional)
└─ README.md


---

## 🔹 Installation

1. **Clone the repository**

```bash
git clone https://github.com/poornimavishwakarma1634-boop/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies
pip install -r requirements.txt

If requirements.txt is missing, install manually:

pip install flask spacy PyPDF2 python-docx
python -m spacy download en_core_web_sm
🔹 Usage
Run the Flask app:
python app.py
Open a browser and go to:
http://127.0.0.1:5000
Upload a PDF or DOCX resume.
View the extracted data on the result page.

Example result page:

<!-- Replace with your screenshot -->

🔹 Example Output (JSON)
{
  "ats_score": 80,
  "contact": {
    "name": "POORNIMA VISHWAKARMA",
    "email": "poornimavishwakarma1634@gmail.com",
    "phone": " 9876543210",
    "links": "Not Found"
  },
  "education": ["BCA"],
  "skills": ["Python", "Machine Learning", "HTML", "CSS", "SQL"],
  "experience": ["2 years at XYZ Company"]
}

🔹 License

This project is licensed under the MIT License.

🔹 Contact

Poornima Vishwakarma
Email: poornimavishwakarma1634@gmail.com

GitHub: poornimavishwakarma1634-boop
