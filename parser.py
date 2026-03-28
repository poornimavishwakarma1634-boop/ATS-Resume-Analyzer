import PyPDF2
import docx
import re
import spacy
from skills import extract_skills

nlp = spacy.load("en_core_web_sm")

class ResumeParser:

    def parse_file(self, file_path):
        text = self.extract_text(file_path)
        text = self.clean_text(text)
        sections = self.split_sections(text)

        skills = extract_skills(sections.get("skills", ""))

        data = {
            "contact": {
                "name": self.extract_name(text),
                "email": self.extract_email(text),
                "phone": self.extract_phone(text),
                "links": self.extract_links(text),
            },
            "skills": skills,
            "education": self.extract_education(sections.get("education", "")),
            "experience": self.extract_experience(sections.get("experience", "")),
            "ats_score": self.calculate_ats_score(skills)
        }

        return data

    def extract_text(self, file_path):
        if file_path.endswith('.pdf'):
            return self.extract_pdf(file_path)

        elif file_path.endswith('.docx'):
            return self.extract_docx(file_path)
            return ""

    def extract_pdf(self, path):
        text = ""
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                content = page.extract_text()

                if content:
                    text += content
                    return text

    def extract_docx(self, path):
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])

    def clean_text(self, text):
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        return text.strip()

    def split_sections(self, text):
        sections = {
            "experience": "",
            "education": "",
            "skills": "",
            "projects": ""
        }

        current = None

        for line in text.split('\n'):
            line_lower = line.lower()

            if any(k in line_lower for k in ["experience", "work history"]):
                current = "experience"

            elif any(k in line_lower for k in ["education", "academic"]):
                current = "education"

            elif "skill" in line_lower:
                current = "skills"

            elif "project" in line_lower:
                current = "projects"

            if current:
                sections[current] += line + "\n"

        return sections

    def extract_email(self, text):
        emails = re.findall(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+', text)
        return emails[0] if emails else "Not Found"

    def extract_phone(self, text):
        phone = re.findall(r'[6-9]\d{9}', text)
        return phone[0] if phone else "Not Found"

    def extract_name(self, text):
        doc = nlp(text[:1000])
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text.split("\n")[0]
                return "Not Found"

    def extract_links(self, text):
        import re

        links = re.findall(r'(https?://[^\s]+|www\.[^\s]+|linkedin\.com/[^\s]+|github\.com/[^\s]+)', text.lower())
        if links:
            return list(set(links))

        return ["Not Found"]

    def extract_education(self, text):
        keywords = ["b.tech", "m.texh", "bca", "bba", "BSc", "MSc", "PHD", "MBA"]

        text = text.lower()
        found = [k for k in keywords if k in text]
        return list(set(found)) if found else ["Not Found"]

    def extract_experience(self, text):
        matches = re.findall(r'(\d+)\+?\s*(years|year|months|month)', text.lower())

        if matches:
            return [{"duration": f"{m[0]} {m[1]}"} for m in matches]
            return [{"duration": "Not Found"}]

    def calculate_ats_score(self, skills):
        if not skills or skills == ["Not Found"]:
            return 0
        return int (min(len(skills) * 10, 100))