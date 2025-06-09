# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request
app = Flask(__name__)

@app.route('/get_source/', methods=["GET","POST"])
def get_source():
    action = request.args.get("action") 
    if action:
        return 'Hello World!'

if __name__ == '__main__':
    app.run()

