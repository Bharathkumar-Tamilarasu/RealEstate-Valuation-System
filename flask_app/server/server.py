from flask import Flask, render_template, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/locations")
def locations():
    response = jsonify({
        'locations' : util.locations_loader(),
        })
    return response

@app.route("/estimate_price",methods=["POST"])
def estimate_price():

    areaSize = float(request.form['areaSize'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':util.price_estimator(location.lower(), bath, bhk, areaSize),
    })
    return response

if __name__ == "__main__":
    print("Starting the Flask App..")
    print("Artifacts Loading - Inprogress...")
    util.artifacts_loader()
    print("Artifacts Loading - Completed...")
    app.run()
    
