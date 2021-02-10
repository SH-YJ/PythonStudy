import socket

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = '192.168.64.1'

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    # print("连接地址: %s" % str(addr))

    smsg = '你好！'
    clientsocket.send(smsg.encode('utf-8'))

    clientsocket.close()