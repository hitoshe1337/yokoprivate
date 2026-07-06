from Utils.Writer import Writer
from Utils.BitStream import BitStream
from Database.DatabaseManager import DataBase
from Logic.Player import Players
from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage
import random
import time
#import BitStream
class VisionUpdate(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24109
        self.player = player


    def encode(self):
        self.writeVint(self.player.battleTick) # Battle Ticks
        self.writeVint(int(self.player.battleTick / 1))
        self.writeVint(1) # Commands Count
        self.writeVint(self.player.battleTick * 10) #viewers
        self.writeBoolean(True) # Live Boolean
        if self.player.battleTick == 1000000000000001:
            self.player.err_code = 18
            LoginFailedMessage(self.client, self.player, 'Battle has ended because of 1000 ticks!').send()
        stream = BitStream()
        stream.writePositiveInt(1000000, 21)
        stream.writePositiveVInt(0, 4)
        stream.writePositiveInt(0, 1)
        stream.writeInt(1, 4) #Game State

        stream.writePositiveInt(1, 10)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)


        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(12200, 12)
        stream.writePositiveInt(696969, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 12)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 4)
        stream.writePositiveInt(1, 8)

        stream.writePositiveInt(16, 5)
        stream.writePositiveInt(0, 8)

        stream.writePositiveInt(0, 14)

        stream.writePositiveVInt(2550, 4)
        stream.writePositiveVInt(150, 4)
        stream.writePositiveVInt(0, 3)
        stream.writePositiveVInt(0, 4)
        stream.writePositiveInt(10, 4)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(4, 3)
        stream.writePositiveInt(0, 1)
        stream.writeInt(63, 6)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 2)
        stream.writePositiveInt(3600, 13)
        stream.writePositiveInt(3600, 13)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 4)
        stream.writePositiveInt(0, 2)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 9)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(0, 5)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(3000, 12)
        stream.writePositiveInt(1, 1)
        stream.writePositiveInt(0, 1)
        stream.writePositiveInt(1, 1)

        stream.writePositiveInt(0, 8)
        buf = bytes(stream.buffer)
        self.buffer += buf
