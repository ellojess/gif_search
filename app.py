from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    apikey = "CIKSZWLE8R9M"
    lmt = 10
    query = request.args.get('query')
    #parameters in a dictionary so we can call it in requests
    params = {
        "q": query,
        "key": apikey, 
        "limit": lmt
        }
    #This requests the tenor api and inputs the parameters so we can get out what we searched for.
    r = requests.get("https://api.tenor.com/v1/search", params)
    
    if r.status_code == 200:
        gifs = json.loads(r.content)["results"]
    else:
        gifs = None

    return render_template('index.html', gifs = gifs)

if __name__ == '__main__':
    app.run(debug=True)

    # parameters
    ##apikey = "CIKSZWLE8R9M" # test value
    ##lmt = 10
    # TODO: Extract query term from url
    ##query = request.args.get('query')
    #out test search
    ##search_term = "excited"

# TODO: Make 'params' dict with query term and API key
    ##params = {
    ##    "query": query,
    ##    "api_consumer_key": apikey, ###
    ##    "link":'https://api.tenor.com/v1/'
    ##    }

# TODO: Make an API call to Tenor using the 'requests' library
    ##response = requests.get(
    ##'https://api.tenor.com/v1/search',
    ##params=params)

    # TODO: Get the first 10 results from the search results
    # https://tenor.com/gifapi/documentation#endpoints-search
    ##r = requests.get(
    ##"https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    ##if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        ##top_10gifs = json.loads(r.content) #was 8
        ##print(top_10gifs)
        # move on
    ##else:
        ##top_10gifs = None #was 8
        # handle error
    # continue a similar pattern until the user makes a selection or starts a new search.

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    ##return render_template("index.html")