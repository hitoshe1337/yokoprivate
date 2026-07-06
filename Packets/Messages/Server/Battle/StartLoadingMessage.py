from Utils.Writer import Writer
import random

class StartLoadingMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20559
        self.player = player

    def encode(self):
        list = [228, 150]
        self.writeInt(6) #6
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeInt(6) #players count
        
        self.writeInt(self.player.high_id) #High ID
        self.writeInt(self.player.low_id) #Low ID
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000001)
        self.writeVint(43000000)
        
        self.writeInt(0) #High ID
        self.writeInt(1) #Low ID
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("hi")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(2) #Low ID
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("hi")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(3) #Low ID
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("hi") #1st enemy player
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(4) #Low ID
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("Dummy")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(5) #Low ID
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("Dummy")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)   
        #PLAYERS SLOT END#
        
        self.writeInt(0) #count...
        
        self.writeInt(0) #Count
        
        self.writeInt(1) # Unknown
        
        self.writeVint(1)
        self.writeVint(1) #DrawMap
        self.writeVint(1)
        
        self.writeByte(0) #2, 39 - Spectating
        self.writeVint(0) # Unknown
        self.writeVint(0)
        
        #self.writeScId(15, random.choice(list))
        self.writeScId(15, 150)
        print("StartLoadingMessage sent.")
