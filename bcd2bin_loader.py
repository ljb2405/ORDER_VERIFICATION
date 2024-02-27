import Adafruit_BBIO.GPIO as GPIO
import time

# Pin configuration

# PROG_CLK = # clock probably should be dealt with PWM
PROG_RST = "P8_7"
PROG_DONE = "P8_8"
PROG_WE = "P8_9"
PROG_DIN = "P8_10"
PROG_DOUT = "P8_11"
PROG_WE_O = "P8_12"

# Setup GPIO
GPIO.setup(PROG_B, GPIO.OUT)
GPIO.setup(CCLK, GPIO.OUT)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(DONE, GPIO.IN)

# Initialize
GPIO.output(PROG_B, GPIO.HIGH)
GPIO.output(CCLK, GPIO.LOW)
time.sleep(0.1)  # Wait for any power-up conditions to stabilize
GPIO.output(PROG_B, GPIO.LOW)
time.sleep(0.01)  # Wait for the FPGA to clear any previous configuration
GPIO.output(PROG_B, GPIO.HIGH)

# Function to send a single bit to the FPGA
def send_bit(bit):
    GPIO.output(DIN, bit)
    GPIO.output(CCLK, GPIO.HIGH)
    time.sleep(0.0001)  # Adjust based on your FPGA's clock requirements
    GPIO.output(CCLK, GPIO.LOW)

# Load the bitstream file
with open("/home/jae/order/bcd2bin/bitgen.out", "rb") as bitstream:
    byte = bitstream.read(1)
    while byte:
        # Send each bit in the byte (assuming MSB first)
        for i in range(7, -1, -1):
            bit = (byte[0] >> i) & 1
            send_bit(bit)
        byte = bitstream.read(1)

# Check if programming was successful
if GPIO.input(DONE):
    print("FPGA programming successful!")
else:
    print("FPGA programming failed.")

