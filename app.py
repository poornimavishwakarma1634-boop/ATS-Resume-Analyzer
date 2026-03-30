from flask import Flask, render_template, request, Response, jsonify
import os
from parser import ResumeParser

app = Flask (__name__)
app.config['UPLOADS_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOADS_FOLDER'], exist_ok=True)

parser = ResumeParser()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uploads', methods=['POST'])
def uploads():
    file = request.files['resume']

    if not file or file.filename == '':
       return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join(app.config['UPLOADS_FOLDER'], file.filename)
    file.save(filepath)

    data = parser.parse_file(filepath)

    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
