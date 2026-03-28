import csv

def load_skills():
    skills = []
    with open('skills.csv', 'r') as file:
        reader = csv.reader(file)
        for now in reader:
            skills.append(now[0].strip().lower())
    return skills


SKILLS_DB = load_skills()

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills)) if found_skills else ["Not Found"]