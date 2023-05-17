import os
import json
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)
 
 
@app.route('/calculate', methods=['POST'])

def calculate():
    data = request.json

    print(data, flush=True)

    if not data or 'file' not in data or not data['file']:
        return jsonify({'file': None, 'error': 'Invalid JSON input.'}), 400

    filename = data.get('file')
    print(filename, flush=True)
    product = data.get('product')

    
    if not os.path.exists('../usr/src/vol/{}'.format(filename)):
        return jsonify({'file': filename, 'error': 'File not found.'}), 404
    
   
    url = f'http://container2:7000/sum?file={filename}&product={product}'
    response = requests.get(url)
    return response.text

