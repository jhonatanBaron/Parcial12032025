def load():
    raw_data = extract_data()
    transformed_data = Transform_data(raw_data)
    load_data(transformed_data)
    return jsonify({"message": "Data loaded successfully"})