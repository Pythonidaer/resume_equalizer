# PDF Miner tutorial in README
from fileinput import filename 
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
# NLTK tutorial in README
import os 
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
# from nltk.tokenize import word_tokenize, blankline_tokenize
# from nltk.corpus import stopwords
# punction will be used to filter out numerous word/characters
import re 
punctuation = re.compile(r'[•%-.?!,:;()$`|0-9+*’™#-@]')
# This allows formatted objects in prints, and to write json
import pprint
import json
# attempt to upload file again
from flask import Flask, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app = Flask(__name__,
static_url_path='',
static_folder='assets',
template_folder='templates')
app.secret_key = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

# dumped all of this into a function to call from flask route
def analyze_data(path_to_pdf):

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

    # Remove duplicate elements in each list
    filtered_accordion = {}
    for key, value in accordion_dict.items():
        filtered_accordion[key] = list(set(value))

    # need to remove $ as character is not allowed in certain html attributes
    if "PRP$" in filtered_accordion:
        filtered_accordion['PRPS'] = filtered_accordion.pop('PRP$')
    return filtered_accordion

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        f = request.files['file']
        secured_file = secure_filename(f.filename)
        if f.filename == '':
            flash('You need to choose a pdf file first!', 'danger')
            return redirect(request.url)
        if not allowed_file(f.filename):
            flash('Sorry! File upload must be .pdf format only.', 'warning')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secured_file))
            return redirect("/analyze/" + secured_file)
    return render_template('index.html') 

@app.route('/analyze/<name>')
def analyze(name):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    analyzed_data = analyze_data(file_path)
    return render_template("output.html", data=analyzed_data)

if __name__ == '__main__':
    from waitress import serve 
    serve(app, host="0.0.0.0", port=8080)