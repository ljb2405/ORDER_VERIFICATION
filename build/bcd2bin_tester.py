import Adafruit_BBIO.GPIO as GPIO
import time

# PARAMETERS
sleepTimeOneCycle = 0.0001 # Based on 10 KHz clk
sleepTime100Cycle = 0.01   # Based on 10 KHz clk

# FUNCTIONS
def set_bcd_value(bcd_digit, pins):
    """Sets the BCD digit on the given GPIO pins."""
    for i in range(4):
        GPIO.output(pins[i], GPIO.HIGH if bcd_digit & (1 << i) else GPIO.LOW)

def test_bcd_to_bin(bcd_digit0, bcd_digit1, expected_binary):
    # GPIO pin setup for BCD digits and binary result would be needed here
    # For example:
    # bcd_pins_digit0 = [w_test_bcd0_0, w_test_bcd0_1, w_test_bcd0_2, w_test_bcd0_3]
    # bcd_pins_digit1 = [w_test_bcd1_0, w_test_bcd1_1, w_test_bcd1_2, w_test_bcd1_3]
    # bin_pins = [w_test_bin_0, w_test_bin_1, w_test_bin_2, w_test_bin_3, w_test_bin_4, w_test_bin_5, w_test_bin_6, w_test_bin_7]

    print(f"\nTest Case BCD: {bcd_digit0}, {bcd_digit1}\n")

    # Set BCD INPUTS for both digits
    set_bcd_value(bcd_digit0, bcd_pins_digit0)
    set_bcd_value(bcd_digit1, bcd_pins_digit1)
    time.sleep(sleepTime100Cycle)

    # Low the reset
    #  GPIO.output(w_test_reset, GPIO.LOW)
    # time.sleep(sleepTime100Cycle)

    # If ready, start
    print("\nWaiting for rdy signal...\n")
    while (GPIO.input(w_impl_ready) == GPIO.LOW):
        time.sleep(sleepTimeOneCycle)

    print("\nStarting Test\n")
    GPIO.output(w_test_reset, GPIO.LOW)
    #GPIO.output(w_test_start, GPIO.HIGH)
    #GPIO.output(w_test_start, GPIO.HIGH)
    #time.sleep(sleepTimeOneCycle)
    #GPIO.output(w_test_start, GPIO.LOW)
    #GPIO.output(w_test_start, GPIO.LOW)

    # Wait until the operation is over
    print("\nTest Case Running...\n")
    while (GPIO.input(w_impl_done_tick) == GPIO.LOW):
        time.sleep(sleepTime100Cycle)

    # Check the resulting binary
    for i, pin in enumerate(bin_pins):
        if (GPIO.input(pin) != (GPIO.HIGH if (1 << i) & expected_binary else GPIO.LOW)):
            print(f"\nTest Case Failed: Wrong bin[{i}]\n")

# Pin configuration
# general clock supplied by PWM
# P8.19 corresponds to folder: /sys/class/pwm/pwmchip7/pwm-7:1
# clock is dealt in PWM with clock.sh
# PROG Signals for reference
PROG_RST = "P8_7"
PROG_DONE = "P8_8"
PROG_WE = "P8_9"
PROG_DIN = "P8_10"
PROG_DOUT = "P8_11"
PROG_WE_O = "P8_12"
PROG_CLK = "P8_13"
gpio = "P8_14"

# Bcd2bin signals
w_test_start = "P8_15"
w_test_reset = "P8_16"
w_impl_ready = "P8_17"
w_impl_done_tick = "P8_18"
w_test_bcd0_3 = "P8_21"
w_test_bcd0_2 = "P8_23"
w_test_bcd0_1 = "P8_25"
w_test_bcd0_0 = "P8_27"
w_test_bcd1_3 = "P8_29"
w_test_bcd1_2 = "P8_31"
w_test_bcd1_1 = "P8_33"
w_test_bcd1_0 = "P8_35"
w_test_bin_6 = "P9_12"
w_test_bin_5 = "P9_14"
w_test_bin_4 = "P9_16"
w_test_bin_3 = "P9_18"
w_test_bin_2 = "P9_20"
w_test_bin_1 = "P9_22"
w_test_bin_0 = "P9_24"

# List
bcd_pins_digit0 = [w_test_bcd0_0, w_test_bcd0_1, w_test_bcd0_2, w_test_bcd0_3]
bcd_pins_digit1 = [w_test_bcd1_0, w_test_bcd1_1, w_test_bcd1_2, w_test_bcd1_3]
bin_pins = [w_test_bin_0, w_test_bin_1, w_test_bin_2, w_test_bin_3, w_test_bin_4, w_test_bin_5, w_test_bin_6] #, w_test_bin_7]

# Setup GPIOs
GPIO.setup(PROG_CLK, GPIO.OUT)
GPIO.setup(PROG_RST, GPIO.OUT)
GPIO.setup(PROG_DONE, GPIO.OUT)
GPIO.setup(PROG_WE, GPIO.OUT)

# GPIO Setup on BCD2BIN
GPIO.setup(w_test_start, GPIO.OUT)
GPIO.setup(w_test_reset, GPIO.OUT)
GPIO.setup(w_impl_ready, GPIO.IN)
GPIO.setup(w_impl_done_tick, GPIO.IN)
GPIO.setup(w_test_bcd0_0, GPIO.OUT)
GPIO.setup(w_test_bcd0_1, GPIO.OUT)
GPIO.setup(w_test_bcd0_2, GPIO.OUT)
GPIO.setup(w_test_bcd0_3, GPIO.OUT)
GPIO.setup(w_test_bcd1_0, GPIO.OUT)
GPIO.setup(w_test_bcd1_1, GPIO.OUT)
GPIO.setup(w_test_bcd1_2, GPIO.OUT)
GPIO.setup(w_test_bcd1_3, GPIO.OUT)
GPIO.setup(w_test_bin_0, GPIO.IN)
GPIO.setup(w_test_bin_1, GPIO.IN)
GPIO.setup(w_test_bin_2, GPIO.IN)
GPIO.setup(w_test_bin_3, GPIO.IN)
GPIO.setup(w_test_bin_4, GPIO.IN)
GPIO.setup(w_test_bin_5, GPIO.IN)
GPIO.setup(w_test_bin_6, GPIO.IN)
#GPIO.setup(w_test_bin_7, GPIO.IN)

# Initialize Outputs
GPIO.output(PROG_RST, GPIO.LOW)
GPIO.output(PROG_DONE, GPIO.HIGH)
GPIO.output(PROG_WE, GPIO.LOW)
GPIO.output(PROG_CLK, GPIO.LOW)

GPIO.output(w_test_start, GPIO.HIGH)
GPIO.output(w_test_reset, GPIO.HIGH)

GPIO.output(w_test_bcd0_0, GPIO.LOW)
GPIO.output(w_test_bcd0_1, GPIO.LOW)
GPIO.output(w_test_bcd0_2, GPIO.LOW)
GPIO.output(w_test_bcd0_3, GPIO.LOW)
GPIO.output(w_test_bcd1_0, GPIO.LOW)
GPIO.output(w_test_bcd1_1, GPIO.LOW)
GPIO.output(w_test_bcd1_2, GPIO.LOW)
GPIO.output(w_test_bcd1_3, GPIO.LOW)

time.sleep(sleepTime100Cycle)

# Test Cases
## Test Case 0: BCD: {4'd0, 4'd0} BIN: 7'h00
test_bcd_to_bin(0, 0, 0)
## Test Case 1: BCD: {4'd9, 4'd9} BIN: 7'h63
test_bcd_to_bin(9, 9, 0x63)
## Test Case 2: BCD: {4'd5, 4'd5} BIN: 7'h37
test_bcd_to_bin(5, 5, 0x37)
## Test Case 3: BCD: {4'd0, 4'd9} BIN: 7'h09
test_bcd_to_bin(0, 9, 0x09)
## Test Case 4: BCD: {4'd9, 4'd0} BIN: 7'h5a
test_bcd_to_bin(9, 0, 0x5a)
