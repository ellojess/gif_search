from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    # parameters
    apikey = "CIKSZWLE8R9M" # test value
    lmt = 10

    # TODO: Extract query term from url
    query = request.args.get('query')

    #out test search
    search_term = "excited"



# TODO: Make 'params' dict with query term and API key
params = {
    "q": query_term,
    "Key": "CIKSZWLE8R9M"
    "lmt": 10
}
response = requests.get(
    'https://api.tenor.com/v1/search',
    params=params)

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        f"{params.get('link')}search?q=%s&key=%s&limit=%s" % (params.get('query'), params.get('apikey'), lmt))

    # TODO: Get the first 10 results from the search results
    # https://tenor.com/gifapi/documentation#endpoints-search
    r = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        print top_8gifs
        # move on 
    else:
        top_8gifs = None
        # handle error
    # continue a similar pattern until the user makes a selection or starts a new search.

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
