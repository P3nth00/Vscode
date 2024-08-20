import socket
import threading

def handle_client(conn, addr):
    print(f"Conectado por {addr}")
    while True:
        command = input("Digite um comando para enviar ao cliente (ou 'exit' para sair): ")
        conn.sendall(command.encode())
        if command.lower() == 'exit':
            break
        
        output = conn.recv(4096).decode()
        print(output)
    
    conn.close()

def start_server():
    host = '0.0.0.0'
    port = 2222

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor ouvindo na porta {port}...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
