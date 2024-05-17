import math
import numpy

class MD:
    def __init__(self, input_str):
        self.input_str = input_str
        self.step1 = 0
        self.step2 = 0
        self.step3 = 0

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
            hash(self, self.bytes_output)
            
    
    def hash(self, arr):   
        #first level of incryption
        for i in range(16):
            for j in range(4):
                self.step1 = self.step1 += arr[i][j]
        #second level of incryption
        

string = input()
md=MD(string)
md.bytes()
