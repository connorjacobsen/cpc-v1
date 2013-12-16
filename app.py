import datetime
from flask import Flask, render_template 
cpc = Flask(__name__)
year = str(datetime.date.today())[:4]

# Views
@cpc.route("/")
def index():
	return render_template("index.html", year=year)

@cpc.route("/brochures")
def brochures():
	return render_template("brochures.html", year=year)

@cpc.route("/cards")
def cards():
	return render_template("cards.html", year=year)

@cpc.route("/newsletters")
def newsletters():
	return render_template("newsletters.html", year=year)

@cpc.route("/stationery")
def stationery():
	return render_template("stationery.html", year=year)

@cpc.route("/catalogs")
def catalogs():
	return render_template("catalogs.html", year=year)

@cpc.route("/folders")
def folders():
	return render_template("folders.html", year=year)

@cpc.route("/custom")
def custom():
	return render_template("custom.html", year=year)

@cpc.route("/contact")
def contact():
	return render_template("contact.html", year=year)

@cpc.route("/map")
def map():
	return render_template("map.html", year=year)

@cpc.route("/ftp")
def ftp():
	return render_template("ftp.html", year=year)

@cpc.route("/products")
def products():
	return render_template("products.html", year=year)


# run the application
if __name__ == "__main__":
	cpc.debug = True
	cpc.run(host="0.0.0.0", port=8000)