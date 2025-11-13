from flask import Flask, jsonify, send_file
import requests
import os

app = Flask(__name__)

# Configurações do Airtable — obtidas de variáveis de ambiente no Vercel
AIRTABLE_TOKEN = os.environ.get("patptp4U8kZ3kYgNO")
BASE_ID = os.environ.get("app1avrro5zomTG6o")
TABLE_NAME = os.environ.get("CARGOBLUE - PROGRAMAÇÃO STATUS ESPELHAMENTO")

@app.route('/')
def home():
    return send_file("02_index.html")

@app.route('/dados')
def dados():
    headers = {"Authorization": f"Bearer {AIRTABLE_TOKEN}"}
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    r = requests.get(url, headers=headers)
    return jsonify(r.json())

# No Vercel, não precisa app.run()
if __name__ == '__main__':
    app.run(debug=True)