import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

while True:
  GPIO.output(17, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(4, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(22, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(27, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(17, GPIO.LOW)
  time.sleep(1)
  GPIO.output(4, GPIO.LOW)
  time.sleep(1)
  GPIO.output(22, GPIO.LOW)
  time.sleep(1)
  GPIO.output(27, GPIO.LOW)
  time.sleep(1)
