import socket
import threading

clientes = set()

def enviar_a_todos(mensaje, cliente_emisor):
    for cliente in list(clientes):
        if cliente != cliente_emisor:
            try:
                cliente.sendall(mensaje)
            except OSError as e:
                print(f"Error al enviar datos: {e}")
                cliente.close()
                clientes.discard(cliente)

def manejar_cliente(conexion, cliente_addr):
    print(f"Cliente conectado: {cliente_addr}")
    clientes.add(conexion)
    conexion.sendall("Conectado al chat.\n".encode('utf-8'))

    while True:
        try:
            data = conexion.recv(1024)
            if not data:
                break
            mensaje = f"[{cliente_addr}]: {data.decode('utf-8')}"
            print(mensaje.strip())
            enviar_a_todos(mensaje.encode('utf-8'), conexion)
        except (ConnectionResetError, socket.error) as e:
            print(f"Error con {cliente_addr}: {e}")
            break
    
    print(f"Cliente {cliente_addr} desconectado")
    clientes.discard(conexion)
    conexion.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 5000))
server.listen(3)
print("Servidor escuchando en puerto 5000...")

try:

    while True:
        conn, addr = server.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True)
        hilo.start()

except OSError:

    print("\nCerrando servidor...")

    # Cerrar todas las conexiones activas
    for c in clientes:
        c.close()

    server.close()
    print("Servidor cerrado correctamente.")