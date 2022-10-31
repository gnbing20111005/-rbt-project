input.onButtonPressed(Button.A, function () {
    basic.showString("Goh Ngan Bing")
    basic.pause(1000)
    basic.showString("5U")
    basic.pause(500)
    basic.showString("Press The Button B")
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("ERroR")
    basic.showLeds(`
        . # . # #
        # # # . #
        # . . # .
        # # # . .
        . . # # .
        `)
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    basic.showString("I am happy.")
    basic.pause(500)
    basic.showString("Please Press The Button A+B")
})
music.playMelody("C5 B A G F E D C ", 120)
music.playMelody("C D E F G A B C5 ", 120)
basic.pause(500)
basic.showString("Press The Button A")
