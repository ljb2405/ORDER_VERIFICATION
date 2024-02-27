import Adafruit_BBIO.GPIO as GPIO
import time

# Parameters
reset = 0
prog_wait = 1
programming = 2
prog_stabilizing = 3
prog_done = 4

# Pin configuration

# PROG_CLK = # clock probably should be dealt with PWM
PROG_RST = "P8_7"
PROG_DONE = "P8_8"
PROG_WE = "P8_9"
PROG_DIN = "P8_10"
PROG_DOUT = "P8_11"
PROG_WE_O = "P8_12"

# Setup GPIO
GPIO.setup(PROG_RST, GPIO.OUT)
GPIO.setup(PROG_DONE, GPIO.OUT)
GPIO.setup(PROG_WE, GPIO.OUT)
GPIO.setup(PROG_DIN, GPIO.OUT)
GPIO.setup(PROG_DOUT, GPIO.IN)
GPIO.setup(PROG_WE_O, GPIO.IN)

# Initialize
GPIO.output(PROG_RST, GPIO.HIGH)
GPIO.output(PROG_DONE, GPIO.LOW)
GPIO.output(PROG_WE, GPIO.LOW)
GPIO.output(PROG_WE, GPIO.LOW)

# Initialize variables
state = reset
prog_progress = 0
wait_count = 0



# Function to send a single bit to the FPGA
def send_bit(bit):
    GPIO.output(DIN, bit)
    GPIO.output(CCLK, GPIO.HIGH)
    time.sleep(0.0001)  # Adjust based on your FPGA's clock requirements
    GPIO.output(CCLK, GPIO.LOW)

# Load the bitstream file
bitstream = open("/home/jae/order/bcd2bin/bitgen.out", "rb")
    # byte = bitstream.read(1)
    # while byte:
    #     # Send each bit in the byte (assuming MSB first)
    #     for i in range(7, -1, -1):
    #         bit = (byte[0] >> i) & 1
    #         send_bit(bit)
    #     byte = bitstream.read(1)

# Programmer FSM
while (state != prog_done):
    if (state == reset):
        state = prog_wait
        # time.sleep(1)
    elif (state == prog_wait):
        


# Check if programming was successful
if GPIO.input(DONE):
    print("FPGA programming successful!")
else:
    print("FPGA programming failed.")

