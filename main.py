mode = 0
# boot icon
basic.show_icon(IconNames.HAPPY)
# reads the value from the sound sensor (analog pin 1) and assigns it to the moisture_sensor_reading
sound_sensor_reading = pins.analog_read_pin(AnalogPin.P1)
# clears led screen
basic.clear_screen()
"""

sets mode value to 0 (default mode)

"""
# controls

def on_forever():
    global mode
    # credits
    if input.button_is_pressed(Button.A):
        basic.show_string("code written by jovan see :)")
    if input.button_is_pressed(Button.AB):
        # sets mode value to 1 (debug mode)
        mode = 1
basic.forever(on_forever)

# forever loop

def on_forever2():
    global sound_sensor_reading, mode
    # forever loop for default mode
    # checks for default mode value
    while mode == 0:
        # rereads the value from the sound sensor (analog pin 1) and reassigns it to the moisture_sensor_reading
        sound_sensor_reading = pins.analog_read_pin(AnalogPin.P1)
        # compares the reading to a fixed value for sound (511)
        if sound_sensor_reading == 511:
            # turns on fan (analog pin 2) by setting its value to 1023 
            pins.analog_write_pin(AnalogPin.P2, 1023)
        else:
            # waits awhile (3 secs) before repeating the loop
            basic.pause(3000)
    # checks for debug mode value (1)
    if mode == 1:
        # displays debug mode intro
        basic.show_string("DEBUG MODE ENABLED")
        # displays sound sensor reading
        basic.show_string("the sound sensor reading is: " + str(pins.analog_read_pin(AnalogPin.P1)))
    pins.analog_write_pin(AnalogPin.P2, 0)
    # shows fan off message
    basic.show_string("the fan is currently set to OFF")
    # turns on fan (analog pin 2) by setting its value to 1023 
    pins.analog_write_pin(AnalogPin.P2, 1023)
    # shows fan on message
    basic.show_string("the fan is currently set to ON")
    # waits awhile (3 secs) before repeating the loop
    basic.pause(3000)
    # sets mode value to 0 (default mode)
    mode = 0
basic.forever(on_forever2)
