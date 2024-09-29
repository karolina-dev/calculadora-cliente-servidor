import socket

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 123456789))
server_socket.listen(5)

print("Servidor escuchando en el puerto 123456...")

def calcular(expresion):
    try:
        # Evalúa la expresión matemática
        resultado = eval(expresion)  
        return f"Resultado: {resultado}"
    except Exception as e:
        return f"Error: {str(e)}"

while True:
    client_socket, address = server_socket.accept()
    print(f"Conexión establecida con {address}")

    # Recibir solicitud del cliente
    data = client_socket.recv(1024).decode()
    print(f"Expresión recibida: {data}")

    respuesta = calcular(data)
    client_socket.sendall(respuesta.encode())

    client_socket.close()

