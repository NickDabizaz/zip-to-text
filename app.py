from flask import Flask, request, jsonify, render_template
import zipfile
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if not file.filename.endswith('.zip'):
        return "Please upload a .zip file", 400

    # Process the zip file in memory
    zip_stream = io.BytesIO(file.read())
    with zipfile.ZipFile(zip_stream, 'r') as zip_ref:
        files = [
            {"filename": file_info.filename, "is_dir": file_info.is_dir()}
            for file_info in zip_ref.infolist()
            if not file_info.is_dir()
        ]

    return jsonify(files)

@app.route('/process', methods=['POST'])
def process_files():
    selected_files = request.form.getlist('selected_files[]')
    zip_stream = io.BytesIO(request.files['zip_file'].read())

    output_content = []
    with zipfile.ZipFile(zip_stream, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename in selected_files:
                with zip_ref.open(file_info) as f:
                    file_content = f.read().decode('utf-8', errors='ignore')
                    output_content.append(
                        f"{file_info.filename}\n```\n{file_content}\n```\n\n"
                    )

    return "\n".join(output_content)

if __name__ == '__main__':
    app.run(debug=True)
