def on_button_pressed_a():
    basic.show_string("Goh Ngan Bing")
    basic.pause(1000)
    basic.show_string("5U")
    basic.pause(500)
    basic.show_string("Press The Button B")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("ERroR")
    basic.show_leds("""
        . # . # #
                # # # . #
                # . . # .
                # # # . .
                . . # # .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    basic.show_string("I am happy.")
    basic.pause(500)
    basic.show_string("Please Press The Button A+B")
input.on_button_pressed(Button.B, on_button_pressed_b)

music.play_melody("C5 B A G F E D C ", 120)
music.play_melody("C D E F G A B C5 ", 120)
basic.pause(500)
basic.show_string("Press The Button A")