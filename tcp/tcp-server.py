import socket, argparse, time

MAXBYTES = 65535
def start_server(interface, port, timeout):
    passive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    passive_socket.bind(('127.0.0.1', port))
    passive_socket.listen(1)
    print('Passive socket is listening at ', passive_socket.getsockname())

    while True:
        active_socket, peer_socket_name = passive_socket.accept()
        print('{active_socket_name} connects to {peer_socket_name}'.format(active_socket_name=active_socket.getsockname(), peer_socket_name=peer_socket_name))
        active_socket.setblocking(0)
        begin = time.time()
        msg = ''
        while True:
            if time.time() - begin > timeout:
                break
            try:
                temp_data = active_socket.recv(MAXBYTES)
                if temp_data:
                    msg += temp_data.decode('ascii')
                    # Restart the timer if receive data
                    begin = time.time()
                else:
                    time.sleep(0.1)
            except:
                pass
        if msg:
            print ('Got message: ' + msg)
            reply = 'Thanks for your note from {name}'.format(name=active_socket.getsockname())
        else:
            print ('No message from client before timeout')
            reply = 'Sorry, no message from you'
        active_socket.sendall(reply.encode('ascii'))
        active_socket.close()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP server')
    parser.add_argument('-i', default='127.0.0.1', help='interface to bind')
    parser.add_argument('-p', default=3000, type=int, help='port number to listen')
    parser.add_argument('-t', default=1, type=int, help='timeout value before shutdown the connection')
    args = parser.parse_args()
    start_server(args.i, args.p, args.t)
