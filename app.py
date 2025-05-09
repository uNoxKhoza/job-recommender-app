from flask import Flask, render_template, request, jsonify
from recommender import recommend_jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    skills = data.get("skills", [])
    location = data.get("location", "")
    results = recommend_jobs(skills, location)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
