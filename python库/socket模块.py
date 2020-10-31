from socket import *
import time
import os
import random

"""
udp和tcp服务器，选择消息或文件收发
"""

port = 6666
ip_dict = {"server": "192.168.1.5", "client": "192.168.49.128"}


def send_udp_msg(udp_socket, recv_msg):
    """服务器发送udp信息"""
    if recv_msg == "0":
        msg = input("请输入要发送的数据:")
        udp_socket.sendto(msg.encode("utf-8"), (ip_dict["client"], port))
    elif recv_msg == "1":
        os_path = "temp/" + "pic%d.jpg" % random.randint(1, 3)
        if os.path.exists(os_path):
            with open(os_path, "rb") as f:
                for line in f.readlines():
                    udp_socket.sendto(line, (ip_dict["client"], port))
                    time.sleep(0.001)
            udp_socket.sendto("".encode("utf-8"),  (ip_dict["client"], port))
        else:
            print("文件不存在！！请重新选择文件名！！")


def send_tcp_msg(client_socket, recv_msg):
    """服务器发送tcp信息"""
    if recv_msg == "0":
        msg = input("请输入要发送的数据:")
        client_socket.send(msg.encode("utf-8"))
    elif recv_msg == "1":
        os_path = "temp/" + "pic%d.jpg" % random.randint(1, 3)
        if os.path.exists(os_path):
            with open(os_path, "rb") as f:
                pic_content = f.read()
            client_socket.send(pic_content)
        else:
            print("文件不存在！！请重新选择文件名！！")


def create_udp_server():
    """创建udp服务端, 接受客户端消息返回消息和文件"""
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("", port))
    while True:
        recv_msg = udp_socket.recvfrom(1024)
        if recv_msg[0]:
            recv_msg = recv_msg[0].decode("utf-8")
        send_udp_msg(udp_socket, recv_msg)


def create_tcp_server():
    """创建tcp服务端, 接受客户端消息返回消息和文件"""
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_socket.bind(('', port))
    tcp_socket.listen(128)
    while True:
        client_socket, client_add1r = tcp_socket.accept()
        recv_msg = client_socket.recv(1024).decode('utf-8')
        send_tcp_msg(client_socket, recv_msg)
        client_socket.close()


def create_udp_client():
    """创建udp客户端"""
    while True:
        udp_socket = socket(AF_INET, SOCK_DGRAM)
        udp_socket.bind(("", port))
        msg_type = input("获取文本选择0，获取图片选择1:")
        udp_socket.sendto(msg_type.encode("utf-8"), (ip_dict["server"], port))
        if msg_type == "0":
            recv_msg = udp_socket.recvfrom(1024)
            print("来自%s信息：%s" % (str(recv_msg[1]), recv_msg[0].decode("utf-8")))
        if msg_type == "1":
            f = open("test.jpg", 'wb')
            while True:
                recv_data = udp_socket.recvfrom(1024*1024)
                if not recv_data[0]:
                    print("接收图片成功！！")
                    break
                f.write(recv_data[0])
            f.close()


def create_tcp_client():
    """创建tcp客户端"""
    while True:
        tcp_socket = socket(AF_INET, SOCK_STREAM)
        tcp_socket.connect((ip_dict["server"], port))
        msg_type = input("获取文本选择0，获取图片选择1:")
        tcp_socket.send(msg_type.encode('utf-8'))
        if msg_type == "0":
            recv_msg = tcp_socket.recv(1024).decode("utf-8")
            print("信息：%s" % recv_msg)
        if msg_type == "1":
            f = open("test.jpg", 'wb')
            while True:
                recv_data = tcp_socket.recv(1024)
                if not recv_data:
                    print("接收图片成功！！")
                    break
                f.write(recv_data)
            f.close()


def main():
    """主函数"""
    while True:
        user_socket_type = input("服务端udp协议选择0，服务端tcp协议选择1，客户端udp协议选择2，客户端tcp协议选择3：")
        if user_socket_type not in ["0", "1", "2", "3"]:
            print("wrong user_socket_type, try again!!")
        else:
            break
    if user_socket_type == "0":
        create_udp_server()
    if user_socket_type == "1":
        create_tcp_server()
    if user_socket_type == "2":
        create_udp_client()
    if user_socket_type == "3":
        create_tcp_client()


if __name__ == "__main__":
    main()
