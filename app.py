from flask import Flask, render_template, request
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

TENOR_API_KEY = os.getenv("CIKSZWLE8R9M")

#defines the app variable
app = Flask(__name__)
#this function asks for the query then searches the tenor api for most popular gifs that fit the key 
@app.route('/')
def index():
    #some variables that need to be declared, this includes the api key that allows us to call the tenor api, the limit of gifs and the search query
    apikey = "CIKSZWLE8R9M"
    lmt = 9
    query = request.args.get('query')
    #parameters in a dictionary so we can call it in requests
    params = {
        "q": query,
        "key": apikey, 
        "limit": lmt
        }
    #this requests the tenor api and inputs the parameters so we can get out what we searched for.
    r = requests.get("https://api.tenor.com/v1/search", params)
    #this loads the gifs data
    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    #returns this function to index.html and the variable gifs=gifs
    return render_template('index.html', gifs = gifs)
#this function displays the trending gifs on tenor
@app.route('/trending')
def trending():
    #just re-defining the variables for this function, because I dont want them global
    apikey = "CIKSZWLE8R9M"
    lmt = 9
    #paramaters required for the tenor api
    params = {
        "key": apikey, 
        "limit": lmt
        }
    #get the top 9 trending GIFs
    r = requests.get("https://api.tenor.com/v1/trending", params)
    #loads the gifs
    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    #once again, returns this function to index.html and gifs
    return render_template('index.html', gifs = gifs)

@app.route('/random')
def random():
    apikey = "CIKSZWLE8R9M"
    lmt = 9

    params = {
        "key": apikey, 
        "limit": lmt
        }

    # get the top 10 trending GIFs - using the default locale of en_US
    r = requests.get("https://api.tenor.com</v1/random", params)

    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None

    return render_template('index.html', gifs = gifs)

#declares entry point
if __name__ == '__main__':
    app.run(debug=True)