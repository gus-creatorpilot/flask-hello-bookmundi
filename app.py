# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/get_source/', methods=["GET","POST"])
def get_source():
    action = request.args.get("action") 
    if action:
        zapier_result='hey there!'
        data = {
            'subject': 'Your articles are here!',
            'contents': zapier_result
        }

        requests.post('https://hooks.zapier.com/hooks/catch/5743071/uy49cx4/', json=data)
        return 'Sent Zap'
    else:
        return 'No data provided'
    
@app.route('/analyze/', methods=["POST"])
def analyze():
    source=request.form.get("source")
    if source:
        return "Got it"
    else:
        return 'No data provided'
    
    


