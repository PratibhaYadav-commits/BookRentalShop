from flask import Flask
app = Flask(__name__)

def getApp():
	from BookRentalShop.main.routes import main

	app.register_blueprint(main)

	return app