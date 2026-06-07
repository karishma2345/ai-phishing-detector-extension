from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']

    print("Received URL:", url)

    # Dummy logic (you can replace with ML)
    if "youtube" in url:
        result = "SAFE"
    else:
        result = "PHISHING"

    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)