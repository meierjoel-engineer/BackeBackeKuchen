import socket

# Server IP and Port
HOST = '192.168.241.218'  # Listen on all available interfaces
PORT = 65432              # Port to listen on

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)  # Allow 1 connection at a time
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()

        try:
            with open('received_data.txt', 'a') as file:
                while True:
                    data = conn.recv(1024)  # Buffer size is 1024 bytes
                    if not data:
                        break
                    decoded_data = data.decode('utf-8')
                    print(f"Received: {decoded_data}")
                    file.write(decoded_data + '\n')
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()


if __name__ == '__main__':
    start_server()
#esptool --chip esp32c3 --port COM12 erase_flash
#esptool --chip esp32c3 --port COM12 --baud 460800 write_flash -z 0x0 C:\GitRepos\BackeBackeKuchen\bin\ESP32_GENERIC_C3-20241025-v1.24.0.bin
#ampy --port COM12 put C:\GitRepos\BackeBackeKuchen\ESP\main.py