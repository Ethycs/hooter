import os, sys, io
import M5
from M5 import *

# Initialize label objects
label_up = None
label_down = None
label_play = None
tone_labels = []
rect_scrollbar = None

# Initialize tones and current index
tones = [440, 880, 1200, 1600, 2000]
current_index = 0

def display_menu():
    global rect_scrollbar, tone_labels



    # Create or update tone labels
    if not tone_labels:
        for i in range(len(tones)):
            label = Widgets.Label("", 40, 100 + (i * 20), 1.0, 0x888888, 0x222222, Widgets.FONTS.DejaVu18)
            tone_labels.append(label)

    for i in range(len(tones)):
        if i == current_index:
            tone_labels[i].setText("> Tone " + str(i + 1))
            tone_labels[i].setColor(0xFFFFFF)
        else:
            tone_labels[i].setText("  Tone " + str(i + 1))
            tone_labels[i].setColor(0x888888)

    # Draw the scroll bar
    bar_height = 80 // len(tones)
    bar_y = 100 + (bar_height * current_index)
    rect_scrollbar = Widgets.Rectangle(200, 100, 10, 80, 0x888888, 0x222222)
    rect_scrollbar_selected = Widgets.Rectangle(200, bar_y, 10, bar_height, 0xFFFFFF, 0xFFFFFF)

    # Update button labels (ensure they are visible)
    label_up.setText("Up")
    label_down.setText("Down")
    label_play.setText("Play")

def play_tone():
    speaker.tone(tones[current_index], 200)

def btnA_wasPressed_event(state):
    global current_index, label_up, label_down, label_play
    current_index = (current_index - 1) % len(tones)
    display_menu()

def btnB_wasPressed_event(state):
    global current_index, label_up, label_down, label_play
    current_index = (current_index + 1) % len(tones)
    display_menu()

def btnC_wasPressed_event(state):
    global label_up, label_down, label_play
    play_tone()

def setup():
    global label_up, label_down, label_play

    M5.begin()
    Widgets.fillScreen(0x222222)

    # Create labels for buttons once
    label_up = Widgets.Label("Up", 40, 220, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    label_down = Widgets.Label("Down", 140, 220, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    label_play = Widgets.Label("Play", 240, 220, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)

    # Initial menu display
    display_menu()

    # Attach button events using setCallback
    BtnA.setCallback(type=BtnA.CB_TYPE.WAS_PRESSED, cb=btnA_wasPressed_event)
    BtnB.setCallback(type=BtnB.CB_TYPE.WAS_PRESSED, cb=btnB_wasPressed_event)
    BtnC.setCallback(type=BtnC.CB_TYPE.WAS_PRESSED, cb=btnC_wasPressed_event)

def loop():
    M5.update()

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
