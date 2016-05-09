import socket, argparse, time

MAXBYTES = 65535

def start_client(interface, port, wait):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((interface, port))
    time.sleep(wait)
    print ('Sending....')
    tcp_socket.sendall('Hello, server!'.encode('ascii'))
    print ('After Sending....')
    reply = tcp_socket.recv(MAXBYTES)
    print ('Get message: ' + reply.decode('ascii'))
    tcp_socket.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP server')
    parser.add_argument('-i', default='127.0.0.1', help='interface to request')
    parser.add_argument('-p', default=3000, type=int, help='port number to request')
    parser.add_argument('-t', default=0, type=int, help='Wait certain period before sending message')
    args = parser.parse_args()
    start_client(args.i, args.p, args.t)
