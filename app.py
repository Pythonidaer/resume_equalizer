from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
import os 
import nltk
from nltk.tokenize import word_tokenize, blankline_tokenize
from nltk.corpus import stopwords
import re 
punctuation = re.compile(r'[•%-.?!,:;()$`|0-9+*’™\']')


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

# path_to_pdf = "./assets/JobRec.pdf"
# path_to_pdf = "./assets/LinkedInSoftEng.pdf"
path_to_pdf = "./assets/BakeryPackager.pdf"

pdf_text = get_pdf_file_content(path_to_pdf)
print(pdf_text)
print('---------- ---------- -- ---------- ----------')

pdf_tokens = word_tokenize(pdf_text)
print(pdf_tokens)
print('---------- ---------- -- ---------- ----------')

post_punctuation = []
for words in pdf_tokens:
    word = punctuation.sub("", words)
    if len(word)>0:
        post_punctuation.append(word)
# print(post_punctuation)

pos_jobrec = []
for token in post_punctuation:
    pos_jobrec.append(nltk.pos_tag([token]))
    # print(nltk.pos_tag([token]))

# print(pos_jobrec[0])
# print(type(pos_jobrec[0][0]))
# print(pos_jobrec)

tuple_extractor = []
for list_tuple in pos_jobrec:
    tuple_extractor.append(list_tuple[0])
    # print(dict(list_tuple[0]))

print(tuple_extractor)

# for tuple in tuple_extractor:
    # print(dict(tuple))
    # print(tuple)

# dict_converter = dict(tuple_extractor)
# print(dict_converter.values())
# pos_list = dict_converter.values()
# new_value = list(pos_list)
# print(new_value)