import socket

import mproto


sock = socket.socket()
sock.connect(('localhost', 7777))

mproto.sendmsg(sock, b'{"type": "say", "data": "hello here?"}')
print(mproto.recvmsg(sock))
