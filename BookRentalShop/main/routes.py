from flask import Blueprint, render_template, jsonify, request

main = Blueprint('main', __name__)

@main.route("/calculate", methods=['POST'])
def calculate():
	# [{"book_name":"seeta","duration":"2"},{"book_name":"PRATIBHA YADAV","duration":"3"}]
	req = request.json
	grandTotal=0
	bookDetailsList=[]
	for obj in req:
		d = {}
		bname=obj['book_name']
		duration=int(obj['duration'])
		total=totalCharge(duration)
		bookDetails = dict(book_name=bname, duration=duration, total=total)
		bookDetailsList.append(bookDetails)

		grandTotal+=duration


	data = {
	"data":bookDetailsList,
	"grand_total": grandTotal
	}

	return jsonify(data)


@main.route("/")
def home():
    return render_template('index.html')

def totalCharge(duration):
	rate = 1
	return duration*rate;