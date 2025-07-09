from flask import Flask, render_template, request
from markupsafe import Markup
from chatbot import get_response
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form["question"]
    response = get_response(user_question)

    # Convert response to Markdown and mark it safe
    response_html = Markup(markdown.markdown(response))

    return render_template("index.html", question=user_question, answer=response_html)

if __name__ == "__main__":
    app.run(debug=True)
