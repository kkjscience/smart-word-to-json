from flask import Flask, render_template, request, jsonify
import os
from smart_parser import parse_docx  # ✅ यह आपका parser होना चाहिए

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    subject = request.form.get("subject", "unknown")
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    json_data = parse_docx(filepath, subject)

    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True)
