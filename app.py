from flask import Flask, request, render_template, send_file
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
        output_content = []
        for file_info in zip_ref.infolist():
            if file_info.is_dir():
                continue
            with zip_ref.open(file_info) as f:
                file_content = f.read().decode('utf-8', errors='ignore')
                output_content.append(f"{file_info.filename}\n```\n{{{{{file_content}}}}}\n```\n\n")

    # Create the output file in memory
    output_stream = io.BytesIO()
    output_stream.write("\n".join(output_content).encode('utf-8'))
    output_stream.seek(0)

    # Return the file as a downloadable response
    return send_file(
        output_stream,
        as_attachment=True,
        download_name='output.txt',
        mimetype='text/plain'
    )

if __name__ == '__main__':
    app.run(debug=True)
