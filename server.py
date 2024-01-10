from flask import Flask, render_template, redirect, url_for
from flask import request
from operator import itemgetter
import csv

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as db:
     email, subject, message = itemgetter("email", "subject", "message")(data)
     db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline = '') as csv_db:
        email, subject, message = itemgetter("email", "subject", "message")(data)
        csv_writer = csv.writer(csv_db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form_page():
   if request.method == 'POST':
       try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
       except: 
           return 'data saving error'
   else:
       return 'submit form error'

# @app.route("/about.html")
# def about_page():
#     return render_template('about.html')

# @app.route("/work.html")
# def work_page():
#     return render_template('work.html')

# @app.route("/works.html")
# def works_page():
#     return render_template('works.html')

# @app.route("/contact.html")
# def contact_page():
#     return render_template('contact.html')

# @app.route('/index.html')
# def index_page():
#     return redirect('/')
