import Adafruit_BBIO.GPIO as GPIO
import time

# Parameters
half_period = 5e-5 # 10 kHz --> In reality, something lower than 10 KHz because of how Python runs

# Pin configuration
# general clock supplied by PWM
# P8.19 corresponds to folder: /sys/class/pwm/pwmchip7/pwm-7:1
# clock is dealt in PWM with clock.sh
PROG_CLK = "P8_14"
PROG_RST = "P8_7"
PROG_DONE = "P8_8"
PROG_WE = "P8_9"
PROG_DIN = "P8_10"
PROG_DOUT = "P8_11"
PROG_WE_O = "P8_12"
gpio = "P8_15"

# Setup GPIO
GPIO.setup(PROG_CLK, GPIO.OUT)
GPIO.setup(PROG_RST, GPIO.OUT)
GPIO.setup(PROG_DONE, GPIO.OUT)
GPIO.setup(PROG_WE, GPIO.OUT)
GPIO.setup(PROG_DIN, GPIO.OUT)
GPIO.setup(PROG_DOUT, GPIO.IN)
GPIO.setup(PROG_WE_O, GPIO.IN)
GPIO.setup(gpio, GPIO.IN)

# Initialize
GPIO.output(PROG_RST, GPIO.HIGH)
GPIO.output(PROG_DONE, GPIO.LOW)
GPIO.output(PROG_WE, GPIO.LOW)
GPIO.output(PROG_WE, GPIO.LOW)
GPIO.output(PROG_CLK, GPIO.LOW)

# Function to send a single bit to the FPGA
def send_bit(bit):
    GPIO.output(PROG_DIN, bit)
    GPIO.output(PROG_WE, GPIO.HIGH)
    GPIO.output(PROG_CLK, GPIO.HIGH)
    time.sleep(half_period)  # Adjust based on your FPGA's clock requirements
    GPIO.output(PROG_CLK, GPIO.LOW)
    GPIO.output(PROG_WE, GPIO.LOW)
    time.sleep(half_period)

# Load the bitstream file
bitstream = open("/home/jae/order/bcd2bin/bitgen.out", "rb")

GPIO.output(PROG_RST, GPIO.LOW)

# Waits until gpio pin goes high
# Should not be needed
while (GPIO.input(gpio) == GPIO.LOW):
    time.sleep(1)


if (GPIO.input(gpio) == GPIO.HIGH):
    print("gpio pin set high")
    byte = bitstream.read(1)
    while byte:
        # Send each bit in the byte (assuming MSB first)
        for i in range(7, -1, -1):
            bit = (byte[0] >> i) & 1
            send_bit(bit)
        byte = bitstream.read(1)

    GPIO.output(PROG_DONE, GPIO.HIGH)
    

# Check if programming was successful?
# Possibly utilize prog_dout / prog_we_o


if GPIO.input(PROG_DONE):
    print("FPGA programming successful!")
else:
    print("FPGA programming failed.")

