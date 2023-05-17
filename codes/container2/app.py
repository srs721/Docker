import os
import json
import requests
import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum')
def sum():
    try:

        total = 0
        filename = request.args.get('file')   
        product = request.args.get('product')

        if not os.path:
            return jsonify({'file': filename, 'error': 'File not found.'}), 404  

        json_data = make_json('../usr/src/vol//{}'.format(filename))
        json_data = json.loads(json_data)

        for data in json_data:  
            if(data['product'] == product):
                total = total + int(data['amount'])

        return jsonify({'file': filename, 'sum': total}), 200
        
    except csv.Error:
        jsonify({'file': filename, 'error': 'Input file not in CSV format'}), 404

    except FileNotFoundError:
        return jsonify({'file': filename, 'error': 'File not found.'}), 404
    

def make_json(csvFilePath):

    csv_file = open(csvFilePath, 'r')
    csv_reader = csv.reader(csv_file)
    field_names = next(csv_reader)

    data = []
    for row in csv_reader:
        data.append(dict(zip(field_names,row)))
    json_data = json.dumps(data)
    csv_file.close()
    return json_data
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 7000, debug=True)