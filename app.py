from flask import Flask, render_template, request, flash, redirect
from flask_bootstrap import Bootstrap
from forms import ImageSearch
import requests
import json

DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#Root URL of NASA image API:
url = 'https://images-api.nasa.gov/search'

## Function to search result from form:
def search_result(search):
    data_term = ["q","center","keywords","location","year_start","year_end","media_type","description"]
    params = {}
    for term in data_term:
        if search.data[term] != '':
            params[term] = search.data[term]
    if not params:
        flash('Error: Please enter something to search :((')
        return redirect("/")
    else:
        try:
            req = requests.get(url= url, params= params)
            # Work ok
            if req.status_code == 200:
                req_json = req.json()
                results = access_API(req_json)
                return render_template('result.html', results= results)
            else:
                flash("Error: Missing required paramaters")
                return redirect("/")
        except requests.ConnectionError:
            flash("Error: Connection error")
            return redirect("/")

## Function to access NASA api:
def access_API(json_data):
    results = list()
    if len(json_data['collection']['items']) > 0:
        # Infomation Attribute
        attributes = ['title','keywords','description','center','date_created']
        for item in json_data['collection']['items']:
            result = dict()
            for att in attributes:
                if att in item['data'][0]:
                    result[att] = item['data'][0][att]
                else:
                    result[att] = None
            # Find media type
            result['type'] = item['data'][0]['media_type']

            result['date_created'] = result['date_created'][:10]

            # For audio and video file
            if result['type'] != 'image':
                try:
                    json_file = (requests.get(url= item['href'])).json()
                    for file in json_file:
                        if result['type'] == 'video':
                            if 'orig.mp4' in file:
                                result['media'] = file
                        else:
                            if 'orig.mp3' in file:
                                result['media'] = file
                except Exception as e:
                    print("{} : {}".format (Exception, e))
                
            # For image and video thumbnail:
            if result['type'] != 'audio':
                result['thumbnail'] = item['links'][0]['href']
            results.append(result)    

    return results

@app.route("/", methods= ["GET", "POST"])
def get_info():
    search = ImageSearch(request.form)
    if request.method == "POST":
        return search_result(search)
    return render_template('index.html', form= search)

@app.route("/keywords/", methods= ["GET"])
def keywords():
    if request.method == 'GET':
        params = dict()
        params['keywords'] = request.args.get('kw')
        try:
            req = requests.get(url= url, params= params)
            # Work ok
            if req.status_code == 200:
                req_json = req.json()
                results = access_API(req_json)
                return render_template('result.html', results= results)
        except requests.ConnectionError:
            flash("Error: Connection error. Return to main search page")
            return redirect("/")


@app.route("/query/", methods= ['GET'])
def query():
    if request.method == 'GET':
        params = dict()
        params['q'] = request.args.get('q')
        print(params['q'])
        try:
            req = requests.get(url= url, params= params)
            # Work ok
            if req.status_code == 200:
                req_json = req.json()
                results = access_API(req_json)
                return render_template('result.html', results= results)
        except requests.ConnectionError:
            flash("Error: Connection error. Return to main search page")
            return redirect("/")
