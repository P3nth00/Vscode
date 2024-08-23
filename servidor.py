import socket
import threading
import logging

# Constantes
MAX_CONEXOES = 5
PORTA = 2245
HOST = '0.0.0.0'
BUFFER_SIZE = 4096

# Configuração de log
logging.basicConfig(level=logging.INFO)

def handle_client(conn, addr):
    logging.info(f"Conectado por {addr}")
    try:
        while True:
            command = input("Digite um comando para enviar ao cliente (ou 'exit' para sair): ")
            conn.sendall(command.encode())
            if command.lower() == 'exit':
                break
            
            output = conn.recv(BUFFER_SIZE).decode()
            logging.info(output)
    except Exception as e:
        logging.error(f"Erro ao lidar com cliente: {e}")
    finally:
        conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORTA))
    server_socket.listen(MAX_CONEXOES)

    logging.info(f"Servidor ouvindo na porta {PORTA}...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()