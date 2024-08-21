from m5stack import *
from m5ui import *
from uiflow import *
import time

# Set screen color
setScreenColor(0x222222)

# Text labels for buttons placed alongside the buttons
label_up = M5TextBox(40, 220, "Up", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label_down = M5TextBox(140, 220, "Down", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label_play = M5TextBox(240, 220, "Play", lcd.FONT_Default, 0xFFFFFF, rotate=0)

# Define the tones and menu
tones = [440, 880, 1200, 1600, 2000]
current_index = 0

# Display menu and scroll bar
def display_menu():
    lcd.clear()
    label_up.show()
    label_down.show()
    label_play.show()
    
    for i in range(len(tones)):
        if i == current_index:
            lcd.print("> Tone " + str(i + 1), 40, 100 + (i * 20), 0xFFFFFF)
        else:
            lcd.print("  Tone " + str(i + 1), 40, 100 + (i * 20), 0x888888)
    
    # Draw scroll bar
    bar_height = 80 // len(tones)
    bar_y = 100 + (bar_height * current_index)
    lcd.rect(200, 100, 10, 80, 0x888888)
    lcd.rect(200, bar_y, 10, bar_height, 0xFFFFFF, fillcolor=0xFFFFFF)

# Play the selected tone
def play_tone():
    speaker.tone(tones[current_index], 200)

# Initial menu display
display_menu()

# Button press events
def buttonA_wasPressed():
    global current_index
    current_index = (current_index - 1) % len(tones)
    display_menu()

def buttonB_wasPressed():
    global current_index
    current_index = (current_index + 1) % len(tones)
    display_menu()

def buttonC_wasPressed():
    play_tone()

# Attach button events
btnA.wasPressed(buttonA_wasPressed)
btnB.wasPressed(buttonB_wasPressed)
btnC.wasPressed(buttonC_wasPressed)

while True:
    # Keep running to capture button presses
    wait_ms(10)
