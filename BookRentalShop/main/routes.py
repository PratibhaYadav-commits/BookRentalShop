from flask import Blueprint, render_template, jsonify, request, abort

main = Blueprint('main', __name__)

@main.route("/calculate", methods=['POST'])
def calculate():
	
	req = request.json
	grandTotal=0
	bookDetailsList=[]
	for obj in req:
		d = {}
		bname=obj['book_name']
		duration=int(obj['duration'])
		btype=obj['book_type']
		total=totalCharge(duration, btype)
		bookDetails = dict(book_name=bname, duration=duration, book_type=btype.title(), total=total)
		bookDetailsList.append(bookDetails)

		grandTotal+=total


	data = {
	"data":bookDetailsList,
	"grand_total": grandTotal
	}

	return jsonify(data)


@main.route("/")
def home():
    return render_template('index.html')

def totalCharge(duration, btype):
	regularAndNovelRate = 1.5
	fictionRate = 3
	total=0.0
	
	if btype.lower() == "fiction":
		total = fictionRate * duration
	elif btype.lower() == "regular":
		if duration<=2 :
			total =2
		else : total = ((duration - 2)*1.5) + 2
	elif btype.lower() == "novel" :
		if duration<3 :
			total =4.5
		else : total = ((duration - 2)*1.5) + 4.5
	else : 
		abort(400)

	return total