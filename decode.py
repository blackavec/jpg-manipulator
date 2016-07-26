import sys
import binascii

def castByteToBit(byte):
    return "{0:08b}".format(ord(byte));

def getLastBits(binByte, len):
    return binByte[len * (-1):]

def doBinaryManipulation(byte):
    binByte = castByteToBit(byte)
    return getLastBits(binByte, 2)

def readFile(path):
    bitBank = ""
    with open(path, "rb") as f:
        for line in f: 
            for byte in line:
                bitBank += doBinaryManipulation(byte)
                if len(bitBank) == 8:
                    print chr(int(bitBank, 2)),
                    bitBank = ""

def main():
    readFile("./secret-msg.jpg");

main()