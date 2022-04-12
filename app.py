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
print(pdf_text)
print('---------- ---------- -- ---------- ----------')

# Tokenize is covered in the NLTK tutorial. I forget what it does, but in general it splits up every word into a list item/ element that is a string.
pdf_tokens = word_tokenize(pdf_text)
print(pdf_tokens)
print('---------- ---------- -- ---------- ----------')

# For each string element in the list, if any indexes fit the regex words, remove/don't include that characters (bullet points, %, ,, ...);
post_punctuation = []
for words in pdf_tokens:
    word = punctuation.sub("", words)
    # Don't keep it if there aren't any letters in it at all
    if len(word)>0:
        post_punctuation.append(word)
# print(post_punctuation)

# This needs a toLowerCase() equivalent -- should be case sensitive to avoid repeats
# Each word in the job description is aligned with an appropriate POS (parts of speech).
# NOTE: THIS WILL EVENTUALLY HELP USERS SEE "IMPORTANT" WORDS IN THE JOB DESCRIPTION THEY MAY WANT TO USE ON THEIR TAILORED RESUMES
# Note to self: ask recruiters if the ATS system looks or any particular parts of speech (nouns, verbs, etc.)
pos_jobrec = []
for token in post_punctuation:
    pos_jobrec.append(nltk.pos_tag([token]))
    # print(nltk.pos_tag([token]))

# See how data looks
# print(pos_jobrec[0])
# print(type(pos_jobrec[0][0]))
# print(pos_jobrec)

# Instead of a list containing nested lists of tuples, unpack so that one list contains every tuple but with no surrounding individual lists.
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


# TO DO NOTES:
# Turn the tuple[1] into an object key
# When that value already exists, make another (VN, NN, etc.)
# When that POS isn't there yet, add it as another key
# Make it so that each key in a dictionary is the former tuple POS, and every value for the respective keys would be just lists of words that align with that POS
# Loop or prepare to loop into a Boostrap Accordion - this requires knowing how store multiple lists into panels
# Ideally this would also include the quantity of each word (not talking about ands, though am talking about 'experience' and relevant pronouns such as Jinja)

# HOW DOES A USER GET TO POSTING A PDF SO THAT WE CAN RETRIEVE IT AND APPLY CHANGES TO IT?!?!?!?!