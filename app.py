from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    # Mengambil data JSON yang dikirim oleh ESP32
    data = request.get_json()
    print(f"Data received: {data}")
    
    # Mengembalikan respon sukses
    return jsonify({"status": "Data received successfully!"})

if __name__ == '__main__':
    # Flask akan mendengarkan semua koneksi di jaringan lokal, pastikan port 5000 terbuka
    app.run(debug=True, host='0.0.0.0', port=5000)
