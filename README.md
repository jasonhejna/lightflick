# lightflick
Trigger events by flicking your lights on and off a couple times

>```
          .----------.
          |   ~ON~   |
          |   ____   |
          |  |.--.|  |
          |  ||  ||  |
          |  ||__||  |
          |  ||\ \|  |
          |  |\ \_\  |
          |  |_\[_]  |
          |          |
          |  ~OFF~   |
          '----------'
>```

Measure a photoresistor value and trigger events if the lights are flicked on/off at least twice. Number of flicks can be set.

[Here's a raspberry pi wiring tutorial](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading)

## Instructions
- You'll need to change the GPIO pin in read.py to the one you chose to wire up. Default is pin 20.
- You should add the functionality you want to execute_functions.py. The cooresponding function will get called depending on how many times the light was flicked.
