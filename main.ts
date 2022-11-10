input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Forever)
})
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        # # # # #
        . # # # .
        . . # . .
        `)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 500, 499, 255, 0, 750, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Forever)
})
input.onSound(DetectedSound.Loud, function () {
    basic.showLeds(`
        . . # . .
        . . # # .
        . . # . #
        . . # . .
        . . # . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(input.lightLevel())
})
input.onButtonPressed(Button.B, function () {
	
})
basic.forever(function () {
	
})
