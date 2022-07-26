// boot icon
basic.showIcon(IconNames.Happy)
// reads the value from the sound sensor (analog pin 1) and assigns it to the moisture_sensor_reading
let sound_sensor_reading = pins.analogReadPin(AnalogPin.P1)
// clears led screen
basic.clearScreen()
// sets mode value to 0 (default mode)
let mode = 0
// controls
basic.forever(function () {
    // credits
    if (input.buttonIsPressed(Button.A)) {
        basic.showString("code written by jovan see :)")
    }
    if (input.buttonIsPressed(Button.AB)) {
        // sets mode value to 1 (debug mode)
        mode = 1
    }
})
// forever loop
basic.forever(function () {
    // forever loop for default mode
    // checks for default mode value
    while (mode == 0) {
        // rereads the value from the sound sensor (analog pin 1) and reassigns it to the moisture_sensor_reading
        sound_sensor_reading = pins.analogReadPin(AnalogPin.P1)
        // compares the reading to a fixed value for sound (511)
        if (sound_sensor_reading == 511) {
            // turns on fan (analog pin 2) by setting its value to 1023
            pins.analogWritePin(AnalogPin.P2, 1023)
        } else {
            // waits awhile (3 secs) before repeating the loop
            basic.pause(3000)
        }
    }
    // checks for debug mode value (1)
    if (mode == 1) {
        // displays debug mode intro
        basic.showString("DEBUG MODE ENABLED")
        // displays sound sensor reading
        basic.showString("the sound sensor reading is: " + ("" + pins.analogReadPin(AnalogPin.P1)))
    }
    pins.analogWritePin(AnalogPin.P2, 0)
    // shows fan off message
    basic.showString("the fan is currently set to OFF")
    // turns on fan (analog pin 2) by setting its value to 1023
    pins.analogWritePin(AnalogPin.P2, 1023)
    // shows fan on message
    basic.showString("the fan is currently set to ON")
    // waits awhile (3 secs) before repeating the loop
    basic.pause(3000)
    // sets mode value to 0 (default mode)
    mode = 0
})
