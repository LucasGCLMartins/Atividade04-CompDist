import socket
import threading

# Função para lidar com mensagens recebidas do cliente
def handle_client(client_socket):
    try:
        while True:
            # Recebe mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Cliente: {message}")

            # Verifica se o cliente quer encerrar a conversa
            if message == "QUIT":
                break
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        # Fecha o socket do cliente
        client_socket.close()

# Função para enviar mensagens para o cliente
def send_message(client_socket, message):
    try:
        client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Erro ao enviar mensagem para o cliente: {str(e)}")

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 32154       # Porta a ser usada

# Criação do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor esperando conexão na porta {PORT}...")

try:
    while True:
        # Aceita a conexão do cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão estabelecida com {client_address}")

        # Inicia uma thread para lidar com o cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

        # Loop para permitir que o servidor envie mensagens ao cliente
        while True:
            server_message = input("Servidor: ")
            if server_message == "QUIT":
                break
            send_message(client_socket, server_message)

except KeyboardInterrupt:
    print("Servidor encerrado pelo usuário.")
finally:
    # Fecha o socket do servidor
    server_socket.close()
