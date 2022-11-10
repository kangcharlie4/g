def on_logo_pressed():
    music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.FOREVER)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # . # .
                # # # # #
                . # # # .
                . . # . .
    """)
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            500,
            499,
            255,
            0,
            750,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.FOREVER)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    pass
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_ab():
    basic.show_number(input.light_level())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
