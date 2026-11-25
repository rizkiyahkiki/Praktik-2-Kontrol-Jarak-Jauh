
import time
import random
import threading
import paho.mqtt.client as mqtt

# ================= KONFIGURASI =================
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "PythonDevice-001"

TOPIC_SUHU = "iot/kelas/sensor/suhu"
TOPIC_LED = "iot/kelas/aktuator/led"
TOPIC_STATUS = "iot/kelas/status/led"

INTERVAL_PUBLISH = 5

# ================= STATE GLOBAL =================
led_state = "OFF"

# ================= CALLBACK MQTT =================
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[MQTT] Terhubung ke broker")
        client.subscribe(TOPIC_LED, qos=0)
        print(f"[MQTT] Subscribe ke topik: {TOPIC_LED}")
    else:
        print(f"[MQTT] Gagal terhubung, kode: {rc}")


def on_message(client, userdata, msg):
    global led_state

    payload = msg.payload.decode("utf-8").strip()
    print(f"[MQTT] Pesan masuk [{msg.topic}]: {payload}")

    if msg.topic == TOPIC_LED:
        if payload in ("ON", "1"):
            led_state = "ON"
            print("[AKTUATOR] LED MENYALA")

        elif payload in ("OFF", "0"):
            led_state = "OFF"
            print("[AKTUATOR] LED MATI")

        else:
            print(f"[AKTUATOR] Perintah tidak dikenal: {payload}")
            return

        client.publish(TOPIC_STATUS, led_state, qos=0)
        print(f"[MQTT] Publish status: {TOPIC_STATUS} -> {led_state}")


def on_disconnect(client, userdata, rc):
    print(f"[MQTT] Terputus (kode: {rc})")


# ================= PEMBACAAN SENSOR =================
def baca_suhu():
    base = 27.0
    noise = random.uniform(-1.5, 1.5)
    return round(base + noise, 2)


# ================= THREAD PUBLISH SENSOR =================
def publish_loop(client):
    while True:
        suhu = baca_suhu()

        if suhu is not None:
            client.publish(TOPIC_SUHU, str(suhu), qos=0)
            print(f"[SENSOR] Publish suhu: {TOPIC_SUHU} -> {suhu} °C")

        time.sleep(INTERVAL_PUBLISH)


# ================= MAIN =================
def main():
    client = mqtt.Client(
        client_id=MQTT_CLIENT_ID,
        protocol=mqtt.MQTTv311
    )

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.reconnect_delay_set(min_delay=1, max_delay=30)

    print(f"[MQTT] Menghubungkan ke {MQTT_BROKER}:{MQTT_PORT}...")

    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
    client.loop_start()

    time.sleep(1)

    publisher = threading.Thread(
        target=publish_loop,
        args=(client,),
        daemon=True
    )
    publisher.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[MAIN] Menghentikan program...")
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
