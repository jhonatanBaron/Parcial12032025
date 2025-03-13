from flask import Flask, jsonify
from services.extract import extract_data
from services.transform import transform_data
from services.load import load_data

app = Flask(__name__)

@app.route('/api/extract', methods=['GET'])
def extract():
    data = extract_data()
    return jsonify(data)

@app.route('/api/transform', methods=['GET'])
def transform():
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    return jsonify(transformed_data)

@app.route('/api/load', methods=['POST'])
def load():
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)
    return jsonify({"message": "Data loaded successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
