import os, sys, io
import M5
from M5 import *
from hardware import sdcard






def setup():

  sdcard.SDCard(slot=2, width=1, sck=18, miso=19, mosi=23, cs=4, freq=1000000)
  M5.begin()
  Widgets.fillScreen(0x222222)



def loop():
  print(os.getcwd())
  print(os.listdir('/sd/' + str(os.getcwd())))
  Speaker.begin()


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
