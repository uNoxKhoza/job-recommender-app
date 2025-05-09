import json

def load_jobs():
    with open('jobs.json', 'r') as file:
        return json.load(file)

def recommend_jobs(user_skills, location=None):
    jobs = load_jobs()
    recommended = []

    for job in jobs:
        skill_match = len(set(user_skills).intersection(set(job['skills'])))
        location_match = location.lower() == job['location'].lower() if location else True

        if skill_match > 0 and location_match:
            recommended.append({**job, "score": skill_match})

    return sorted(recommended, key=lambda x: x["score"], reverse=True)
