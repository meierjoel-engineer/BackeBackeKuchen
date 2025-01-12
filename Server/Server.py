import socket
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('DB\data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    adc INTEGER,
                    temperature REAL,
                    timestamp TEXT)''')
    conn.commit()
    conn.close()

def insert_data(adc, temperature):
    conn = sqlite3.connect('DB\data.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO data (adc, temperature, timestamp) VALUES (?, ?, ?)', (adc, temperature, timestamp))
    conn.commit()
    conn.close()

def start_server():
    SERVER_IP = '192.168.80.218'
    SERVER_PORT = 42069
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data}")
            try:
                decoded_data = data.decode('utf-8').strip()
                parts = decoded_data.split(',')
                if len(parts) == 2:
                    adc = int(parts[0])
                    temperature = float(parts[1])
                    insert_data(adc, temperature)
                else:
                    print(f"Malformed data: {decoded_data}")
            except Exception as e:
                print(f"Error: {e}")
        client_socket.close()

if __name__ == '__main__':
    init_db()
    start_server()

#esptool --chip esp32c3 --port COM12 erase_flash
#esptool --chip esp32c3 --port COM12 --baud 460800 write_flash -z 0x0 C:\GitRepos\BackeBackeKuchen\bin\ESP32_GENERIC_C3-20241025-v1.24.0.bin
#ampy --port COM12 put C:\GitRepos\BackeBackeKuchen\ESP\main.py