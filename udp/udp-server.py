import socket, argparse
MAXBYTES = 65535

def start_server(port, middle_man):
    # AF_INET indicates the internet family of protol
    # SOCK_DGRAM indicated use UDP protocol
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server is listening at port of localhost
    udp_socket.bind(('127.0.0.1', port))
    print 'UDP server {name} listening at 127.0.0.1:{port}'.format(name=udp_socket.getsockname(), port=port)

    while True:
        # At most, we will receive MAXBYTES number of bytes from client, there is difference between TCP and UDP about
        # how to receive packets
        data, client_address = udp_socket.recvfrom(MAXBYTES)
        data = data.decode('ascii')
        print 'Get message "{data}" from {address}'.format(data=data, address=client_address)
        if not middle_man:
            reply = 'Greeting from {server}'.format(server=udp_socket.getsockname())
            print 'reply: ' + reply
            # Use the server to reply
            udp_socket.sendto(reply.encode('ascii'), client_address)
        else:
            # Mock a middle man to reply
            middle_man = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print 'Middle man capture message from client at {address}'.format(address=client_address)
            middle_man.sendto('Middle man replies'.format(address=middle_man.getsockname()), client_address)
            middle_man.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UDP server')
    parser.add_argument('-p', metavar='port number', default=3000, type=int)
    parser.add_argument('-m', help='if demo middle man', action='store_true')
    args = parser.parse_args()
    start_server(args.p, args.m)
