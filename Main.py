import logging
import socket
import time
import os
from threading import *
import struct
from Logic.Device import Device
from Logic.Player import Players
from Packets.LogicMessageFactory import packets
from Utils.Config import Config

logging.basicConfig(filename="errors.log", level=logging.INFO, filemode="w")

def _(*args):
    print('[INFO]', end=' ')
    for arg in args:
        print(arg, end=' ')
    print()

MOVE_PACKET_ID = 20100
ATTACK_PACKET_ID = 20101
MATCHMAKING_PACKET_ID = 20200  # Eşleştirme için yeni paket ID

class Server:
    Clients = {"ClientCounts": 0, "Clients": {}}
    ThreadCount = 0
    matchmaking_list = []  # Eşleştirme listesi

    def __init__(self, ip: str, port: int):
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = port
        self.ip = ip

    def start(self):
        if not os.path.exists('./config.json'):
            print("Creating config.json...")
            Config.create_config(self)

        self.server.bind((self.ip, self.port))
        _(f'Puvay Brawl started on ip {self.ip} and port {self.port}.')
        while True:
            self.server.listen()
            client, address = self.server.accept()
            _(f'New connection from ip {address[0]}')
            ClientThread(client, address).start()
            Server.ThreadCount += 1

class ClientThread(Thread):
    def __init__(self, client, address):
        super().__init__()
        self.client = client
        self.address = address
        self.device = Device(self.client)
        self.player = Players(self.device)

    def recvall(self, length: int):
        data = b''
        while len(data) < length:
            s = self.client.recv(length)
            if not s:
                print("Receive Error!")
                break
            data += s
        return data

    def handle_matchmaking(self):
        Server.matchmaking_list.append(self.player)  # Oyuncuyu eşleştirme listesine ekle
        print(f"{self.player.low_id} is in matchmaking. Total: {len(Server.matchmaking_list)}")

        if len(Server.matchmaking_list) >= 3:  # 3 oyuncu olduğunda eşleştir
            # Burada eşleştirme odası oluşturabiliriz
            self.start_game()

    def start_game(self):
        # Eşleştirilen oyuncuların listesini işleme al
        for player in Server.matchmaking_list:
            # Her oyuncuya eşleştirme tamamlandığını bildir
            player.client.sendall(b'Matchmaking complete! You are in a game.')
        
        # Eşleştirme listesini sıfırla
        Server.matchmaking_list.clear()

    def run(self):
        last_packet = time.time()
        try:
            while True:
                header = self.client.recv(7)
                if len(header) > 0:
                    last_packet = time.time()
                    packet_id = int.from_bytes(header[:2], 'big')
                    length = int.from_bytes(header[2:5], 'big')
                    data = self.recvall(length)

                    if packet_id in packets:
                        _(f'Received packet with ID {packet_id}.')
                        message = packets[packet_id](self.client, self.player, data)
                        message.decode()
                        message.process()

                        if packet_id == MOVE_PACKET_ID:
                            self.handle_move_packet(data)
                        elif packet_id == ATTACK_PACKET_ID:
                            self.handle_attack_packet(data)
                        elif packet_id == MATCHMAKING_PACKET_ID:
                            self.handle_matchmaking()  # Eşleştirme işlemi

                        if packet_id == 10101:
                            Server.Clients["Clients"][str(self.player.low_id)] = {"SocketInfo": self.client}
                            Server.Clients["ClientCounts"] = Server.ThreadCount
                            self.player.ClientDict = Server.Clients

                    else:
                        _(f'Packet {packet_id} not handled!')

                if time.time() - last_packet > 10:
                    print(f"[INFO] Ip: {self.address[0]} disconnected!")
                    self.client.close()
                    break
        except ConnectionAbortedError:
            print(f"[INFO] Ip: {self.address[0]} disconnected!")
            self.client.close()
        except ConnectionResetError:
            print(f"[INFO] Ip: {self.address[0]} disconnected!")
            self.client.close()
        except TimeoutError:
            print(f"[INFO] Ip: {self.address[0]} disconnected!")
            self.client.close()

if __name__ == '__main__':
    server = Server('0.0.0.0', 9339)
    server.start()