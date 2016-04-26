import socket, argparse

MAXBYTES = 65535
def start_client(port, data_to_send, safe_mode):
    # AF_INET indicates the internet family of protol
    # SOCK_DGRAM indicated use UDP protocol
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server is listening at port of localhost
    data_to_send = data_to_send.encode('ascii')
    if safe_mode:
        udp_socket.connect(('127.0.0.1', port))
        udp_socket.send(data_to_send)
        data_received = udp_socket.recv(MAXBYTES)
        address = '127.0.0.1'
    else:
        udp_socket.sendto(data_to_send, ('127.0.0.1', port))
        data_received, address = udp_socket.recvfrom(MAXBYTES)
    data_received = data_received.decode('ascii')
    print 'The server {address} reply me with "{data_received}"'.format(address=address, data_received=data_received)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UDP server')
    parser.add_argument('-p', default=3000, type=int)
    parser.add_argument('-s', action='store_true', help='safe mode')
    parser.add_argument('-d', default='I have something to say')
    args = parser.parse_args()
    start_client(args.p, args.d, args.s)
