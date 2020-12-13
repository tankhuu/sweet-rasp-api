import RPi.GPIO as GPIO

class AlarmController:
  def __init__(self, pin: int, relay_type: str = 'LOW'):
    # Constants
    RELAY_TYPES = ['LOW', 'HIGH']

    # Validate Arguments
    if pin > 40:
      raise 'Raspberry Pi 3 has only 40 pins!'
    if relay_type not in RELAY_TYPES:
      raise 'Supported Relay Type is LOW & HIGH!'
    
    self.ALARM_PIN = pin
    print('default relay on with voltage: LOW')
    self.RELAY_ON = GPIO.LOW
    self.RELAY_OFF = GPIO.HIGH
    if relay_type == 'HIGH':
      print('relay on with voltage: HIGH')
      self.RELAY_ON = GPIO.HIGH
      self.RELAY_OFF = GPIO.LOW

    print(f'setup RPi with pin: {self.ALARM_PIN} for relay type: {relay_type}')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.ALARM_PIN, GPIO.OUT)

  def on(self):
    print(f'on relay pin: {self.ALARM_PIN}')
    GPIO.output(self.ALARM_PIN, self.RELAY_ON)

  def off(self):
    print(f'off relay pin: {self.ALARM_PIN}')
    GPIO.output(self.ALARM_PIN, self.RELAY_OFF)

  def clean(self):
    print(f'cleanup pin before exit')
    GPIO.cleanup()

