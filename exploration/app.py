from flask import Flask
from flask_cors import CORS
import os


app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

### DO NOT modify this route ###
@app.route('/')
def hello_world():
    return 'server setup'


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))
    
