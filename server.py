from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return render_template("thankyou.html")
		except:
			return "something went wrong"
	else: 
		return "something went wrong"

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		name = data["name"]
		file = database.write(f"\n{name},{subject},{message},{email}")


def write_to_csv(data):
	with open('database2.csv', mode='a',newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		name = data["name"]
		csv_writer = csv.writer(database2, delimiter =',',quotechar='"',quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,subject,message,email])