# Loading Developer Libraries
import os
from flask import Flask, request
from apiclient.discovery import build

# Import hte 21 Developer Libraries
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Server side wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Obtain Google Translate API key
service = build('translate', 'v2', developerKey=os.environ.get('GOOGLE_TRANSLATE_API_KEY'))

# Create the 402 payment endpoint
@app.route('/translate')
@payment.required(3000)
def translate():
    """Translate from English to Chinese."""
    print(request.get_data)
    text = request.args.get('text')

    # Send a request to Google's Translate REST API using your API credentials defined above
    ans = service.translations().list(source='en', target='zh-CN', q=text).execute()

    # Return translated text back to user
    return ans['translations'][0]['translatedText']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4004)
