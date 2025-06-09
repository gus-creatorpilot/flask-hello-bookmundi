# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request
import requests
from scrapingbee import ScrapingBeeClient
import re, json
app = Flask(__name__)

def send_zap(data):
    data = {
        'subject': 'Your articles are here!',
        'contents': 'hhh'
    }
    requests.post('https://hooks.zapier.com/hooks/catch/5743071/uy49cx4/', json=data)
    return "Zap sent"

def get_page_source_bee(url):
    client = ScrapingBeeClient(api_key='MCLLUMZPSFJW1KGX9TCFOWV9EED1F7US5CMZALDRAVF02BF0TJDRC6G9LIZ9Q742N3UNDF7VBJQ4GL5C')
    print("Calling client with premium proxy...")
    response = client.get(
    url,
    params={
        'stealth_proxy': 'True'
        #'country_code': 'fr',
        #'wait_browser': 'load'
    })
    return response.content

def extract_clean_json_itinerary(raw_text):
    day_number=1
    raw_text=str(raw_text)
    raw_text = raw_text.replace('\\\\\\', '')
    matches=[]
    while 1:
        itinerary_match = re.compile(fr'"Day {str(day_number)}.*?day_duration', re.DOTALL)
        first_match = itinerary_match.search(raw_text)
        if first_match:
          if "span" not in str(first_match.group()):
            matches.append(first_match.group())
            day_number+=1
        else:
            break
        if day_number > 20:
          break
    return matches

@app.route('/get_source/', methods=["GET","POST"])
def get_source():
    url = request.args.get("url") 
    if url:
        raw=get_page_source_bee(url)
        print("Got source...")
        itinerary_data = extract_clean_json_itinerary(raw)
        print(itinerary_data)
        return "All good"
    else:
        return 'No data provided'
    
if __name__ == "__main__":
    app.run()
    
    


