cd /sys/class/pwm/pwmchip7/pwm-7:0 #Selects the directory of P8_19
echo 0 > enable # Disables the clock
echo 0 > duty_cycle # Disables the duty cycle
echo 0 > period # Disables the period
