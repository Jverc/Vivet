# https://www.youtube.com/watch?v=3HuYr6G2Z28 (min 17:00)
# https://www.youtube.com/watch?v=oVr6unKZbg4
# https://stackoverflow.com/questions/30011170/flask-application-how-to-link-a-javascript-file-to-website/30011819



from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    return render_template("search_main.html")

@app.route('/search_results', methods=["POST"])
def search_results():
    return render_template(("search_results.html"))

# @app.route('/google')
# def search():
#     return render_template("/google-maps-nearby-search-js/work/index.html")

app.run(debug=True, port=8000, host='0.0.0.0')