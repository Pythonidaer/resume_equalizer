# resume_equalizer

A project aimed to bring advantage to job applications for roles that may screen resumes based off of keywords.

This was unnecessarily difficult:
https://stackoverflow.com/questions/31172719/pip-install-access-denied-on-windows

The first hurdle I've come to struggle greatly with is having a user upload a file (pdf) to a server that can be returned into a file path. I think I need this for the pdf reader to work, but once I get past this hurdle the user can provide their PDF.

There are unforeseen exceptions to special characters. I tried to test for many, such as weird apostraphes, bullet items, etc.

One issue I stopped on tonight was on the values of all the tuples:
https://pythonguides.com/python-dictionary-values-to-list/

The issue is that parts of speech are being organized by acronyms. Every word is in a tuple with a POS. I need to figure out a way that makes separate lists for each acronym.

I'm thinking, maybe it's possible to use each tuple POS value as a key in a dict? That way, if the POS value doesn't exist in the dict, make it a new key. Else, if there is already a POS key present, add that tuple's key into the list for that associated dict key

sample idea:

[
('do', 'VB'),
('display', 'NN'),
('needs', 'NNS)
]

would become:

{
'VB': ['do'],
'NN': ['display', 'pricing'], # etc.
'NNS': ['needs']
}

How users would get to providing a PDF:

- copy your Job Description into a Google Document
- Paste without formatting
- Try to remove any where characters
- (bullet points, list items are fine)
- Download as pdf ---> this would be uploaded

From the demo.py:
https://stackoverflow.com/questions/37934476/print-term-frequency-list-have-distribution

fdist can be used to find the most_common words. Either that or another library method can be used to find the amout for each word after each speech type has been organized

NLTK docs:
https://www.youtube.com/watch?v=X2vAabgKiuM
https://www.nltk.org/data.html
https://pypi.org/project/nltk/
https://www.guru99.com/pos-tagging-chunking-nltk.html#:~:text=POS%20Tagging%20in%20NLTK%20is,each%20word%20of%20the%20sentence.
https://www.nltk.org/book/ch05.html

- This needed to be downloaded
- How would this go about being used on a production server?

PDF Miner:

Explained best by this gentlemen, finally one that works!
https://www.youtube.com/watch?v=1TDS6-hYPDI&t=302s

https://pypi.org/project/pdfminer/
https://www.analyticsvidhya.com/blog/2021/09/pypdf2-library-for-working-with-pdf-files-in-python/

Possible Resources for Flask:
https://www.youtube.com/watch?v=Qr4QMBUPxWo&t=1s
https://prettyprinted.com/

- https://flask.palletsprojects.com/en/1.0.x/patterns/fileuploads/
- Flask uses Jinja and is great for templating web pages
- I want to template in POS collections into an accordion

SQL Alchemy is a Python ORM - was tough to figure out
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

- I don't currently have enough time to dive into this.

Bootstrap

- https://getbootstrap.com/docs/5.1/utilities/float/

pprint for formatted prints to terminal
https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python

Very convenient way to loop over lists by range:
https://www.askpython.com/python/list/iterate-through-list-in-python

I need to combine the PDF Miner tutorial with this one:
https://github.com/viveksb007/camscanner_watermark_remover
https://viveksb007.github.io/2018/04/uploading-processing-downloading-files-in-flask

Bootstrap Accordion:
https://getbootstrap.com/docs/5.1/components/accordion/

Get in the Flask:
https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
