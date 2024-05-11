import math
class MD:
    def __init__(self, input_str):
        self.input_str = input_str

    def bytes(self):
        self.bytes_original = bytearray(self.input_str,"ascii")
        self.bytes_output = bytearray(self.input_str, "ascii")
        self.output_array = []
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
            for i in range(1,64):
                output_array.append(math.abs(math.sin(bytes_output[i]+1))*2^32)
string = input()
md=MD(string)
md.bytes()
