import math
import numpy

class MD:
    def __init__(self, input_str):
        self.input_str = input_str
        self.A = 19088743
        self.B = 2309737967
        self.C = 4275878552
        self.D = 1985229328
        self.input_array_iteration_two = [1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12]
        self.input_array_iteration_three = [5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2]
        self.input_array_iteration_four = [0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9]

    def bytes(self):
        self.bytes_original = bytearray(self.input_str,"ascii")
        self.bytes_output = bytearray(self.input_str, "ascii")

        if len(self.bytes_original) > 56:
            pass # hash the string straight away
            return
        else:
            zeros = 56 - len(self.bytes_original) + 6
            self.bytes_output.append(0x01)
            for i in range(zeros):
                self.bytes_output.append(0x00)
            self.length = bytearray(str(len(self.bytes_original)),"ascii")
            self.bytes_output.append(len(self.length))
            
            self.bytes_output = numpy.array_split(self.bytes_output, 16)
            
            return self.hash123(self.bytes_output)
            
    def F (self):
        return (self.B and self.C) or (not self.B and self.D)
    
    def G (self):
        return (self.B and Self.D) or (self.C and not self.D)
    
    def H (self):
        return self.B ^ self.C ^ self.D
        
    def I (self):
        return self.C ^(self.B or not self.D)
    
    def hash123(self, arr):   
        #first level of incryption
        for i in range(1, 16):
            for j in range(1, 4):
                self.A += self.F()
                self.A += arr[i][j]
                self.A += math.fabs(math.sin(i+1))*2**32
                if i == 1 or i == 5 or i == 9 or i == 13:
                    self.A << 7
                if i == 2 or i == 6 or i == 10 or i == 14:
                    self.A << 12
                if i == 3 or i == 7 or i == 11 or i == 15:
                    self.A << 17
                if i == 4 or i == 8 or i == 12 or i == 16:
                    self.A << 18
                self.D = self.C
                self.C = self.B
                self.B = self.B + self.A
                self.D = self.A
                
        #second level of incryption
        for i in range(17, 32):
            for j in range(1, 4):
                self.A += self.G()
                self.A += arr[self.input_array_iteration_two[i-17]][j]
                self.A += math.fabs(math.sin(i+1))*2**32
                if i == 17 or i == 21 or i == 25 or i == 29:
                    self.A << 5
                if i == 18 or i == 22 or i == 26 or i == 30:
                    self.A << 9
                if i == 19 or i == 23 or i == 27 or i == 31:
                    self.A << 4
                if i == 20 or i == 24 or i == 28 or i == 32:
                    self.A << 20
                self.D = self.C
                self.C = self.B
                self.B = self.B + self.A
                self.D = self.A
                
        #third level of incryption        
        for i in range(33, 48):
            for j in range(1, 4):
                self.A += self.H()
                self.A += arr[self.input_array_iteration_three[i-33]][j]
                self.A += math.fabs(math.sin(i+1))*2**32
                if i == 33 or i == 37 or i == 41 or i == 45:
                    self.A << 4
                if i == 34 or i == 38 or i == 42 or i == 46:
                    self.A << 11
                if i == 35 or i == 39 or i == 43 or i == 47:
                    self.A << 16
                if i == 36 or i == 40 or i == 44 or i == 48:
                    self.A << 13
                self.D = self.C
                self.C = self.B
                self.B = self.B + self.A
                self.D = self.A
                
        #forth level of incryption
        for i in range(49, 64):
            for j in range(1, 4):
                self.A += self.I()
                self.A += arr[self.input_array_iteration_four[i-49]][j]
                self.A += math.fabs(math.sin(i+1))*(2**32)
                if i == 49 or i == 53 or i == 57 or i == 61:
                    self.A << 6
                if i == 50 or i == 54 or i == 58 or i == 62:
                    self.A << 10
                if i == 51 or i == 55 or i == 59 or i == 63:
                    self.A << 15
                if i == 52 or i == 56 or i == 60 or i == 64:
                    self.A << 21
                self.D = self.C
                self.C = self.B
                self.B = self.B + self.A
                self.D = self.A
                
        # final steps!
            self.A = (self.A + 19088743) % self.C
            self.B = (self.B + 2309737967) % self.C
            self.C = (self.C + 4275878552) % self.C
            self.D = (self.D + 1985229328) % self.C
            
            return hex(self.A+self.B+self.C+self.D)
string = input()
md=MD(string)
print(md.bytes())
