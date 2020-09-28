# https://www.youtube.com/watch?v=3HuYr6G2Z28 (min 17:00)
# https://www.youtube.com/watch?v=oVr6unKZbg4
# https://stackoverflow.com/questions/30011170/flask-application-how-to-link-a-javascript-file-to-website/30011819


#
# from flask import Flask
# from flask import render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template("index.html")
#
# # @app.route('/search')
# # def search():
# #     return render_template("search_main.html")
# #
# # @app.route('/search_results', methods=["POST"])
# # def search_results():
# #     return render_template(("search_results.html"))
#
# # @app.route('/google')
# # def search():
# #     return render_template("/google-maps-nearby-search-js/work/index.html")
#
# app.run(debug=True, port=8000, host='0.0.0.0')

# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)