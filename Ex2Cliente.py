import socket
import threading

# Função para enviar mensagens para o servidor
def send_messages(client_socket):
    try:
        while True:
            # Envia mensagem para o servidor
            message = input("Você: ")
            client_socket.send(message.encode('utf-8'))

            # Verifica se o cliente quer encerrar a conversa
            if message == "QUIT":
                break
    except Exception as e:
        print(f"Erro: {str(e)}")

# Função para receber mensagens do servidor
def receive_messages(client_socket):
    try:
        while True:
            # Recebe a resposta do servidor
            reply = client_socket.recv(1024).decode('utf-8')
            if not reply:
                break
            print(f"Servidor: {reply}")

            # Verifica se o cliente quer encerrar a conversa
            if reply == "QUIT":
                break
    except Exception as e:
        print(f"Erro: {str(e)}")

# Configurações do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 32154       # Porta do servidor

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Inicia threads para enviar e receber mensagens
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
send_thread.start()
receive_thread.start()

# Aguarda as threads terminarem
send_thread.join()
receive_thread.join()

# Fecha o socket do cliente
client_socket.close()
