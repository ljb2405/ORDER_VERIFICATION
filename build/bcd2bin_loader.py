"""Script to load the bitstream into ORDER FPGA"""

import Adafruit_BBIO.GPIO as GPIO
import time

# Parameters
half_period = 5e-5 # 10 kHz --> In reality, something lower than 10 KHz because of how Python runs
sleepTime100Cycle = half_period * 2 * 100 # Computer sleep for 100 cycles of clock
sleepTime10Cycle = half_period * 2 * 10 # Computer sleep for 10 cycles of clock

BS_NUM_QWORDS       = 422 # Bitstream length of bcd2bin
BS_WORD_SIZE        = 1 # Byte

# Pin configuration
# general clock supplied by PWM
# P8.19 corresponds to folder: /sys/class/pwm/pwmchip7/pwm-7:1
# clock is dealt in PWM with clock.sh

PROG_CLK = "P8_13"
PROG_RST = "P8_7"
PROG_DONE = "P8_8"
PROG_WE = "P8_9"
PROG_DIN = "P8_10"
PROG_DOUT = "P8_11"
PROG_WE_O = "P8_12"
gpio = "P8_14"

# Setup GPIO
GPIO.setup(PROG_CLK, GPIO.OUT)
GPIO.setup(PROG_RST, GPIO.OUT)
GPIO.setup(PROG_DONE, GPIO.OUT)
GPIO.setup(PROG_WE, GPIO.OUT)
GPIO.setup(PROG_DIN, GPIO.OUT)
GPIO.setup(PROG_DOUT, GPIO.IN)
GPIO.setup(PROG_WE_O, GPIO.IN)
GPIO.setup(gpio, GPIO.IN)

# Initialize Outputs
GPIO.output(PROG_RST, GPIO.HIGH)
GPIO.output(PROG_DONE, GPIO.LOW)
GPIO.output(PROG_WE, GPIO.LOW)
GPIO.output(PROG_CLK, GPIO.LOW)

"""Function to send one bit of bitstream to the FPGA"""
def send_bit(bit):
    # Sets the data bit
    GPIO.output(PROG_DIN, bit)

    # Causes rising edge of the clock
    GPIO.output(PROG_CLK, GPIO.HIGH)
    time.sleep(half_period)  # Adjust based on your FPGA's clock requirements
    
    # Clock goes low
    GPIO.output(PROG_CLK, GPIO.LOW)
    time.sleep(half_period) # Adjust based on your FPGA's clock requirements

"""Sends clock signal for the inputted amount of cycles
Argument 1: cycles - specifies the number of cycles that the chip will execute for
Argument 2: high_factor - specifies how the factor that the clock will be high compared to the clock low"""
def prog_sleep(cycles, high_factor):
    count = 0
    while (count < cycles):
        GPIO.output(PROG_CLK, GPIO.HIGH)
        count += 1
        time.sleep(half_period * high_factor)  # Adjust based on your FPGA's clock requirements
        GPIO.output(PROG_CLK, GPIO.LOW)
        time.sleep(half_period)

# Load the bitstream file
bitstream = open("../bcd2bin/bitgen.out", "r")

# Reset goes low
prog_sleep(10000, 1)
GPIO.output(PROG_RST, GPIO.LOW)

# Waits until gpio pin goes high
while (GPIO.input(gpio) == GPIO.LOW):
    time.sleep(1)


if (GPIO.input(gpio) == GPIO.HIGH):
    print("gpio pin set high")
    byte = int(bitstream.read(2), 16)
    prog_progress = 0
    GPIO.output(PROG_WE, GPIO.HIGH)
    prog_sleep(1)
    while (prog_progress + BS_WORD_SIZE < BS_NUM_QWORDS * 8):
        GPIO.output(PROG_WE, GPIO.HIGH)
    # Send each bit in the byte (assuming MSB first)
        for i in range(7, -1, -1):
            bit = (byte >> i) & 1
            send_bit(bit)
        prog_progress += BS_WORD_SIZE
        byte = int(bitstream.read(2), 16)
        # ## Potentially add error checking mechanism using dout?
        prog_sleep(1)
    
    GPIO.output(PROG_WE, GPIO.LOW)
    prog_sleep(10000)
    GPIO.output(PROG_DONE, GPIO.HIGH)
    prog_sleep(10000)
    time.sleep(sleepTime100Cycle)


if GPIO.input(PROG_DONE):
    print("FPGA programming successful!")
else:
    print("FPGA programming failed.")
