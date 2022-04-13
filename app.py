# PDF Miner tutorial in README
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage

# NLTK tutorial in README
import os 
import nltk
from nltk.tokenize import word_tokenize, blankline_tokenize
from nltk.corpus import stopwords
# punction will be used to filter out numerous word/characters
import re 
punctuation = re.compile(r'[•%-.?!,:;()$`|0-9+*’™\']')

# This allows formatted objects in prints, and to write json
import pprint
import json

# attempt to upload file again
# CAMSCANNER CODE START
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader, PdfFileWriter

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
# ALLOWED_EXTENSIONS = {'pdf', 'txt'}
ALLOWED_EXTENSIONS = {'pdf'} #my edit attempt

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

# function checks the filename for allowed file extension
# if the file type is supported, function returns True
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            get_pdf_file_content(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')


def process_file(path, filename):
    remove_watermark(path, filename)


def remove_watermark(path, filename):
    input_file = PdfFileReader(open(path, 'rb'))
    output = PdfFileWriter()
    for page_number in range(input_file.getNumPages()):
        page = input_file.getPage(page_number)
        page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 20)
        output.addPage(page)
    output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
    output.write(output_stream)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# CANSCANNER CODE END




# All from the PDF Miner tutorial - this function takes the path to pdf file as an argument, and returns the string version of the pdf.
def get_pdf_file_content(path_to_pdf):

    resource_manager = PDFResourceManager(caching=True)

    out_text = StringIO()

    laParams = LAParams()

    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)

    fp = open(path_to_pdf, 'rb')

    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()

    fp.close()
    text_converter.close()
    out_text.close()

    return text






# Samples worked!!! - Instructions in README for how to create a pdf of your own in Google Docs
# path_to_pdf = "./assets/JobRec.pdf"
# path_to_pdf = "./assets/LinkedInSoftEng.pdf"
path_to_pdf = "./assets/BakeryPackager.pdf"

# Create a variable that contains the value of the pdf-turned-to-string
pdf_text = get_pdf_file_content(path_to_pdf)

# Tokenize is covered in the NLTK tutorial. I forget what it does, but in general it splits up every word into a list item/ element that is a string.
pdf_tokens = word_tokenize(pdf_text)

# For each string element in the list, if any indexes fit the regex words, remove/don't include that characters (bullet points, %, ,, ...);
post_punctuation = []
for words in pdf_tokens:
    word = punctuation.sub("", words)
    # Don't keep it if there aren't any letters in it at all
    if len(word)>0:
        post_punctuation.append(word)

# Each word in the job description is aligned with an appropriate POS (parts of speech).
pos_jobrec = []
for token in post_punctuation:
    pos_jobrec.append(nltk.pos_tag([token]))

# Instead of a list containing nested lists of tuples, unpack so that one list contains every tuple but with no surrounding individual lists.
tuple_extractor = []
for list_tuple in pos_jobrec:
    tuple_extractor.append(list_tuple[0])

# Reverse tuples so POS appear first, almost like a K:V pair
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup      
tuples_POS_first = []
for tuple in tuple_extractor:
    tuples_POS_first.append(Reverse(tuple))

# Create a list of POS elements then make it unique w/ set()
unique_POS_list = []
for POS in tuples_POS_first:
    unique_POS_list.append(POS[0])
unique_POS_list = list(set(unique_POS_list))

# Now all unique POS keys are stored in a dictionary/object
accordion_dict = {}
for POS in unique_POS_list:
    accordion_dict[POS] = []

# This is a dictionary of POS lists that should be cleaned
for words in tuples_POS_first:
    accordion_dict[words[0]] += [words[1]]

# for each list in the dict, lowercase each str in that list
for key, value in accordion_dict.items():
    for i in range(len(value)):
        value[i] = value[i].lower()

# Capitalization differs so there are still repeats
filtered_accordion = {}
for key, value in accordion_dict.items():
    filtered_accordion[key] = list(set(value))

pprint.pprint(filtered_accordion)

out_file = open("accordion.json", "w")
json.dump(filtered_accordion, out_file, indent = 6)
out_file.close()