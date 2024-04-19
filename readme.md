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
├── readme.md
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
```
- /bcd2bin dirctory contains bitstream and other Verilog files related to sample application of bcd2bin
- /build directory contains scripts to load the bcd2bin bitstream into ORDER and test the properly loaded ORDER FPGA.
- /riscv_build directory contains files to properly set the user IOs of the FPGA by using the RISC-V CPU.
-  

## Bitstream Programming

## ORDER FPGA Testing
