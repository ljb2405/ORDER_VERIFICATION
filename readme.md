# ORDER VERIFICATION
This repository contains Python scripts and test bitstreams to verify the functionalities of ORDER FPGA.

The file tree is as such: 
```bash
.
├── bcd2bin
│   ├── bcd2bin_test_basic.v
│   ├── bcd2bin.v
│   ├── bitgen.out
│   ├── checker.v
│   └── prga_bitstream_loader.v
├── build
│   ├── bcd2bin_loader.py
│   ├── bcd2bin_tester.py
│   ├── clock_disable.sh
│   └── clock.sh
├── riscv_build
│   ├── Makefile
│   ├── prga_blink.c
│   ├── prga_blink.hex
│   ├── prga_blink.hexe
│   ├── prgablink.hexe
│   ├── prga_blink.lst
│   ├── prga.c
│   ├── prga.hex
│   ├── prga.hexe
│   ├── prga.lst
│   └── prga_tb.v
├── sample_tests
│   ├── 1_test_bitgen.out
│   ├── 2_test_bitgen.out
│   ├── 3_test_bitgen.out
│   └── test_bitgen.out
└── test
    ├── loader_test.py
    └── test.py
├── readme.md
```
- /bcd2bin dirctory contains bitstream and other Verilog files related to sample application of bcd2bin
- /build directory contains scripts to load the bcd2bin bitstream into ORDER and test the properly loaded ORDER FPGA.
- /riscv_build directory contains files to properly set the user IOs of the FPGA by using the RISC-V CPU. 
- /sample_tests directory contains sample bitstreams to ensure that the FPGA is being programmed correctly.
- /test directory contains test Python scripts to test if the bit is being correctly read from the file and if a bit is properly being sent to the FPGA.

## FPGA Test Setup
To set the FPGA up for programming and testing, Beaglebone Black was used. Beaglebone Black's GPIO sent signals to the FPGA to program and send test bits and to verify the outputs from ORDER FPGA. Beaglebone Black is connected via jumper wires to the ORDER breakout board. Both boards can be powered by micro-usb to usb wires to the computer. Or, Beaglebone Black can be powered via DC power source. 

Refer to https://github.com/efabless/caravel_board/tree/main/firmware/chipignite#readme
to learn more about Caravel Breakout Board.

## Bitstream Programming
To program ORDER FPGA, there are few pins to know beforehand:
1. `prog_clk`:  This is different from the regular clk of ORDER and is only used as the clock signal of bitstream programming for the FPGA. 
                Each data bit of the bitstream is shifted at each rising edge of `prog_clk` and if `prog_we` is high.
2. `prog_din`:  This pin is used to send each bit of the bitstream into the FPGA for programming. 
3. `prog_we`:   This pin is write enable signal to write `prog_din` and to shift the bitstream to the next register in the FPGA. 
4. `prog_dout`: This pin is a debug pin that outputs the inputted `prog_din`.
5. `prog_we_o`: This pin is a debug pin that outputs the inputted `prog_we`.
6. `prog_done`: This pin is used to send a signal to the FPGA that the programming is now done. 
7. `prog_rst`:  This pin resets the programmed FPGA.

### Bitstream Program Process
Before programming the FPGA, it is crucial to set the directions of the I/O pins of ORDER FPGA by programming the ORDER CPU.
The CPU can be programmed using the Makefile under /riscv_build using the command below.

```bash
make hex
make flash
```

The pins' direction can be changed by editing prga.c. Refer to prga.c for specific details. 

The current directions of the I/O pins prevent using the SPI flash to program the CPU. This is because `prog_dout` and `prog_we_o` share the same I/O pin as some of the SPI bus to the CPU. Because of this, changing the configuration of the I/O pins would require a hard reset of the CPU. The solution to this is to hold down the reset button (SW1) on the board and then power cycle the chip (by unplugging and re-plugging the USB cable) while you still have the reset button pressed.  Keep the reset button held down while you start the flashing. Once the flash is erasing, you can release the button; the first part of the flashing program is to put the chip into reset through the SPI interface and hold it in reset.

ORDER bitstream is programmed by sending each bit of bitstream into `prog_din` at every cycle of `prog_clk` while `prog_we` is high. 
At each clock cycle when `prog_we` is high, ORDER FPGA would take one bit of the bitstream and registers into the ORDER FPGA.
This bit is shifted to the next register at each clock cycle and would be properly placed after a number of clock cycles when 
all the bits of the bitstream is sent to the FPGA. After the FPGA is programmed, the user can send `prog_done` to be high so that the
FPGA knows the FPGA is done being programmed. 

After the bitstream is fully loaded, the user can verify if the correct bitstream was loaded by keep sending new bits into the 
FPGA. After a number of cycles, the programmed bits will be keep shifting to prog_dout. However, this method would require the FPGA
to be re-programmed after the verification.

`Prog_we_o` will output the inputted `prog_we` after a number of cycles, but `prog_we_o` would be outputting much faster than `prog_dout` would. 

## ORDER FPGA Testing

Prior to running the FPGA, it is crucial to generate clock signal. Clock signal in Beaglebone Black can be generated using `clock.sh` under /build. This will generate clock signal from P8.19 pin of Beaglebone Black. To disable the clock, use `clock_disable.sh`.

After the FPGA is programmed, the FPGA can be tested by running the FPGA by sending signals using `bcd2bin_loader.py` under /build directory. 