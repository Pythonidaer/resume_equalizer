# Resumé Equalizer

_Job Description PDF parser that returns unique keywords organized by Parts Of Speech (POS). Created with Python, Flask, PDF Miner and Natural Language Processing._

[View Deployed Application Here.](https://resumeequalizer.herokuapp.com/)

# Installation

1. Clone repository to your local device
2. `pip install` the requirements.txt dependencies - You may also need to download [nltk](https://www.nltk.org/data.html).
3. May work best in a virtual environment (venv).
4. Test by running app with `python app.py`
5. If you run into any issues, feel free to reach out and I will try to assist via LinkedIn.

# User Story

```
GIVEN a user looking to tailor a resumé and/or cover letter
WHEN I upload a Job Description pdf
THEN I see an accordion component of unique words from the pdf, categorized by Parts Of Speech
WHEN I click on a panel
THEN I see a full list of words relating to that Part Of Speech
WHEN I click the filter icon
THEN I can choose to view only Nouns | Adjectives | Verbs | Miscellaneous / etc.
WHEN I click the red "x" on a panel
THEN that panel gets removed permanently from the page (re-upload a pdf to view again)
WHEN I want to use these words to add to my resumé and/or cover letter
THEN each word available in the accordion panel were words parsed from the PDF I uploaded
```

# How to Use

1. Click the "Choose File" button or drag and drop a Job Description pdf to the "No file chosen" input.
2. Click "Upload".
3. Click a grey panel ("JJ: adjective") to expand and see all the words available in this section.
4. Click the filter icon to choose between Nouns, Adjectives, Verbs and Miscellanous POS.
5. Click the red "x" on any panel to permanently remove it from the page.
6. Expand each tab you like to easily choose from words as you tailor your documents.
7. Please feel free to [Buy Me A Coffee!](https://www.buymeacoffee.com/jonamichahammo)

# Usage

This repo contains a Group Project created by [Jonathan Hammond](https://www.linkedin.com/in/jonamichahammo/) and [Andrew Clarkson](linkedin.com/in/andrewtclarkson/). Special thanks to [Mohammed Ahmed](https://www.linkedin.com/in/mohakc/) who greatly assisted with troubleshooting errors experienced when we first attempted to deploy an app with nltk to Heroku.

Feel free to inspect the code and make it your own. This product utilized:

- Heroku CLI to deploy from the command line
- Bootstrap and custom CSS ([Kevin Powell](https://www.kevinpowell.co/) always saves the day)
- Flask, a Python microframework, and Jinja, an extensible templating engine
- PDF Miner, a Python library that transforms pdfs into string text
- python-dotenv, a Python library that allowed me to access variables from my .env file
- gunicorn, a aPython WSGI HTTP Server, which allowed me to deploy my Heroku application
- NLTK, a platform that allowed me to work with human language data ([The P.O.S. part](https://www.nltk.org/book/ch05.html)).

# Credits

[When I couldn't even pip install](https://stackoverflow.com/questions/31172719/pip-install-access-denied-on-windows)

[Categorizing and Tagging in NLTK](https://www.nltk.org/book/ch05.html)

[I Learned NLTK from this YouTube video!](https://www.youtube.com/watch?v=X2vAabgKiuM)

[This PDF Miner YouTube video is simply amazing](https://www.youtube.com/watch?v=1TDS6-hYPDI&t=302s)

[pprint for formatted prints](https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python)

[Iterating through Python lists](https://www.askpython.com/python/list/iterate-through-list-in-python)

[A useful StackOverflow post](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask)

["Buy Me A Coffee" button by Sayed Rafeeq](https://codepen.io/syedrafeeq/pen/Brjezo)

[That RuntimeWarning error that wasn't an issue](https://doc.scalingo.com/languages/python/nltk)

[Stripe Developers help with dotenv](https://www.youtube.com/watch?v=ecshCQU6X2U)

[More dotenv](https://www.youtube.com/watch?v=ryVzkQAtpKQ)

[Even more dotenv](https://github.com/theskumar/python-dotenv)

[Secret Keys Demystified](https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key)

# Future Ideas

My next project idea for this includes a dashboard. I want to maybe utilize SQL Alchemy to allow for persistent storage of multiple pdfs. I also don't want to strip away duplicates. For example, if a pdf has 7 Python, 3 hardworking and 17 JavaScript keywords, I want to be able to compare that in a pie chart with multiple Job Descriptions to detect trends.

# Additional Features

Would love to make this look like the main Google Search page and not like Bootstrap.

# License

We've chosen an MIT License. Do what you'd like with this material.
