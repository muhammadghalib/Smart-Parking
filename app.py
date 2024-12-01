from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()  # Mengambil data JSON yang dikirim oleh ESP32
    print(f"Data received: {data}")
    return jsonify({"status": "Data received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
