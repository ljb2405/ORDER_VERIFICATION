cd /sys/class/pwm/pwm-6:0 # goes to the directory to change the setting
                          # P8.19 to change PWM setting

echo 500000 > period # Period of 1 MHz
echo 250000 > duty_cycle # Sets the duty cycle as half
echo 1 > enable # Enables the PWM signal for clock
