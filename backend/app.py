from flask import Flask, request, jsonify
import requests
import validators
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from textblob import TextBlob

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def check_reputation(url):
    api_key = os.getenv('GOOGLE_SAFE_BROWSING_API_KEY')
    response = requests.post(
        f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}',
        json={"client": {"clientId": "yourcompany", "clientVersion": "1.5.2"},
              "threatInfo": {"threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
                             "platformTypes": ["ANY_PLATFORM"],
                             "threatEntryTypes": ["URL"],
                             "threatEntries": [{"url": url}]}})
    if response.json():
        return 'red', 10  # High risk
    return 'green', 90  # Low risk

def analyze_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity < -0.1:
        return 'red', 30  # Negative sentiment, possible misleading information
    elif polarity > 0.1:
        return 'green', 70  # Positive sentiment, likely safe
    return 'yellow', 50  # Neutral sentiment, moderate risk

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    
    if not validators.url(url):
        return jsonify({'error': 'Invalid URL'}), 400
    
    status, score = check_reputation(url)
    if status == 'green':
        status, score = analyze_content(url)

    return jsonify({'url': url, 'score': score, 'status': status})

if __name__ == '__main__':
    app.run(debug=True)
