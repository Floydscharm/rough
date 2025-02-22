import os, sys
from flask import Flask, request, render_template
from pypdf import PdfReader 
import json
from resume_parser import ats_extractor

sys.path.insert(0, os.path.abspath(os.getcwd()))


UPLOAD_PATH = r"D:/FastAPI/app/13014900.pdf"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def ats():
    doc = request.files['pdf_doc']
    doc.save(os.path.join(UPLOAD_PATH, "D:\FastAPI\app\13014900.pdf"))
    doc_path = os.path.join(UPLOAD_PATH, "D:\FastAPI\app\13014900.pdf")
    data = _read_file_from_path(doc_path)
    data = ats_extractor(data)

    # return render_template('index.html', data = json.loads(data))
 
def _read_file_from_path(path):
    reader = PdfReader(path) 
    data = ""

    for page_no in range(len(reader.pages)):
        page = reader.pages[page_no] 
        data += page.extract_text()

    return data 


if __name__ == "__main__":
    app.run(port=8000, debug=True)
