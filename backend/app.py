from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
#WORLDTIDES_API_KEY = os.getenv('WORLDTIDES_API_KEY')

@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from Flask!")



@app.route('/api/weather/<lat>/<lon>')
def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/api/tides/<lat>/<lon>')
def get_tides(lat, lon):
    url = f"https://www.worldtides.info/api/v2?heights&lat={lat}&lon={lon}&key={WORLDTIDES_API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)