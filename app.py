from flask import Flask, render_template, abort, jsonify
from gemini_service import is_gemini_configured, generate_ai_quiz

app = Flask(__name__)

topics = [
    "Python Basics", "Machine Learning", "Data Structures",
    "Computer Networks", "Operating Systems", "Database Management Systems",
    "Artificial Intelligence", "Java Programming", "Web Development",
    "Cyber Security",
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        topics=topics,
        gemini_configured=is_gemini_configured(),
    )

@app.route("/topic/<topic_name>")
def topic(topic_name):
    if topic_name not in topics:
        abort(404)
    content = generate_ai_quiz(topic_name)
    return render_template("topic.html", topic=topic_name, content=content)

@app.route("/api/generate-quiz/<topic_name>", methods=["POST"])
def api_generate_quiz(topic_name):
    if topic_name not in topics:
        return jsonify({"success": False, "error": "Unknown topic"}), 404
    data = generate_ai_quiz(topic_name)
    return jsonify({"success": True, "data": data})

if __name__ == "__main__":
    app.run(debug=True)
