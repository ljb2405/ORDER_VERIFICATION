config-pin P8.19 pwm
cd /sys/class/pwm/pwmchip7/pwm-7:0 # goes to the directory to change the setting
                          # P8.19 to change PWM setting
echo 100000 > period # Period of 10 KHz
echo 50000 > duty_cycle # Sets the duty cycle as half
echo 1 > enable # Enables the PWM signal for clock
