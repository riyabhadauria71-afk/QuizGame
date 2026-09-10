

from flask import Flask, render_template, abort

app = Flask(__name__)

topics = [
    "Python Basics",
    "Machine Learning",
    "Data Structures",
    "Computer Networks",
    "Operating Systems",
    "Database Management Systems",
    "Artificial Intelligence",
    "Java Programming",
    "Web Development",
    "Cyber Security"
]

@app.route("/")
def home():
    return render_template("index.html", topics=topics)

@app.route("/topic/<topic_name>")
def topic(topic_name):
    if topic_name not in topics:
        abort(404)
    return render_template("topic.html", topic=topic_name)

if __name__ == "__main__":
    app.run(debug=True)
