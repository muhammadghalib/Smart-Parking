import cv2
import serial

# Path gambar
image_path = r"C:\Users\Muhammad Ghalib\Downloads\all off.png"

# Membaca gambar hanya sekali
base_img = cv2.imread(image_path)

# Mendefinisikan koordinat kotak sebagai dictionary
parking_boxes = {
    1: (1151, 37, 1220, 188),
    2: (1008, 36, 1076, 186),
    3: (875, 36, 941, 188),
    4: (737, 36, 805, 189),
    5: (601, 39, 668, 192),
    6: (457, 39, 526, 192),
    7: (324, 39, 391, 192),
    8: (185, 39, 253, 192),
    9: (1152, 244, 1219, 396),
    10: (1018, 244, 1085, 395),
    11: (875, 244, 943, 394),
    12: (737, 244, 804, 395),
    13: (603, 243, 671, 396),
    14: (469, 243, 538, 396),
    15: (326, 243, 393, 395),
    16: (188, 244, 254, 396),
    17: (1150, 472, 1217, 625),
    18: (1018, 472, 1086, 625),
    19: (874, 473, 941, 623),
    20: (736, 472, 802, 623),
    21: (603, 472, 671, 625),
    22: (470, 472, 537, 625),
    23: (326, 472, 395, 624),
    24: (188, 473, 256, 625),
}

# Membuka koneksi serial di port COM3 dengan baud rate 115200
ser = serial.Serial('COM3', 115200, timeout=0.05)

# Menyimpan status kotak parkir
parking_status = {key: False for key in parking_boxes.keys()}  # False berarti kosong, True berarti terisi

# Fungsi untuk memperbarui kotak parkir
def update_parking_display():
    img_copy = base_img.copy()
    for parking_slot, is_terisi in parking_status.items():
        if is_terisi:  # Jika slot terisi, gambar kotak merah
            x1, y1, x2, y2 = parking_boxes[parking_slot]
            cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 0, 255), -1)  # Kotak merah terisi
            cv2.putText(img_copy, str(parking_slot), ((x1 + x2) // 2 - 10, (y1 + y2) // 2 + 10), 
                         cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    return img_copy

# Membaca data dari serial dan menampilkan kotak sesuai status
while True:
    data = ser.readline().decode('utf-8').strip()
    if data:
        try:
            parking_slot, slot_status = data.split()
            parking_slot = int(parking_slot)
            parking_status[parking_slot] = slot_status == "Terisi"
        except (ValueError, KeyError):
            # Abaikan data tidak valid
            continue

    # Memperbarui tampilan hanya jika ada perubahan
    display_img = update_parking_display()
    cv2.imshow('Status Parkir', display_img)

    # Memeriksa jika tombol 'q' ditekan untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Menutup jendela OpenCV setelah keluar dari loop
cv2.destroyAllWindows()
