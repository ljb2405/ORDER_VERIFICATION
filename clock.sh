config-pin P8.19 pwm
cd /sys/class/pwm/pwmchip7/pwm-7:1 # goes to the directory to change the setting
                          # P8.19 to change PWM setting
sh -c "echo '5000' >> ./period" # Period of 10 KHz
sh -c "echo '2500' >> ./duty_cycle" # Sets the duty cycle as half
sh -c "echo '1' >> ./enable" # Enables the PWM signal for clock
