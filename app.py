import os
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    not_found = False
    files = os.listdir(UPLOAD_FOLDER)
    # files = [f for f in files if allowed_file(f)]
    files = [f for f in files if allowed_file(f) and not f.startswith('~$')]

    selected_file = request.form.get("excel_file")
    mobile = request.form.get("mobile")

    if request.method == "POST" and selected_file and mobile:
        filepath = os.path.join(UPLOAD_FOLDER, selected_file)
        try:
            df = pd.read_excel(filepath)
            # Search for the value in any column (case-insensitive)
            mask = df.apply(lambda row: row.astype(str).str.contains(mobile, case=False, na=False)).any(axis=1)
            result_df = df[mask]
            if not result_df.empty:
                result = result_df.to_dict(orient="records")  # List of dicts for all matching rows
            else:
                not_found = True
        except Exception as e:
            not_found = True

    return render_template("index.html", files=files, result=result, not_found=not_found, mobile=mobile)

@app.route("/upload", methods=["POST"])
def upload():
    print("Upload endpoint reached")
    error = None
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        error = f"Duplicate file: '{filename}' already exists."
        files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f) and not f.startswith('~$')]
        return render_template("index.html", files=files, error=error)
    file.save(file_path)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)