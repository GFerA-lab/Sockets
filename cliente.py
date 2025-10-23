import socket
import threading

def recibir_mensajes(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            print("\n" + data)
        except (socket.error, ConnectionError):
            print("Desconectado del servidor.")
            break

sktCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sktCliente.connect(('localhost', 5000))

threading.Thread(target=recibir_mensajes, args=(sktCliente,), daemon=True).start()

while True:
    msg = input()
    if msg.lower() == 'salir':
        break
    sktCliente.sendall(msg.encode('utf-8'))

sktCliente.close()