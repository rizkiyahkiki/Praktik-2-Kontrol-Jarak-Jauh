# PRAKTIK 2 – KONTROL JARAK JAUH

## 1. Deskripsi Praktik

Praktik ini membahas penerapan Internet of Things (IoT) untuk melakukan monitoring suhu dan kontrol LED secara jarak jauh menggunakan Python, Mosquitto MQTT Broker, dan Node-RED Dashboard.

## 2. Tujuan Praktik

1. Memahami komunikasi menggunakan protokol MQTT.
2. Menghubungkan Python dengan MQTT Broker.
3. Melakukan monitoring suhu melalui Node-RED Dashboard.
4. Mengontrol LED melalui Dashboard.
5. Menampilkan status LED berdasarkan perintah yang diberikan.

## 3. Alat dan Bahan

1. Laptop dengan sistem operasi Windows 11.
2. Python.
3. Mosquitto MQTT Broker.
4. Node-RED.
5. Library Paho-MQTT.

## 4. Topik MQTT

Topik yang digunakan dalam praktik ini adalah:

- `iot/kelas/sensor/suhu` untuk mengirim data suhu.
- `iot/kelas/aktuator/led` untuk menerima perintah LED.
- `iot/kelas/status/led` untuk mengirim status LED.

## 5. Hasil Praktik

Berdasarkan praktik yang telah dilakukan, program Python berhasil dijalankan dan terhubung dengan Mosquitto MQTT Broker.

Data suhu berhasil dikirimkan secara berkala dan ditampilkan pada Node-RED Dashboard. Selain itu, kontrol LED berhasil dilakukan melalui tombol pada Dashboard dengan perintah ON dan OFF.

Status LED juga berhasil ditampilkan sesuai dengan perintah yang diberikan.

## 6. Kesimpulan

Praktik kontrol jarak jauh menggunakan teknologi Internet of Things (IoT) berhasil dilakukan. Komunikasi antara Python, Mosquitto MQTT Broker, dan Node-RED Dashboard berjalan dengan baik.

Sistem dapat melakukan monitoring suhu serta mengontrol LED secara jarak jauh menggunakan protokol MQTT.

## 7. Dokumentasi

Dokumentasi hasil pengerjaan praktik dilampirkan dalam folder `Screenshot`, yang berisi bukti proses dan hasil pengujian sistem.

