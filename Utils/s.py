def writeBit(self, data):
        self.bitIndex = data
        if (self.bitIndex == 0):
            self.offset += 1
            self.buffer += bytearray(b'\xff');
        
        value = self.buffer[self.offset - 1]
        value &= ~(1 << self.bitIndex)
        value |= (data << self.bitIndex)
        self.buffer[self.offset - 1] = value
        
        self.bitIndex = (self.bitIndex + 1) % 8

    def dectobin(self, num, bitsCount):
        binary = bin(num)
        bitterly = binary[2:]
        bits = []
        for b in bitterly:
            if b == '0': bits.append(0)
            else: bits.append(1)
        return bits[::-1]
    
    def writeBits(self, bits, count):
        i = 0
        position = 0
        while i < count:
            value = 0
            
            p = 0
            while p < 8 and i < count:
                value = (bits[position] >> p) & 1
                self.writeBit(value)
                p += 1
                i += 1
            position += 1
    
    def writePositiveInt(self, value, bitsCount):
        self.writeBits(value.to_bytes(4, byteorder='little'), bitsCount)

    def writeInt2(self, value, bitsCount):
        val = value
        if val <= -1:
            self.writePositiveInt(0, 1)
            val = -value
        elif val >= 0:
            self.writePositiveInt(1, 1)
            val = value
        self.writePositiveInt(val, bitsCount)
    
    def writePositiveVint(self, value, count):
        v3 = 1
        v7 = value
        
        if v7 != 0:
            if (v7 < 1):
                v3 = 0
            else:
                v8 = v7
                v3 = 0
                
                v3 += 1
                v8 >>= 1
                
                while (v8 != 0):
                    v3 += 1
                    v8 >>= 1
        self.writePositiveInt(v3 - 1, count)
        self.writePositiveInt(v7, v3)
self.writePositiveInt(1000000, 21)
        self.writeVint(0, 4)
        self.writePositiveInt(0, 1)
        self.writeInt(0, 4)

        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)


        self.writePositiveInt(0, 5)
        self.writePositiveInt(0, 6)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(0, 6)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 12)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(1, 8)

        self.writePositiveInt(16, 5)
        self.writePositiveInt(0, 8)

        self.writePositiveInt(0, 14)

        self.writeVint(2550, 4)            
        self.writeVint(150, 4)
        self.writeVint(0, 3)
        self.writeVint(0, 4)
        self.writePositiveInt(10, 4)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(4, 3)
        self.writePositiveInt(0, 1)
        self.writeInt(63, 6)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 2)
        self.writePositiveInt(3600, 13)
        self.writePositiveInt(3600, 13)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 4)
        self.writePositiveInt(0, 2)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 9)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(0, 5)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(3000, 12)
        self.writePositiveInt(1, 1)
        self.writePositiveInt(0, 1)
        self.writePositiveInt(1, 1)

        self.writePositiveInt(0, 8)