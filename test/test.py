## Test Python script to read the test file
## and prints each bit to the terminal

import Adafruit_BBIO.GPIO as GPIO
import time

# Load the bitstream file
bitstream = open("../sample_tests/1_test_bitgen.out", "r")
byte = int(bitstream.read(2), 16)
print("\n", byte)

while byte:
    for i in range(7, -1, -1):
        bit = (byte >> i) & 1
        print(str(bit))
    byte = int(bitstream.read(2), 16)
    print("\n")
