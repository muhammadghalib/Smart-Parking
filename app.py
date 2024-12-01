from flask import Flask, request

app = Flask(__name__)

# Menambah batasan ukuran data
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # Maksimum 10 MB

@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()  # Mengambil data JSON yang dikirim
    print(f"Data received: {data}")
    return jsonify({"status": "Data received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
