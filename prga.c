/*
 * SPDX-FileCopyrightText: 2020 Efabless Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * SPDX-License-Identifier: Apache-2.0
 */

// This include is relative to $CARAVEL_PATH (see Makefile)
#include <defs.h>
#include <stub.h>

/*
	IO Test:
		- Configures MPRJ lower 8-IO pins as outputs
		- Observes counter value through the MPRJ lower 8 IO pins (in the testbench)
*/


// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void configure_io()
{

//  ======= Useful GPIO mode values =============

//      GPIO_MODE_MGMT_STD_INPUT_NOPULL
//      GPIO_MODE_MGMT_STD_INPUT_PULLDOWN
//      GPIO_MODE_MGMT_STD_INPUT_PULLUP
//      GPIO_MODE_MGMT_STD_OUTPUT
//      GPIO_MODE_MGMT_STD_BIDIRECTIONAL
//      GPIO_MODE_MGMT_STD_ANALOG

//      GPIO_MODE_USER_STD_INPUT_NOPULL
//      GPIO_MODE_USER_STD_INPUT_PULLDOWN
//      GPIO_MODE_USER_STD_INPUT_PULLUP
//      GPIO_MODE_USER_STD_OUTPUT
//      GPIO_MODE_USER_STD_BIDIRECTIONAL
//      GPIO_MODE_USER_STD_ANALOG


//  ======= set each IO to the desired configuration =============

    //  GPIO 0 is turned off to prevent toggling the debug pin; For debug, make this an output and
    //  drive it externally to ground.

    reg_mprj_io_0 = GPIO_MODE_MGMT_STD_ANALOG;

    // Changing configuration for IO[1-4] will interfere with programming flash. if you change them,
    // You may need to hold reset while powering up the board and initiating flash to keep the process
    // configuring these IO from their default values.

    reg_mprj_io_1 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_2 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_3 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_4 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;

    // -------------------------------------------

    reg_mprj_io_5 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;     // UART Rx
    reg_mprj_io_6 = GPIO_MODE_MGMT_STD_OUTPUT;           // UART Tx
    reg_mprj_io_7 = GPIO_MODE_MGMT_STD_OUTPUT;           // prog_we_o
    reg_mprj_io_8 = GPIO_MODE_MGMT_STD_OUTPUT;           // prog_dout
    reg_mprj_io_9 = GPIO_MODE_USER_STD_BIDIRECTIONAL;    // N.C
    reg_mprj_io_10 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // N.C
    reg_mprj_io_11 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_bin[6]
    reg_mprj_io_12 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_bin[5]
    reg_mprj_io_13 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_bin[4]
    reg_mprj_io_14 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_bin[3]
    reg_mprj_io_15 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // N.C
    reg_mprj_io_16 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_bin[2]
    reg_mprj_io_17 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_bin[1]
    reg_mprj_io_18 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_bin[0]

    reg_mprj_io_19 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_done_tick
    reg_mprj_io_20 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_impl_ready
    reg_mprj_io_21 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd0[3]
    reg_mprj_io_22 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd0[2]
    reg_mprj_io_23 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd0[1]
    reg_mprj_io_24 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd0[0]
    reg_mprj_io_25 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd1[3]
    reg_mprj_io_26 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd1[2]
    reg_mprj_io_27 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd1[1]
    reg_mprj_io_28 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_bcd1[0]
    reg_mprj_io_29 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_start
    reg_mprj_io_30 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // w_test_reset
    reg_mprj_io_31 = GPIO_MODE_USER_STD_BIDIRECTIONAL;   // 1'b0
    reg_mprj_io_32 = GPIO_MODE_USER_STD_INPUT_NOPULL; // prog_we
    reg_mprj_io_33 = GPIO_MODE_USER_STD_INPUT_NOPULL; // prog_rst
    reg_mprj_io_34 = GPIO_MODE_USER_STD_INPUT_NOPULL; // prog_done
    reg_mprj_io_35 = GPIO_MODE_USER_STD_INPUT_NOPULL; // prog_din
    reg_mprj_io_36 = GPIO_MODE_USER_STD_INPUT_NOPULL; // clk
    reg_mprj_io_37 = GPIO_MODE_USER_STD_INPUT_NOPULL; // prog_clk

    // Initiate the serial transfer to configure IO
    reg_mprj_xfer = 1;
    while (reg_mprj_xfer == 1);
}

void delay(const int d)
{

    /* Configure timer for a single-shot countdown */
	reg_timer0_config = 0;
	reg_timer0_data = d;
    reg_timer0_config = 1;

    // Loop, waiting for value to reach zero
   reg_timer0_update = 1;  // latch current value
   while (reg_timer0_value > 0) {
           reg_timer0_update = 1;
   }

}

void main()
{
	/* 
	IO Control Registers
	| DM     | VTRIP | SLOW  | AN_POL | AN_SEL | AN_EN | MOD_SEL | INP_DIS | HOLDH | OEB_N | MGMT_EN |
	| 3-bits | 1-bit | 1-bit | 1-bit  | 1-bit  | 1-bit | 1-bit   | 1-bit   | 1-bit | 1-bit | 1-bit   |

	Output: 0000_0110_0000_1110  (0x1808) = GPIO_MODE_USER_STD_OUTPUT
	| DM     | VTRIP | SLOW  | AN_POL | AN_SEL | AN_EN | MOD_SEL | INP_DIS | HOLDH | OEB_N | MGMT_EN |
	| 110    | 0     | 0     | 0      | 0      | 0     | 0       | 1       | 0     | 0     | 0       |
	
	 
	Input: 0000_0001_0000_1111 (0x0402) = GPIO_MODE_USER_STD_INPUT_NOPULL
	| DM     | VTRIP | SLOW  | AN_POL | AN_SEL | AN_EN | MOD_SEL | INP_DIS | HOLDH | OEB_N | MGMT_EN |
	| 001    | 0     | 0     | 0      | 0      | 0     | 0       | 0       | 0     | 1     | 0       |

	*/

	/* Set up the housekeeping SPI to be connected internally so	*/
	/* that external pin changes don't affect it.			*/

	// reg_spi_enable = 1;
	// reg_spimaster_cs = 0x10001;
	// reg_spimaster_control = 0x0801;

	// reg_spimaster_control = 0xa002;	// Enable, prescaler = 2,
                                        // connect to housekeeping SPI

	// Connect the housekeeping SPI to the SPI master
	// so that the CSB line is not left floating.  This allows
	// all of the GPIO pins to be used for user functions.

    // Use GPIO as the signal that the mgmt core is ready
    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 1;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;

    configure_io();
    
    reg_gpio_out = 0;
    reg_gpio_out = 0;

	// // Configure lower 8-IOs as user output
	// // Observe counter value in the testbench
    // reg_mprj_io_0 =  GPIO_MODE_USER_STD_OUTPUT;     // prog_we_o
    // reg_mprj_io_1 =  GPIO_MODE_USER_STD_OUTPUT;     // prog_dout
    // reg_mprj_io_2 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_3 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_4 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_5 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_6 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_7 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_8 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_9 =  GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_10 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_11 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_12 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_13 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_14 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_15 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_16 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_17 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_18 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_19 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_20 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_21 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_22 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_23 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_24 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_25 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_26 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_27 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_28 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_29 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_30 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_31 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_32 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_33 = GPIO_MODE_USER_STD_BIDIRECTIONAL;
    // reg_mprj_io_32 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // prog_we
    // reg_mprj_io_33 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // prog_rst
    // reg_mprj_io_34 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // prog_done
    // reg_mprj_io_35 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // prog_din
    // reg_mprj_io_36 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // clk
    // reg_mprj_io_37 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // prog_clk
        
	
    
    
    reg_uart_enable = 1;
    
    /* Apply configuration */
	reg_mprj_xfer = 1;
	while (reg_mprj_xfer == 1);

    // set GPIO to 1 to signal the external bitstream loader
    reg_gpio_out = 1;
    reg_gpio_out = 1;
    // Reset the IOs
    reg_mprj_datal = 0x00000000;
    reg_mprj_datah = 0x00000000;

    print("Pin configuration succeeeded");

	// while (1) {

    //     // reg_gpio_out = 1; // OFF
    //     reg_mprj_datal = 0x00000000;
    //     reg_mprj_datah = 0x00000000;

	// 	//delay(800000);
	// 	delay(8000000);

    //     // reg_gpio_out = 0;  // ON
    //     reg_mprj_datah = 0x0000003f;
    //     reg_mprj_datal = 0xffffffff;

	// 	//delay(800000);
	// 	delay(8000000);

    // }
    // If the gpio[34] accepts PROG_DONE properly,
    // the board starts blinking
   
    while (1) {
        if (reg_mprj_datah == 0x00000004)
        {
            reg_gpio_out = 1; // OFF
    //     reg_mprj_datal = 0x00000000;
    //     reg_mprj_datah = 0x00000000;

	// 	//delay(800000);
		    delay(8000000);

            reg_gpio_out = 0;  // ON
    //     reg_mprj_datah = 0x0000003f;
    //     reg_mprj_datal = 0xffffffff;

	// 	//delay(800000);
		    delay(8000000);

    // }
    }
    else {
        reg_gpio_out = 1; // OFF
        delay(8000000);
    }
}